# scrapper_pdf
Um servidor Flask que serve um CRUD para trabalhar dados de um PDF especifico.
O PDF em questao foi tranformado em texto utilizando uma ferramenta OCR online, disponivel em:

https://pdftotext.com/pt/

Alem do Flask, sao utilizadas as bibliotecas Pandas e sqlite3, sendo sqlite o banco de dados do servico.

O servidor pode ser executado diretamente atraves dos arquivos python ou atraves de um container docker.
Para levantar o container, basta criar a imagem apartir do arquivo <b>dockerfile</b>.

Para executa-lo localmente, primeiro instale as bibliotecas utilizadas. Na pasta do projeto, usando pip:

```
pip install -r requirements.txt
```

Apos isso, e possivel iniciar o servidor Flask executando o script <b>app.py</b>:

```
python app.py
```

Com o servidor iniciado, e possivel acessar a documentacao via swagger, na rota:

```
http://localhost:5002/swagger
```
