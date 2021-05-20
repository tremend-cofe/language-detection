from flask import Flask, request, jsonify, has_request_context
from whatlangid import WhatLangId
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


# logging.getLogger().addHandler(default_handler)

@app.route('/detect', methods=['POST'])
def detect():
    lang = WhatLangId()
    if request.method == "POST":
        app.logger.warning(request.json['text'])
        detected = lang.predict_lang(request.json['text'])
        if request.json['original_language'] != detected:
            app.logger.warning("Detected, {id}, {requested}, {detected}".format(requested=request.json['original_language'] , id=request.json['id'],detected=detected  ))
        return jsonify({"detected": detected })

    return jsonify({"detected": ""})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
