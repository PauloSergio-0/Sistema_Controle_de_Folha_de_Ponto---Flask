from flask import Flask, request, jsonify

def routes_funcionario(app:Flask):
    
    @app.route("/funcionario/cadastro", methods =["POST"])
    def cadastro():
        json_funcionario = request.json()
        if json_funcionario:
            return jsonify({"message": "escravo recebido",
                            "data": json_funcionario})