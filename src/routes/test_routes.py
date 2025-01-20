from flask import Flask, jsonify

def test_routes(app: Flask):
    
    @app.route('/test', methods = ['GET'])
    def test():
        return jsonify({'message': 'esssa bomba funcionou'})
    
    