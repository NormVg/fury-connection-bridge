from flask import Flask
from flask import request


app = Flask(__name__)



@app.route('/', methods = ['GET','POST'])
def code():
    return '<-THIS-IS-FURY-SERVER-PROGRAM->'

@app.route('/commandavalable')
def command_avalable():
    avalable = open("./commandAvalable.txt",'r')
    reply = avalable.read()
    avalable.close()

    return reply

@app.route('/responseavalable')
def response_avalable():
    avalable = open("./responseAvalable.txt",'r')
    reply = avalable.read()
    avalable.close()

    return reply

@app.route('/response')
def response():
    command = open("./response.txt",'r')
    reply = command.read()
    command.close()
    command = open("./response.txt",'r+')
    command.truncate(0)
    command.close()
    avalable = open("./responseAvalable.txt",'r+')
    avalable.truncate(0)
    avalable.close()
    avalable = open("./responseAvalable.txt",'w')
    avalable.write("False")
    avalable.close()
    
    return reply

@app.route('/command')
def command():
    command = open("./command.txt",'r')
    reply = command.read()
    command.close()
    command = open("./command.txt",'r+')
    command.truncate(0)
    command.close()
    avalable = open("./commandAvalable.txt",'r+')
    avalable.truncate(0)
    avalable.close()
    avalable = open("./commandAvalable.txt",'w')
    avalable.write("False")
    avalable.close()
    
    return reply

@app.route('/responseinput')
def response_input():
    text = str(request.args.get('input'))
    command = open("./response.txt",'w')
    command.write(text)
    command.close()
    avalable = open("./responseAvalable.txt",'r+')
    avalable.truncate(0)
    avalable.close()
    avalable = open("./responseAvalable.txt",'w')
    avalable.write("True")
    avalable.close()
    
    return ""

@app.route('/commandinput')
def command_input():
    text = str(request.args.get('input'))
    command = open("./command.txt",'w')
    command.write(text)
    command.close()
    avalable = open("./commandAvalable.txt",'r+')
    avalable.truncate(0)
    avalable.close()
    avalable = open("./commandAvalable.txt",'w')
    avalable.write("True")
    avalable.close()
    
    return ""

if __name__ == '__main__':

    app.run()