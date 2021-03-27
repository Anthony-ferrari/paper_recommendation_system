# importing module to read PDFs
import PyPDF2 

#import counter to count num of words in our 
from collections import Counter

#import regular expressions for data-cleaning
import re 

#import os to create list of files
import os

#import string to create remove puctuation function
import string

#create counter with stopwords
stopwords = Counter(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])
print(stopwords)

#finding files within pdfs folder
papers = []
for root, dirs, files in os.walk("./pdfs"):
    for filename in files:
        papers.append(filename)
print(papers)

def get_num_of_words(pdf):
  '''Input: pdf_name (str)
     Output: list of words per page
  '''
    # creating a pdf file object 
    pdfFileObj = open(pdf, 'rb') 
      
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


    #get number of pages in the pdf file 
    n = pdfReader.numPages

    #create a list that will hold all words 
    num_of_words = []

    #loop though each page to each words from each page
    for i in range(n):
        #create page object
        pageObj = pdfReader.getPage(i) 
      
        # extracting text from page
        num_of_words.append(pageObj.extractText())
      
    # closing the pdf file object 
    pdfFileObj.close() 

    #return our num of words 
    return num_of_words

#create list of all words for our paper 
number_of_words = get_num_of_words('kotas_paper.pdf')
print(len(number_of_words))

#create list for second paper 
number_of_words1 = get_num_of_words('kotas_paper1.pdf')

#create directionary with common symbol distortions
distortions = {"˜":"ff","ˇ":"ff","˝":"fi","˚":"fl"}

#linear time replace function
def faster_replace(number_of_words_string):
  '''Input: pdf_name (str)
     Output: list of words per page
  '''
  cleaned_string = []
  for char in number_of_words_string:
    if char in distortions:
      cleaned_string.append(distortions[char])
    else:
      cleaned_string.append(char)
  return cleaned_string

#clean up data
def clean_data(number_of_words):
  unclean = ''.join(number_of_words)
  return faster_replace(unclean)

#function to remove any non_essential words
def remove_stopwords(clean_text):
  return [word for word in clean_text if word not in stopwords]

#create directionary of punctutation to speed up run time from linear to constant
punct = Counter(string.punctuation)

#remove punctuation
def remove_punctuation(cleaned_text):
  return [char for char in cleaned_text if char not in punct]

#create a dictionary with the number of words 
def create_word_counter(clean_pdf):
  joint_words = ' '.join(clean)
  joint_words.lower()
  split_words = joint_words.split()
  return Counter(split_words)