from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = "domain_order.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/customers', methods=['GET'])
def get_customers():
    """고객 데이터 반환"""
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM customers").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
