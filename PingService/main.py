from flask import Flask, request
from flask_restplus import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/ping')
class Ping(Resource):
    def post(self):
        url = request.form['url']
        return requests.get(url, verify=False).text

@api.route('/health')
class Health(Resource):
    def get(self):
        return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8080)
