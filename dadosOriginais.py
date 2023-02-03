import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class DadosOriginais:
    def tratarDados():
        anos = list(map(str, list(range(1992,2031))))
        encontrado = False
        tabela = []
        meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
        resultado = pd.DataFrame(tabela, columns=['ano','mes','baseIPCA'])
        with open('ipca_texto.txt','r',encoding="utf-8") as file:
            ano_atual = ''
            mes_atual = 0
            for linha in file:
                linha  = linha.strip()
                
                if(linha in anos): 
                    encontrado = True
                    ano_atual = linha
                    continue

                if encontrado and linha != '':
                    resultado = resultado.append({'ano' : ano_atual , 'mes' : meses[mes_atual], 'baseIPCA' : linha} , ignore_index=True)
                    mes_atual = mes_atual +1

                elif encontrado:
                    encontrado = False
                    mes_atual = 0

        return resultado        