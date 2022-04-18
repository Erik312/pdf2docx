####################################
#                                  #
# Simple Pdf text 2 docx converter.#
# Supports pdf text parsing only.  #
#                                  #
# Written by: Erik Ramos           #
#                                  #
#                                  #
####################################



import os
import pdfplumber

def read_pdf(file_object):
    """ read and extract text """
    file = pdfplumber.open(file_object)
    data1 = file.pages[0]
    text_data = data1.extract_text()
    return(text_data)



def create_doc():
    """ main application creates docx/ parse text """
    print("Enter path of pdf file")
    user_file = input("> ")
    data_to_write = read_pdf(user_file)
    print(data_to_write)
    new_doc = open("wonka.docx","w+")
    new_doc.write(data_to_write)
    new_doc.close()
    return






if __name__ == "__main__":
    create_doc()
