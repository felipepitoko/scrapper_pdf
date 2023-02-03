import fitz

# Open the PDF file
pdf_document = fitz.open("ipca.pdf")

# Extract the text from each page in the PDF
text = ""
for page in pdf_document:
    text += page.get_text("text")

print(text)