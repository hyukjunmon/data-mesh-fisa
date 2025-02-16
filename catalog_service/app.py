from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    """데이터 카탈로그 반환"""
    with open("catalog.json") as f:
        catalog = json.load(f)
    return jsonify(catalog)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
