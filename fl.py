from flask import Flask, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Connect to the MySQL database
engine = create_engine('mysql+pymysql://root:rp#$9882@localhost/li_ion_dashboard')

@app.route('/data/<int:cell_id>', methods=['GET'])
def get_data(cell_id):
    query = f"SELECT * FROM cell_data WHERE cell_id = {cell_id}"
    data = pd.read_sql(query, con=engine)
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(port=8051)
