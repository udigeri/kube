##!/usr/local/bin python
from flask import Flask, request
import sys
import os
import datetime

app = Flask(__name__)

def hello():
    picture = "w95"
    try:
        picture = sys.argv[1].strip()
    except Exception as e:
        print(e)

    return "Udi 1.0.0<br />{}<br />OS: {}<br />ServerIP: {}:{} - {}<br />RemoteIP: {}:{}<br /> \
        <img src=\"static/{}.jpg\">".format(
        datetime.datetime.now(),
        os.getenv('OS'), 
        request.environ['SERVER_NAME'],
        request.environ['SERVER_PORT'],
        os.getenv('HOSTNAME'),
        request.environ['REMOTE_ADDR'],
        request.environ['REMOTE_PORT'],
        picture
)

@app.route("/")
def html():
    return "<!DOCTYPE html><html><head><meta http-equiv=\"refresh\" content=\"1\"></head><body style=\"font-size:30px; color:blue;\">{}</body></html>".format(hello())


if __name__== "__main__":
    print("Udi 1.0.0\nOS: {}\nContainer: {}".format(
        os.getenv('OS'), 
        os.getenv('HOSTNAME')))

    app.run(host="0.0.0.0", port=80)