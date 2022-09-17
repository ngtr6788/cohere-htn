import cohere
import PyPDF2

key = cohere.Client("QMXjhSthJ4z6tKjLYRDPcCPYNkt2YXZRKI3flVfl")


pdffileobj=open('Natural_Language_Processing.pdf','rb')#open the pdf file




pdfreader=PyPDF2.PdfFileReader(pdffileobj)#reads the pdf that we bring in 
NumOfPages=pdfreader.numPages #gets the number of pages in the book
#NumOfPages=2 #hard sets the number of pages we will be parsing for testing reasons
myList=[]


print(NumOfPages)
for i in range (NumOfPages): #iterates through pages
    pageObj= pdfreader.getPage(i) #
    PdfAsText= pageObj.extractText() #Extracts the text from the PDF
    myList.append(PdfAsText.split("\n"))
    






for i in range(NumOfPages):
    for j in range(len(myList[i])):
        print(myList[i][j])







#print(split_paragraph2(myList[0]))

