# Data Analysis & Management Bot
**Description**:
# Installation
```
git clone https://github.com/kaustav1996/bot-data_analysis-management/
sudo bash ./bot-data_analysis-management/setup.sh
```

# Others

```
# ./bot-data_analysis-management/
sudo pip install -r requirements.txt
```
### Modules
**Speech** (backend_functions/speech.py)
* Text to Speech:

```
import speech #This works when you are in the same folder as speech.py so change this accordingly
speech.say('Hello!')
```

* Speech to Text:

First Set These Variables According to your need in **speech.py** .

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

* Punctuate
```
speech.punctuate('Hello I am Kaustav') # returns the string with punctuations
Hello, I am Kaustav
```
* Sentiment Analysis
```
sentences = ["VADER is smart, handsome, and funny.",      # positive sentence example
            "VADER is not smart, handsome, nor funny.",   # negation sentence example
            "VADER is smart, handsome, and funny!",       # punctuation emphasis handled correctly (sentiment intensity adjusted)
            "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
            "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
            "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
            "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",# booster words & punctuation make this close to ceiling for score
            "The book was good.",                                     # positive sentence
            "The book was kind of good.",                 # qualified positive sentence is handled correctly (intensity adjusted)
            "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
            "At least it isn't a horrible book.",         # negated negative sentence with contraction
            "Make sure you :) or :D today!",              # emoticons handled
            "Today SUX!",                                 # negative slang with capitalization emphasis
            "Today only kinda sux! But I'll get by, lol"  # mixed sentiment example with slang and constrastive conjunction "but"
             ]
for sentence in sentences:
  print(str(speech.sentiment(sentence)))
```
See https://github.com/cjhutto/vaderSentiment#python-code-example for more .
