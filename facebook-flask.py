import requests
import json

from flask import Flask, request

class facebook_interface:
    def __init__(self, access_token, verify_token):
        self.access_token= access_token
        self.verify_token= verify_token
        self.graph_url   = 'https://graph.facebook.com/v2.8/'
    def get_posts(self, user):
        data = {}
        return None
    def reply(self, user_id, message):
        data = {
            'recipient': {
                'id': user_id
            },
            'message': {
                'text': message
            }
        }
        response = requests.post(self.graph_url + '/me/messages/?access_token=' + access_token, json=data)
        return None
    def search(self, query, qeury_type):
        data = {
            'q': query,
            'type': qeury_type,
            'access_token': access_token
        }
        response = requests.get(self.graph_url + '/search/', params=data)
        return json.loads(response.text)
    def listen_messages(self):
        app  = Flask(__name__)
        
        @app.route('/', methods=['GET'])
        def handle_verification():
            if request.args['hub.verify_token'] == self.verify_token:
                return request.args['hub.challenge']
            else:
                return "Invalid verification token"
        @app.route('/', methods=['POST'])
        def handle_incoming_messages():
            data    = request.json
            sender  = data['entry'][0]['messaging'][0]['sender']['id']
            message = data['entry'][0]['messaging'][0]['message']['text']
            reply(sender, message)
        
        app.run(debug=True, port=8888)

user = 'me'
access_token = ''
verify_token = ''
interface = facebook_interface(access_token, verify_token)
interface.listen_messages()