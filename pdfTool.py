from pypdf import PdfWriter
from pypdf import PdfReader

input = open("input.pdf", "rb")
pdfReader = PdfReader(input)
merger = PdfWriter()

# count number of pages
totalPages = len(pdfReader.pages)
print(f"Total Pages: {totalPages}")
for i in range(int(totalPages/2)):
    merger.append(pdfReader,[i])
    merger.append(pdfReader,[totalPages-i-1])
merger.write("merged-pdf.pdf")
merger.close()
