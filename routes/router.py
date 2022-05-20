import boto3
from flask import Blueprint, request, jsonify, make_response

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(("127.0.0.1", 12345))


client = boto3.client('comprehend')

comprehend_router = Blueprint("comprehend_router", __name__, url_prefix="/api/v1/comprehend/")


@watson_router.route("/keyPhrases", methods=["POST"])
def get_key_phrases():
    body = request.get_json()
    print("BODY: ", body)
    text = body["text"]

    if text:
        client.detect_key_phrases(Text=text, LanguageCode='en')
        return make_response(jsonify({"success": True}, 200))

    else:
        return make_response(jsonify({"success": False}), 500)