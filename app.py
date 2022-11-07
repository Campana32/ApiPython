from http import client
from multiprocessing.sharedctypes import Value
from flask import Flask, request
from bd import clientes

app = Flask(__name__)

@app.route("/", methods=['GET'])
def clientess_get():
    return clientes

@app.route("/post", methods=['POST'])
def clientes_creat():
    novo_clientes = request.json
    if novo_clientes in clientes:
        return "<h1>clientes já cadastrado!</h1>"
    else:
        clientes.append(novo_clientes)
        return clientes
    
@app.route("/delete", methods=['DELETE'])
def clientes_delet():
    delet_clientes = request.json
    if delet_clientes in clientes:
        clientes.remove(delet_clientes)
        return clientes
    else:
        return "<h1>clientes não encontrado!</h1>"
    
@app.route("/put", methods=['PUT'])
def clientes_put():
    put_clientes = request.json
    idt = put_clientes.get("id")
    nome = put_clientes.get("nome")
    
    clientes[idt]["nome"] = nome
    return clientes
        
@app.route("/patch", methods=['PATCH'])
def clientes_patch():
    patch_clientes = request.json
    id = patch_clientes.get("id")
    nome = patch_clientes.get("nome")
    cpf = patch_clientes.get("cpf")
    DataNascimento = patch_clientes.get("DataNascimento")
    Telefone = patch_clientes.get("Telefone")
    
    clientes[id]["nome"] = nome
    clientes[id]["cpf"] = cpf
    clientes[id]["DataNascimento"] = DataNascimento
    clientes[id]["Telefone"] = Telefone   
    return clientes  

app.run()