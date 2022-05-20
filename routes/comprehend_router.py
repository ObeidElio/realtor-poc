import boto3
import json
import requests
from flask import Blueprint, request, jsonify, make_response

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(("127.0.0.1", 12345))


client = boto3.client('comprehend')

comprehend_router = Blueprint("comprehend_router", __name__, url_prefix="/api/v1/comprehend")


# @comprehend_router.route("/keyPhrases", methods=["POST"])
def get_key_phrases(body):
    # body = request.get_json()
    # print("BODY: ", body)
    text = body["Text"]

    if text:
        response = client.detect_key_phrases(Text=text, LanguageCode='en')
        return response
    else:
        return 'ERROR'


def get_entities(body):
    print("BODY: ", body)
    text = body["Text"]

    if text:
        response = client.detect_entities(Text=text, LanguageCode='en')
        return response

    else:
        return 'ERROR'

@comprehend_router.route("/bot", methods=["POST"])
def get_weather():
    body = request.get_json()
    entities = get_entities(body)
    key_phrases = get_key_phrases(body)

    print("Key phrases", key_phrases['KeyPhrases'][0]['Text'])

    if 'news' in key_phrases['KeyPhrases'][0]['Text']:



        headers = {'x-api-key':'8A3H-BV4WSuw4LXRawpvgI4vF9dgtY7a5H7zw7MDw4k','Access-Control-Allow-Origin':'*'}
        PARAMS = {'q': entities['Entities'][0]['Text']}
        r = requests.get("https://api.newscatcherapi.com/v2/search",params=PARAMS,headers = headers )
        data = r.json()
        news_data = [i['title'] for i in data['articles']]
        #print(news_data[:5])
        return {"entities":entities['Entities'],"keyPhrases":key_phrases['KeyPhrases'],"data":news_data[:5]}

    elif 'weather' in key_phrases['KeyPhrases'][0]['Text']:

        headers = {'Authorization': 'Bearer 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', 'Content-Type':'application/json','key':'0b378e34d4e3454cad6103446220304'}
        PARAMS = {'q': entities['Entities'][0]['Text']}
        r = requests.post("http://api.weatherapi.com/v1/current.json",params=PARAMS,headers = headers )
        data = r.json()
        weather_data = [data['current']['condition']['text']]
        #print('WEATHER DATA',weather_data)
        return {"entities":entities['Entities'],"keyPhrases":key_phrases['KeyPhrases'],"data":weather_data}
    else:
        return {"entities":entities['Entities'],"keyPhrases":key_phrases['KeyPhrases'],"data":{}}




