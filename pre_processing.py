# importing module to read PDFs
import PyPDF2 

#get titles of each paper
from PyPDF2 import PdfFileReader
#import counter to count num of words in our 
from collections import Counter

#import regular expressions for data-cleaning
import re 

#import os to create list of files
import os

#import string to create remove puctuation function
import string

def get_pdf_title(pdf_list):
		all_titles_list = []
    for pdf in pdf_list:
      pdf_reader = PdfFileReader(open(pdf_file_path, "rb")) 
    	all_titles_list.append(str(pdf_reader.getDocumentInfo().title))
    return all_titles_list

def get_pdf_content(pdfs):
  '''Input: pdf_name (str)
     Output: list of words per page
     [[content for pdf1], [content for pdf2]]
  '''
  	
    all_pdf_content = []
    
    
    for pdf in pdfs:
      # creating a pdf file object 
      pdfFileObj = open(pdf, 'rb') 

      # creating a pdf reader object 
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


      #get number of pages in the pdf file 
      n = pdfReader.numPages

      #create a list that will hold all words 
      content = []

      #loop though each page to each words from each page
      for i in range(n):
          #create page object
          pageObj = pdfReader.getPage(i) 

          # extracting text from page
          content.append(pageObj.extractText())

      # closing the pdf file object 
      pdfFileObj.close() 

      #return our num of words 
      all_pdf_content.append(content[0])
    
    return all_pdf_content

def merge_content_titles(list_pdf_content,list_pdf_titles):
  length = len(list_pdf_content)
  res = {}
  for idx in range(length):
    res[list_pdf_titles[idx]] = list_pdf_content[idx]
  return res

all_pdfs = []
for root, dirs, files in os.walk("./pdfs"):
    for filename in files:
        all_pdfs.append("./pdfs/" + filename)
        
#create list of all words for our paper 
list_pdf_content = get_pdf_content(all_pdfs) 
list_pdf_titles = get_pdf_title(all_pdfs)
corpus = merge_content_titles(list_pdf_content, list_pdf_title)
m_content = list(corpus.values())