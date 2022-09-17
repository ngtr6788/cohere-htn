import cohere
import pandas as pd
from annoy import AnnoyIndex

key = cohere.Client("QMXjhSthJ4z6tKjLYRDPcCPYNkt2YXZRKI3flVfl")
input_value = ["Hello there, my name is bob", "When are we going to get a notebook", "I really need coffee right now", "Coffee beans are needed" , "We are going to drive a car", "I am going to charge my laptop", "I am using my phone"]
pdf_data = pd.DataFrame(input_value, columns= ["text"])

user_input = ["computer device", "school supply"]

def train_model_from_string_list(pdf_data, save_file) -> AnnoyIndex:
    """
    Train the model based on the tokens from the pdf input

    Parameters:
    pdf_data (DataFrame): Contains the text tokens from the pdf
    save_file (String): Saving file name  
    """
    search_index = AnnoyIndex(4096, "angular")
    try:
        search_index.load(f"{save_file}.ann")
    except OSError:
        response = key.embed(pdf_data["text"]).embeddings

        for i in range(len(response)):
            search_index.add_item(i, response[i])

        search_index.build(10)  # 10 trees
        search_index.save(f"{save_file}.ann")

    return search_index

def do_semantic_search(pdf_data, user_input, search_index):
    '''
    Performs a semantic search on the input by the user

    Paramters:
    pdf_data (DataFrame): Contains the text tokens from the pdf
    user_input (list[String]): keywords to do meaningful searches of
    search_index (AnnoyIndex): index embeddings 
    '''
    input_embed = key.embed(texts = user_input).embeddings

    #Get average embeddings for the vectors
    sum_input_embed = [sum(vectors) for vectors in zip(*input_embed)]
    average_input_embeddings = [vector/len(user_input) for vector in sum_input_embed]

    # Retrieve the nearest neighbors
    similar_item_ids = search_index.get_nns_by_vector(average_input_embeddings, 3, include_distances=True)

    # Format the results
    results = pd.DataFrame(data={'texts': pdf_data.iloc[similar_item_ids[0]]['text'], 'distance': similar_item_ids[1]})
    print(f"Keyword Search:'{user_input}'\nNearest neighbors: '{results}'")


search_index = train_model_from_string_list(pdf_data, "test")
do_semantic_search(pdf_data, user_input, search_index)