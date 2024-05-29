# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Clear-Trail!</h1><h2>This is Version 2</h2><img src='https://media.licdn.com/dms/image/C510BAQGYGct9oxYKxA/company-logo_200_200/0/1630590592479/cleartrail_technologies_logo?e=2147483647&v=beta&t=nYF6pZLKxNBONLe5sJ7WSnQD7ollvMgQx6xZhrodPKM' width='40%' alt='Pinehead @ Clear-Trail'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
