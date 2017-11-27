import os.path
import csv
import sys
import json
import login
from backend_functions import speech, integrate
curr_path = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.abspath(os.path.join(curr_path, os.pardir))

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '7df34bbf717b412d97b7056c110b967e'


def main():
     apiIntent=""
     username, account_id = (-1, -1)
     while (username == -1 and account_id == -1):
         username, account_id = login.login_func()
     name = ""
     integrate.printOut(int(account_id))
     with open(os.path.join(par_dir, "bot-data_analysis-management/data/credentials.csv"), 'r') as file:
         reader = csv.reader(file, delimiter=',')
         for row in reader:
             if (row[1] == username):
                 name = row[0]
     talk = 0
     while(apiIntent!="bye"):
        stringu=raw_input("User : ")
        stringu=speech.punctuate(stringu)
        userSentiment=str(speech.sentiment(stringu))
        print ("User Sentiment : "+userSentiment)
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'de'  # optional, default value equal 'en'

        request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

        request.query = stringu

        response = request.getresponse()

        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        apiIntent=""
        try:
            apiIntent=json_obj["result"]["metadata"]["intentName"]
        except:
            apiIntent = ""
        if (talk==0):
            apiResp="Hello "+name+"! How may I help you?"
        else:
            apiResp=json_obj["result"]["fulfillment"]["speech"]
        #print("Intent name: "+apiIntent)
        speech.say(apiResp)
        print("Agent : "+apiResp)
        talk=talk+1
if __name__ == '__main__':
	main()
