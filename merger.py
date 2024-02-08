from pypdf import PdfWriter
import os

merger = PdfWriter()

# Add files to the merger one by one
for file in os.listdir('./pdfs'):
    if file.endswith('.pdf'):
        print(file)
        merger.append("./pdfs/"+file)
    merger.write('result.pdf')  # write the merged PDF to disk
