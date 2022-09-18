# Keyword Context Tracking with NLP

# Product Goal
As undergraduate students in computer science and engineering, we often find ourselves tediously scanning scholary articles. To streamline this process, we decided to use Cohere's NLP API to help us find what we are searching for.

# Product Overview
In order to search through the document, the user enters keywords related to a topic/concept/event/etc. Instead of individually using CRTL+F to find instances of these words, the NLP model extracts meaning from the cluster of keywords and furthermore searches the document for the same meaning within the text. Using parsers, we are able to locate and return the 3 most likey page numbers to be refereneced. This process is done through a simple user interface that lets the user input a path to the pdf file of the article and the keywords they are searching for. 


<img width= "700" height = "300" src= "https://user-images.githubusercontent.com/106715980/190882390-d4e8f456-807d-4b12-8fc1-909fca31a6f1.png">



## Skills Used: 

`Python`, `Cohere NLP API`, `Pandas`, `React.js`, `FLask`, `Data Dreprocessing`


## Background information
At `Hack the North 2022` @UWaterloo, Cohere AI, a sponsor of the event, challenged hackers to use their NLP API in hacks. 

<img width= "300" height = "100" src= "https://user-images.githubusercontent.com/106715980/190878315-862325db-7dba-4a06-b9f1-9c3ea647aedc.png">
<img width= "200" height = "200" src= "https://user-images.githubusercontent.com/106715980/190880544-46444940-316c-497a-a925-d1aa0adf6c69.png">


# Preprocessing
A large part of this project was data preprocessing. The first step was to use a libary that converts PDF to text. To isolate paragraphs, we initially parsed by double line breaks ("\n\n"). We then furthermore took out single spaces and new line characters. Each individual lists of page number and paragraphs were combined into a data frame using `Pandas`



# NLP API
The benefit of using an NLP API is that the machine learning aspects of the project are done at a very high level and thus are user friendly. Using the annoy library, we set up a plane for word vectors. Using the API's built in functions we embedded both the users keywords and  the text from the article. Again using the API's built in function, the vectors of the keywords and those in each paragraph were compared on the annoy vector indicie. The smaller the ditance between them, the more similair the vectors are. Since we could only perform this search on one keyword at a time, we averaged the embeddings of each keyword. This average was used to compare to the embeddings of the text and ultimately determine a most likey paragraph of interest. Referencing back to the dataframe we could identify and output the page that the paragraph is on, along with the first few words so the user can identify which section it is referencing. 



## User Interface
Using React.js and Flask, a demo interface was created allowing students to easily upload their keywords and the path to the pdf. An output screen showing the selected paragraph 


# Steps Moving Forward
A large issue we faced in the creation of this project was the parsing of the pdf. We needed the text to be parsed by paragraphs while also keeping track of the page number. The process was difficult because splitting the text by new lines ("\n") or double new lines ("\n\n") did not work on every PDF we tried. In other words, different PDF's have different formatting. Moving forward, we would like to create a parsing tool that works on more PDF's, AKA more generability. 

![image](https://user-images.githubusercontent.com/106715980/190882503-617eeee7-9464-46c3-8688-944dd4f52746.png)


