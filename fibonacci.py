import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibonacci():
   nextt = 1
   previous = 0
   limit = 50
   found = 0
   respost = "0"

   while (found < limit):
       tmp = nextt
       nextt = nextt + previous
       previous = tmp
       found=found+1
       respost+= "," + str(nextt)

   return respost + "."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

