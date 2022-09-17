# Keyword Context Tracking with NLP

# Product Goal
As undergraduate students in computer science and engineering, we often find ourselves tediously scanning scholary articles. To sreamline this process, we decided to use Cohere's NLP API to help us find what we are searching for.

# Product Overview
In order to search through the document, the user enters keywords related to a topic/concept/event/etc. Instead of individually using CRTL+F to find instances of these words, the NLP model extracts meaning from the cluster of keywords and furthermore searches the document for the same meaning within the text. Using parsers, we are able to locate and return the page number to be refereneced. This process is done through a simple user interface that lets the user input the pdf file of the article and the keywords they are searching for. 


## Background information
At `Hack the North 2022` @UWaterloo, Cohere AI, a sponsor of the event, challenged hackers to use their NLP API in hacks. 

<img width= "300" height = "100" src= "https://user-images.githubusercontent.com/106715980/190878315-862325db-7dba-4a06-b9f1-9c3ea647aedc.png">


## User Interface
Using React.js, a demo interface was created allowing students to easoly upload their keywords and the path to the pdf.

# NLP API
The benefit of using an NLP API is that the machine learning aspect is very high level and user friengly.  split the pdf file into paragrpahs, we embbed the keywords using the API, when a user enters a keyword, it will obtain the average embedded values and try to match with the most similaor vectors found in the text. the API has several functions for us to use, there is classification, embedding, generation,

# Steps Moving Forward
An large issue we faces in the creation of this project with the parsing of the pdf. We needed the text to be parsed by paragraphs while also keeping track of the page number. The process was difficult because splitting the text by new lines ("\n") or double new lines ("\n\n") did not work on every PDF we tried. Moving forward, we would like to create a parsing tool that works on more PDF's, in other words- more generability. 

