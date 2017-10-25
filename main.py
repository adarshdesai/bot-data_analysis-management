import os.path
import sys
import json
from backend_functions import speech
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
	 while(1 and apiIntent!="bye"):
	    stringu=raw_input()
	    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

	    request = ai.text_request()

	    request.lang = 'de'  # optional, default value equal 'en'

	    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

	    request.query = stringu
	    
	    response = request.getresponse()
	   
	    string = response.read().decode('utf-8')
	    json_obj = json.loads(string)
	    apiIntent=json_obj["result"]["metadata"]["intentName"]
	    if(apiIntent=="nameIntent"):
		username=
	    apiResp=json_obj["result"]["fulfillment"]["speech"]
	    speech.say(apiResp)

if __name__ == '__main__':
	main()
