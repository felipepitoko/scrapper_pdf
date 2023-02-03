from flask import Flask, request, jsonify, json
from database import Database
from dadosOriginais import DadosOriginais

df = DadosOriginais.tratarDados()
connection = Database.create_connection()
Database.criar_tabela(connection)
Database.alimentar_primeiros_dados(connection,df)
connection.close()

app = Flask(__name__)

@app.route('/consultaIPCACompleta', methods=['GET'])
def consulta_completa():
    conn = Database.create_connection()
    basesIPCA = Database.consultar_todos(conn)
    conn.close()

    response = app.response_class(
        response=json.dumps(basesIPCA),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/consultaIPCA', methods=['GET'])
def consulta_parametros():
    args = request.args.to_dict()
    ano, mes = '', ''
    ano = args['ano'] if 'ano' in args else ''
    mes = args['mes'] if 'mes' in args else ''

    conn = Database.create_connection()
    basesIPCA = Database.consultar_mes_ano(conn,ano,mes)
    conn.close()

    if(len(basesIPCA) == 0):
        return app.response_class(
            response=json.dumps({
                'mensagem': 'Dado nao encontrado para estes parametros.',
                'mes': mes,
                'ano': ano
            }),
            status=404,
            mimetype='application/json'
        )   

    return app.response_class(
        response=json.dumps(basesIPCA),
        status=200,
        mimetype='application/json'
    )

@app.route('/inserirIPCA', methods=['POST'])
def inserir_base():
    data = json.loads(request.data)    
    meses_validos = ['janeiro','fevereiro','marco','abril','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    ano, mes, baseIPCA = '', '', 0.0
    ano = data['ano'] if 'ano' in data else ''
    mes = data['mes'] if 'mes' in data and data['mes'] in meses_validos else ''
    baseIPCA = data['baseIPCA'] if 'baseIPCA' in data else 0.0

    if(ano == '' or mes == '' or baseIPCA == 0.0):
        response = app.response_class(
            response=json.dumps({
                'mensagem':'Para criar um registro, envie ano, mes e baseIPCA validos!'
            }),
            status=400,
            mimetype='application/json'
        )
        return response

    conn = Database.create_connection()
    dado_criado = Database.inserir_registro(conn,ano,mes,baseIPCA)
    conn.close()

    if(len(dado_criado) == 0):
        return app.response_class(
            response=json.dumps({
                'mensagem':'Ja ha um valor registrado para este mes/ano. Caso deseje atualizar utilize /atualizar'
            }),
            status=400,
            mimetype='application/json'
        )    

    return app.response_class(
            response=json.dumps(dado_criado),
            status=200,
            mimetype='application/json'
        )

@app.route('/atualizarIPCA', methods=['PUT'])
def atualizar_registro():
    data = json.loads(request.data) 
    ano, mes, baseIPCA = '', '', 0.0
    ano = data['ano'] if 'ano' in data else ''
    mes = data['mes'] if 'mes' in data else ''
    baseIPCA = data['baseIPCA'] if 'baseIPCA' in data else 0.0

    if(ano == '' or mes == ''):
        response = app.response_class(
            response=json.dumps({
                'mensagem':'Para atualizar um registro, envie ano, mes e baseIPCA.'
            }),
            status=400,
            mimetype='application/json'
        )
        return response

    conn = Database.create_connection()
    dadoAtualizado = Database.atualizar_registro(conn,baseIPCA,ano,mes)
    conn.close()

    if (len(dadoAtualizado) == 0):
        return app.response_class(
        response=json.dumps({
            'mensagem': 'Registro nao encontrado.',
            'mes': mes,
            'ano': ano
        }),
        status=404,
        mimetype='application/json'
        )

    return app.response_class(
        response=json.dumps(dadoAtualizado),
        status=200,
        mimetype='application/json'
    )

@app.route('/excluirIPCA', methods=['DELETE'])
def excluir_registro():
    args = json.loads(request.data) 
    ano, mes = '', ''
    ano = args['ano'] if 'ano' in args else ''
    mes = args['mes'] if 'mes' in args else ''

    if(ano == '' or mes == ''):
        response = app.response_class(
            response=json.dumps({
                'mensagem':'Para excluir um registro, envie ano e mes.'
            }),
            status=400,
            mimetype='application/json'
        )
        return response

    conn = Database.create_connection()
    dadoExcluido = Database.excluir_registro(conn,ano,mes)
    conn.close()

    if (len(dadoExcluido) == 0):
        return app.response_class(
        response=json.dumps({
            'mensagem': 'Registro nao encontrado para exclusao.',
            'mes': mes,
            'ano': ano
        }),
        status=404,
        mimetype='application/json'
        )

    return app.response_class(
        response=json.dumps(dadoExcluido),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5002)