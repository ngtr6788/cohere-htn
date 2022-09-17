from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # In real life, production code, not recommended, don't do this

@app.route("/search", methods=["POST"])
def search():
    if request.is_json:
        json_request = request.get_json()
        text_path = json_request["textPath"]
        keywords = json_request["keywords"]

        # TODO: Integrate this HTTP endpoint with the semantic search logic
        return {"textPath": text_path, "keywords": keywords}
    else:
        return {"error": "Request must be JSON"}, 415
