from flask import Flask, jsonify

app = Flask(__name__)

# Define uma rota para a API que retorna as informações coletadas pelo NFC
@app.route('/nfc')
def get_nfc_data():
    # Aqui você pode adicionar o código para coletar as informações do NFC
    nfc_data = "Exemplo de informações coletadas pelo NFC"
    return jsonify(nfc_data)

if __name__ == '__main__':
    app.run(debug=True)
