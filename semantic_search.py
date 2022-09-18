import cohere
import pandas as pd
import PyPDF2
from annoy import AnnoyIndex

key = cohere.Client("QMXjhSthJ4z6tKjLYRDPcCPYNkt2YXZRKI3flVfl")
user_input = ["similarities and differences"]


def extract_info(pdf_path):
    '''
    Parses the pdf file into paragraphs for search
    
    Parameters:
    pdf_path (String): path to the pdf with the information
    '''
    pdf_file_obj = open(pdf_path,'rb') #open the pdf file

    pdfreader=PyPDF2.PdfFileReader(pdf_file_obj)#reads the pdf that we bring in 
    num_pages =pdfreader.numPages
    extracted_info = []
    page_info = []

    for page in range (num_pages): #iterates through pages
        page_obj= pdfreader.getPage(page)
        pdf_as_text = page_obj.extractText() #Extracts the text from the PDF
        paragraphs = pdf_as_text.split("\n \n")
        for i in range(len(paragraphs)):
            paragraphs[i] = paragraphs[i].strip(" \n")
        extracted_info += paragraphs
        page_info += [page + 1] * len(paragraphs)

    #Remove whitenoise in extracted_information   
    pdf_data = pd.DataFrame(columns= ["text", "page_number"]) 
    for i in range(len(extracted_info)):
        if extracted_info[i] != " " and extracted_info[i] != " \n " and extracted_info[i] != "":
            temp_frame = pd.DataFrame({"text": [extracted_info[i]], "page_number": [page_info[i]]}, columns= ["text", "page_number"])
            pdf_data = pd.concat([pdf_data, temp_frame])

    return pdf_data
    
def train_model_from_string_list(pdf_data) -> AnnoyIndex:
    """
    Train the model based on the tokens from the pdf input

    Parameters:
    pdf_data (DataFrame): Contains the text tokens from the pdf
    save_file (String): Saving file name  
    """
    search_index = AnnoyIndex(4096, "angular")
    

    response = key.embed(list(pdf_data["text"])).embeddings

    for i in range(len(response)):
        search_index.add_item(i, response[i])

    search_index.build(10)  # 10 trees
        
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
    results = pd.DataFrame(data={'texts': pdf_data.iloc[similar_item_ids[0]]['text'], 'distance': similar_item_ids[1], "page_number":pdf_data.iloc[similar_item_ids[0]]['page_number'] })
    print(f"Keyword Search:'{user_input}'\nNearest neighbors: '{results}'")

    return results

