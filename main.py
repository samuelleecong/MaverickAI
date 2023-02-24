# Flask server for bot
from __future__ import print_function
import os
from flask import Flask, request
import requests
from maverickQA import MaverickQA
from maverickChat import MaverickGPT

app = Flask('app')


@app.route('/')
def load_server():
  return 'Yay! server up and running! Users can now query MaverickAi!'


@app.route('/sms_callback', methods=['POST'])

def sms_callback():
  print(request.form)
  global sender, reply_to
  sender = request.form['to']
  reply_to = request.form['from']
  
  if sender == '5959':
    reply = MaverickQA(request.form['text'])

  else: #59009
    reply = MaverickGPT(request.form['text'])
  
  #print(reply)
  sms_response(reply_to, reply)
  
  return 'success', 201
  
api_key = os.environ['at_api']
username = 'sandbox'

def sms_response(send_to, message):
  print("sending back")
  requests.post("https://api.sandbox.africastalking.com/version1/messaging",
                data={
                  "username": username,
                  "to": send_to,
                  "message": message,
                  "from": sender,
                },
                headers={
                  "apiKey": api_key,
                  "Accept": "application/json",
                  "Content-Type": "application/x-www-form-urlencoded"
                })


app.run(host='0.0.0.0', port=8080)
