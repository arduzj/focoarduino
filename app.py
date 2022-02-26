from flask import Flask
from flask_restful import Api, Resource
import serial

sar = serial.Serial("COM3", 9600)

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self, name):
        if (name == 'on'):
            sar.write("on".encode("ascii"))
            return {'hello': 'Foco encendido'}
        else:
            sar.write("of".encode("ascii"))
            return {'saludo' : 'Foco apagado'}

api.add_resource(HelloWorld, '/foco/<string:name>')

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
