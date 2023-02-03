import pdfquery
import pandas as pd

# pdf = pdfquery.PDFQuery('ipca.pdf')
# pdf.load()
# pdf.tree.write('pdfXML.xml', pretty_print = True)

anos = list(map(str, list(range(1992,2023))))
ano_atual = ''
cont = 0
encontrado = False
buffer = []
resultado = pd.DataFrame()
print('Anos:',anos)
with open('ipca_texto.txt','r',encoding="utf-8") as file:
    for linha in file:
        linha  = linha.strip()
        if(linha in anos): 
            print('Trabalhando o ano:',linha)
            encontrado = True
            ano_atual = linha
            continue
        if encontrado and linha != '':
            buffer.append(linha)
        elif encontrado:
            encontrado = False
            resultado[ano_atual] = buffer
            buffer = []

print(resultado.head())
resultado.to_excel('resultado.xlsx')


print('Final do codigo ::::')


# import tabula as tb
# import pandas as pd
# import re

# file = 'ipca.pdf'
# data = tb.read_pdf(file, area = (200, 94, 400, 790), pages = '1')
# print(data)