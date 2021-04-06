from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/info')
class Info(Resource):
    def get(self):
        return {"Receiver": "Cisco is the best!"}

if __name__ == '__main__':
    app.run(debug=False)
