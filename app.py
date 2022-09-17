from typing import List
from flask import Flask, request

app = Flask(__name__)


@app.post("/search")
def search():
    if request.is_json:
        json_request = request.get_json()
        text_path = json_request["textPath"]
        keywords: List[str] = json_request["keywords"]

        # TODO: Integrate this HTTP endpoint with the semantic search logic
        return {"textPath": text_path, "keywords": keywords}
