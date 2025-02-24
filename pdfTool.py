from pypdf import PdfWriter
from pypdf import PdfReader
import sys
import os

args = sys.argv

input = open(args[1], "rb")
pdfReader = PdfReader(input)
merger = PdfWriter()

# ページ交換
totalPages = len(pdfReader.pages)
print(f"Total Pages: {totalPages}")
for i in range(int(totalPages/2)):
    merger.append(pdfReader,[i])
    merger.append(pdfReader,[totalPages-i-1])
merger.write("merged-pdf.pdf")
merger.close()

os.rename(args[1],f"{args[1]}.org")
os.rename("merged-pdf.pdf",args[1])
# 単純マージ

