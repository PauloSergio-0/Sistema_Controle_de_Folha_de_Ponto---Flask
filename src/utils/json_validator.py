class JsonValidator:
    
    def jsonClientes(json: dict):
        
        keys_funcionario = ['ID', 'Nome', 'CPF', 'Departamento', 'Status']
        
        
        for key, value in json.items():
            
            if not key in keys_funcionario:
                return {"status": False, "error": ""}
            
            if not type(value) == str:
                return {"status": False, "error": ""}