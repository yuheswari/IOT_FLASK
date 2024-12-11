import os
from flask import Flask
app = Flask(__name__)
basename = '/iotcloud'

@app.route('/hello')
def hello_world():
   return "<h1>MANU SORRY</h1>"
@app.route(basename+'/whoami')
def whoami():
    return os.popen('whoami').read()

@app.route(basename+'/cpuinfo')
def cpuinfo():
    return os.popen('cpuinfo').read()

@app.route(basename+'/echo')
def echo():
    return os.popen('echo').read()

if __name__ == '__main__':
   app.run(host='172.30.9.107',port=7000,debug=True)