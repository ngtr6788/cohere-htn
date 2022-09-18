from typing import List
from flask import Flask, request
from flask_cors import CORS

from semantic_search import (
    do_semantic_search,
    extract_info,
    train_model_from_string_list,
)

app = Flask(__name__)
CORS(app)  # In real life, production code, not recommended, don't do this


@app.route("/search", methods=["POST"])
def search():
    if request.is_json:
        json_request = request.get_json()
        text_path: str = json_request["textPath"]
        keywords: List[str] = json_request["keywords"]

        pdf_data = extract_info(text_path)
        search_index = train_model_from_string_list(pdf_data)
        result = do_semantic_search(
            pdf_data, keywords, search_index
        )  # result is a DataFrame and it returns top three results

        for _, row in result.iterrows():
            print(row)

        return {
            "result": [
                {"text": row["texts"], "pageNumber": row["page_number"]}
                for _, row in result.iterrows()
            ]
        }
    else:
        return {"error": "Request must be JSON"}, 415
