from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

THRESHOLD = 80
CHUNK_SIZE = 50
FORMAT = pyaudio.paInt16
RATE = 44100
def punctuate(s):
	import os
	import subprocess
	s='%20'.join(s.strip().split(" "))
	proc = subprocess.Popen("curl -d 'text="+s+"' http://bark.phon.ioc.ee/punctuator", stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return out.decode("utf-8", "ignore")
	
def say(s):
	import pyttsx
	engine = pyttsx.init()
	if not isinstance(s, (list, tuple)):
        	s = [s]
	for i in s:
		engine.say(i)
	engine.runAndWait()

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()
def recognise(voice):
	import speech_recognition as sr
	import os
	r = sr.Recognizer()
	with sr.Microphone() as source:
		AUDIO_FILE_EN = os.path.join(os.path.dirname(os.path.realpath(__file__)), voice)
		with sr.AudioFile(AUDIO_FILE_EN) as source: audio = r.record(source)	 
	# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    return r.recognize_google(audio)
	except sr.UnknownValueError:
	    return "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
	    return "Could not request results from Google Speech Recognition service; {0}".format(e)
def sentiment(s):
	from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
	analyzer = SentimentIntensityAnalyzer()
	vs = analyzer.polarity_scores(s)
	return vs

def voice_to_text():
	import speech_recognition as sr  
   
 	# obtain audio from the microphone  
 	r = sr.Recognizer()  
 	with sr.Microphone() as source:  
   		print("Please wait. Calibrating microphone...")  
   		# listen for 5 seconds and create the ambient noise energy level  
   		r.adjust_for_ambient_noise(source, duration=5)  
   		print("Say something!")  
   		audio = r.listen(source)  
   
 	# recognize speech using Sphinx  
 	try:  
   		print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
 	except sr.UnknownValueError:  
   		print("Sphinx could not understand audio")  
 	except sr.RequestError as e:  
   		print("Sphinx error; {0}".format(e))  
