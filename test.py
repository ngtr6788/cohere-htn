import cohere
import pandas as pd
from annoy import AnnoyIndex

key = cohere.Client("QMXjhSthJ4z6tKjLYRDPcCPYNkt2YXZRKI3flVfl")

input = ["Hello there, my name is bob", "When are we going to get a notebook", "I really need coffee right now", "Coffee beans are needed" , "We are going to drive a car", "I am going to charge my laptop", "I am using my phone"]
df = pd.DataFrame(input, columns= ["text"])

embeds = key.embed(texts=list(df['text']), model='large', truncate='LEFT').embeddings
search_index = AnnoyIndex(4096, 'angular')
for i in range(len(embeds)):
    search_index.add_item(i, embeds[i])

search_index.build(10) # 10 trees
search_index.save('test.ann')


query = ["computer device", "school supply"]
# Get the query's embedding
query_embed = key.embed(texts=query, model="large", truncate="LEFT").embeddings

#Get average results for the vectors
sum_query_embed = [sum(vectors) for vectors in zip(*query_embed)]
average_query_embed = [vector/len(query) for vector in sum_query_embed]

# Retrieve the nearest neighbors
similar_item_ids = search_index.get_nns_by_vector(average_query_embed,10,include_distances=True)

# Format the results
results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'], 'distance': similar_item_ids[1]})
print(f"Query:'{query}'\nNearest neighbors: '{results}'")
