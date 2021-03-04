#!/usr/bin/python
from flask import Flask, render_template
app = Flask(__name__)

import socket
import json
import requests

@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')

##Test data for tabulator lib
@app.route('/api/index.json', methods=['GET'])
def data():
    return '''
{
  "data":
    [
      {"ip":"1.1.1.1",  "data":"abcdefghijklmnopqrstuvwxyz"},
      {"ip":"1.1.1.2",  "data":"1234567890"},
      {"ip":"1.1.1.3",  "data":"This is a test"},
      {"ip":"1.1.1.4",  "data":"This is a test too"},
      {"ip":"1.1.1.5",  "data":"This is a test three"},
      {"ip":"1.1.1.6",  "data":"This is a not a test. Wait, i lied it is a test,"},
      {"ip":"1.1.1.7",  "data":"This might be a test ??"},
      {"ip":"1.1.1.8",  "data":"We have falash back poeple"},
      {"ip":"1.1.1.9",  "data":"This is the most fun I have had since not dieing in the war!"},
      {"ip":"1.1.1.10", "data":"We fired Phillip. Thats just what we did back them."},
      {"ip":"1.1.1.11", "data":"!@#$%^&*()_+=-/.,?><;"},
    ]
}
'''

@app.route('/ip.html', methods=['GET'])
def ip_lookup():
    return "Test"

@app.route('/api/ip/<string:this_ip>', methods=['GET'])
def ip_view(this_ip):
    answer = json.loads('{}')
    try:
        check_ip = socket.inet_aton(this_ip)
    except:
        check_ip = False
        return False
    try:
        hostname = socket.gethostbyaddr(this_ip)
    except:
        hostname = False
    this_answer = {"ip":this_ip, "gethostbyaddr":hostname}
    answer.update(this_answer)
    response = requests.get("https://freegeoip.app/json/" + this_ip)
    answer.update(response.json())
    return json.dumps(answer)

if __name__ == "__main__":
    app.run()
