import pandas as pd
from flask import Flask
from flask import jsonify


    

tb_cliente = pd.read_excel("Base Financeiro.xlsx", sheet_name= "Cliente")
tb_fornecedor = pd.read_excel("Base Financeiro.xlsx", sheet_name= "Fornecedor")
tb_banco = pd.read_excel("Base Financeiro.xlsx", sheet_name= "Banco")
tb_pagamentos = pd.read_excel("Base Financeiro.xlsx", sheet_name= "Pagamentos")
tb_recebimentos = pd.read_excel("Base Financeiro.xlsx", sheet_name= "Recebimentos")

app = Flask(__name__) # Cria o site

@app.route('/')
def cliente():
  dic_cliente = tb_cliente.to_dict()
  return jsonify(dic_cliente)

@app.route('/fornecedor')
def fornecedor():
  dic_fornecedor = tb_fornecedor.to_dict()
  return jsonify(dic_fornecedor)

@app.route('/banco')
def banco():
  dic_banco = tb_banco.to_dict()
  return jsonify(dic_banco)

@app.route('/pagamentos')
def pagamentos():
  dic_pagamentos = tb_pagamentos.to_dict()
  return jsonify(dic_pagamentos)

@app.route('/recebimentos')
def recebimentos():
  dic_recebimentos = tb_recebimentos.to_dict()
  return jsonify(dic_recebimentos)



if __name__ == '__main__':
    app.run()