from pypdf import PdfReader

meses = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
reader = PdfReader("ipca.pdf")
text = ""

# Iterate through each page of the PDF
for page in range(len(reader.pages)):
    # Extract the text from the page
    text += reader.pages[page].extract_text()
    with open('pdf2.txt','w') as file:
        file.write(text)

def apenas_numeros(valores):
    for string in valores:
        print('>'+string)
        if(string.strip() in meses):
            print('Vou apagar:',string)
            valores.remove(string)
        if (string == ''):
            print('Vou apagar:',string)
            valores.remove(string)
        # else:
        #     try:
        #         float(string)
        #     except ValueError:
        #         valores.remove(string)
    
    return valores

with open('pdf2.txt','r') as texto:
    for linha in texto:
        palavras = linha.strip().split(' ')
        if (palavras[0] in meses):
            print(linha)
            palavras = apenas_numeros(palavras)
            print(palavras)
            print('--------------------------------------')
            # valores = list(map(lambda r: apenas_numeros(r), palavras))
            # print(valores)




print('FIM DO CODIGO :::::::')