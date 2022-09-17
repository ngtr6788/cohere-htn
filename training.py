from typing import List
import cohere
from annoy import AnnoyIndex

co = cohere.Client("QMXjhSthJ4z6tKjLYRDPcCPYNkt2YXZRKI3flVfl")

def train_model_from_string_list(
    texts: List[str], save_file: str
) -> AnnoyIndex:
    """"""
    search_index = AnnoyIndex(4096, "angular")
    try:
        search_index.load(f"{save_file}.ann")
    except OSError:
        response = co.embed(texts).embeddings

        for i in range(len(response)):
            search_index.add_item(i, response[i])

        search_index.build(10)  # 10 trees
        search_index.save(f"{save_file}.ann")

    return search_index
