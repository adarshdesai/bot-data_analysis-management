import os.path
import sys
import json
from backend_functions import speech, nameSearch, name
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
	    apiIntent=json_obj["result"]["metadata"]["intentName"]
	    if(apiIntent=="find-name" or apiIntent=="nameIntent"):
		stringu[0]=stringu[0].upper()
		for i in range(1,len(stringu)):
			if(stringu[i-1]==" "):
				stringu[i]=stringu[i].upper()
		username=name.find_name(stringu)
		apiResp="Hello "+username+"! How may I help you?"
	    else:
	    	apiResp=json_obj["result"]["fulfillment"]["speech"]
	    #print("Intent name: "+apiIntent)
	    speech.say(apiResp)
	    print("Agent : "+apiResp)

if __name__ == '__main__':
	main()
