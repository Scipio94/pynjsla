import pdfplumber as pdfp
from pypdf import PdfReader,PdfWriter
import numpy as np
from tqdm import tqdm
from pathlib import Path

def njsla_batch_split(pdf_file_folder):
    """
    Splits New Jersey Student Learning Assessments (NJSLA) Individual Student Reports (ISR)
    into a two page pdf document based on student state id (SID)

    Parameters
    ----------
    pdf_file_folder: string
        The file path of the folder where the NJSLA ISRs are located.
    
    """
    # creating folder path variable
    folder_path = Path(pdf_file_folder)
    
    # for loop leveraging iterdir() method to iterate over files in folder
    for file_path in folder_path.iterdir():
        pdf_object = f"{file_path}"
        reader = PdfReader(pdf_object)
        doc_len = len(reader.pages)//2 #--> returning number of pages, divided by 2 to account for 2 page documents
    
        # variables
        search_text = 'ID: ' #--> substring search
        search_text_len = len(search_text) #--> len of search text
        sid_len = 10 #--> len of SID
        sid = [] #--> creating an empty list
        
        # opening pdf with pdfplumber and searching for text using a for loop
        with pdfp.open(pdf_object) as pdf:
            for pages in tqdm(pdf.pages[::2],desc = 'Retrieving SIDs'): #--> extracting text from every other page and using tqdm to track progress
                text = pages.extract_text_simple() #--> creating string object
                start = text.find(search_text) #--> assigning the index of the search text to start variable
                end = start +  search_text_len + sid_len #--> assigning the index to stop extracting text to the end variable
                sid.append(text[start:end].split(':')[1].strip()) #--> appening and manipulating extracted text from PDF file

        #creating variable for length of the sid list
        list_len = len(sid)
        count = 0

        # conditional statement - if conditional met will run for loop, if not will print error statement
        if doc_len == list_len:
            #error handling
            try:
                for i, page_num in enumerate(tqdm(range(0,len(reader.pages),2),desc = 'Splitting NJSLA ISRs')): #--> creating a range of all even pages of the document
                        writer = PdfWriter() #--> resets the writer object in each iteration of the loop
                        page_name = sid[i]  #--> returns sid based on list indexing 
                        writer.add_page(reader.pages[page_num]) #--> adding first page to PDF export
                        if page_num <= len(reader.pages): #--> conditional to ensure that that page num is not outside of index
                            writer.add_page(reader.pages[page_num +1]) #--> adding second page to PDF export
                        with open(f'{page_name}.pdf','wb') as f: #--> file writing
                                writer.write(f)
                                count += 1
                print(f'{count} PDF documents were successfully created')  #--> print statement to confirm that documents were created')
            # error description
            except Exception as e:
                print("An exception occurred:", type(e).__name__)
