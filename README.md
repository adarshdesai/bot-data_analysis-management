# Data Analysis & Management Bot
```
git clone https://github.com/kaustav1996/bot-data_analysis-management/
```
```
# ./bot-data_analysis-management/
sudo pip install -r requirements.txt
```
### Modules
* **Speech** :
             * Text to Speech:
               ```
               import speech #This works when you are in the same folder as speech.py so change this accordingly
               speech.say('Hello!')
               ```
             * Speech to Text:
                 First Set These Variables According to your need in **speech.py**
                 ```
                  THRESHOLD = 120
                  CHUNK_SIZE = 80
                  FORMAT = pyaudio.paInt16
                  RATE = 44100
                 ```
                 Then
                 ```
                 speech.record_to_file('temp.wav') # saves recording to temp.wav.You can use any path instead of just the working dir.
                 ```
             * Speech Recognition
               ```
               speech.recognise('temp.wav') # returns the google api result as string.
               ```
               To use other APIs use the SpeechRecognition module available using pip.
