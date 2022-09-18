# Keyword Context Tracking with NLP

# Product Goal
As undergraduate students in computer science and engineering, we often find ourselves tediously scanning scholary articles. To streamline this process, we decided to use Cohere's NLP API to help us find what we are searching for.

# Product Overview
In order to search through the document, the user enters keywords related to a topic/concept/event/etc. Instead of individually using CRTL+F to find instances of these words, the NLP model extracts meaning from the cluster of keywords and furthermore searches the document for the same meaning within the text. Using parsers, we are able to locate and return the page number to be refereneced. This process is done through a simple user interface that lets the user input the pdf file of the article and the keywords they are searching for. 

## Skills Used: 

`Python`, `Cohere NLP API`, `Pandas`, `React.js`, `FLask`, `Data Dreprocessing`


## Background information
At `Hack the North 2022` @UWaterloo, Cohere AI, a sponsor of the event, challenged hackers to use their NLP API in hacks. 

<img width= "300" height = "100" src= "https://user-images.githubusercontent.com/106715980/190878315-862325db-7dba-4a06-b9f1-9c3ea647aedc.png">
<img width= "200" height = "200" src= "https://user-images.githubusercontent.com/106715980/190880544-46444940-316c-497a-a925-d1aa0adf6c69.png">


# Preprocessing
A large part of this project was data preprocessing. The first step was to use a libary that converts PDF to text. To isolate paragraphs, we initially parsed by double line breaks ("\n\n"). We then furthermore took out single spaces and new line characters. Each individual lists of page number and paragraphs were combined into a data frame using `Pandas`



# NLP API
The benefit of using an NLP API is that the machine learning aspects of the project are done at a very high level and are user friendly. Using the annoy library, we set up a plane for word vectors. Using the API's built in functions we embedded both the keywords and the text from the article. Again using the API's built in function, the vectors of the keywords and those in each paragraph were compared on the annoy vector indicie. The smaller the ditance between them, the more similair the vectors are. Since we could only perform this search on one keyword at a time, we individually found each keywords closest match in a loop and averaged all values out to determine a most likey paragraph of interest. Referencing back to the dataframe we could identify and output the page that the paragraph is on along with the first few words so the user can identify which section it is referencing. 



## User Interface
Using React.js and Flask, a demo interface was created allowing students to easoly upload their keywords and the path to the pdf.


# Steps Moving Forward
An large issue we faces in the creation of this project with the parsing of the pdf. We needed the text to be parsed by paragraphs while also keeping track of the page number. The process was difficult because splitting the text by new lines ("\n") or double new lines ("\n\n") did not work on every PDF we tried. Moving forward, we would like to create a parsing tool that works on more PDF's, in other words- more generability. 

