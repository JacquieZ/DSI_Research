import os
import glob
import PyPDF2

# pdf files in the directory
os.chdir("/Users/jacquie/Desktop/DSI_Reasearch/Test_PDFs/")
all_filenames = [i for i in glob.glob('*.pdf')]

for file_name in all_filenames:
    pdfFileObj = open("/Users/jacquie/Desktop/DSI_Reasearch/Test_PDFs/" + file_name, 'rb')

    # pure file name
    file_name = file_name[0:len(all_filenames[0]) - 4]

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # save text files to another folder
    save_path = "/Users/jacquie/Desktop/DSI_Reasearch/Test_PDFs/converted_text"
    save_file = file_name + ".txt"
    completeName = os.path.join(save_path, save_file)
    f = open(completeName, 'a')

    # number of pages in the pdf file
    pages = pdfReader.numPages

    # creating a page object extract text page by page
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        f.write(pageObj.extractText())
        f.write('\n')

    f.close()

    # closing the pdf file object
    pdfFileObj.close()