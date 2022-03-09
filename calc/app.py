# Put your app in here.

from flask import Flask
app = Flask(__name__)
from flask import request
import calc.operations as Math

@app.route("/<operation>")
def math(operation):

    a = int(request.args["a"])
    b = int(request.args["b"])
    
    fn = {'add': Math.add, 'sub': Math.sub, 'mult': Math.mult, 'div': Math.div}

    result = fn[operation](a,b)

    return f"{result}"