from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

todos = {}


class HoraFormatada(Resource):
    def get(self):
        now = datetime.now()
        return {"hora_atual": now.isoformat()}


api.add_resource(HoraFormatada, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # importante, para que o docker 'escute' a sua requisição.
