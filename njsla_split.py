import pdfplumber as pdfp
import pypdf
from pypdf import PdfReader,PdfWriter
import string as str
import pandas as pd
import numpy as np

def njsla_split(pdf_object):
    """
    Splits New Jersey Student Learning Assessments (NJSLA) Individual Student Reports (ISR)
    into a two page pdf document based on student satte id (SID)

    Parameters
    ----------
    pdf_object: string
        The file path of the NJSLA ISR export
    
    """
    reader = PdfReader(pdf_object)
    writer = PdfWriter() #--> instantiating PDF Writer
    doc_len = len(reader.pages)/2 #--> returning number of pages, divided by 2 to account for 2 page documents

    # variables
    search_text = 'ID: ' #--> substring search
    search_text_len = len(search_text) #--> len of search text
    sid_len = 10 #--> len of SID
    sid = [] #--> creating an empty list

    
    # opening pdf with pdfplumber and searching for text using a for loop
    with pdfp.open(pdf_object) as pdf:
        for pages in pdf.pages: #--> range to extract text from odd pages
            text = pages.extract_text_simple() #--> creating string object
            start = text.find(search_text) #--> assigning the index of the search text to start variable
            end = start +  search_text_len + sid_len #--> assigning the index to stop extracting text to the end variable
            sid.append(text[start:end]) #--> appening extracted text from the PDF to list
 
    # create a dataframe for extracted SIDs
    sid_df = pd.DataFrame({'State ID':sid})
    
    # removing blank values
    sid_df = sid_df[sid_df['State ID'] != '']
    
    # data cleaning
    sid_df['State ID'] = sid_df['State ID'].str.split(':').str[1].str.strip()
    
    # reseting index
    sid_df = sid_df.reset_index(drop = True)

    # creating rows variables
    rows = sid_df.shape[0]
    
    # creating count variable to coun the number of iteration through the loop
    count = 0
    
    # creating qa variable
    qa = doc_len == rows #--> doc_len and SID list should be equal
    
    # conditional statement - if conditional met will run for loop, if not will print error statement
    if qa == True:
    
        for i, page_num in enumerate(range(0,len(reader.pages),2)): #--> creating a range of all even pages of the document
            writer = PdfWriter() #--> resets the writer object in each iteration of the loop
            page_name = sid_df['State ID'].iloc[i]  #--> returns other id based on indexing of df based on 
            writer.add_page(reader.pages[page_num]) #--> adding first page to PDF export
            if page_num <= len(reader.pages): #--> conditional to ensure that that page num is not outside of index
                writer.add_page(reader.pages[page_num +1]) #--> adding second page to PDF export
            with open(f'{page_name}.pdf','wb') as f: #--> file writing
                    writer.write(f)
            count += 1 #--> adding 1 to the count object after each iteration through the for loop
    
        print(f'{count} PDF documents were successfully created')  #--> print statement to confirm that documents were created
                
    else:
        print(f'There is an error, and the for loop was not excecuted.')
    
