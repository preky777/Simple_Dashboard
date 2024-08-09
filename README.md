# Li-ion Battery Dashboard

## Requirements
- Python 3.x
- MySQL
- Flask
- Streamlit
- Plotly

## Setup Instructions
1. Install dependencies:
    ```bash
    pip install pandas sqlalchemy pymysql flask streamlit plotly requests
    ```

2. Set up the MySQL database:
    - Create a database `li_ion_dashboard`.
    - Run the Python script to import data into MySQL.

3. Start the Flask API:
    ```bash
    python fl.py
    ```

4. Run the Streamlit dashboard:
    ```bash
    streamlit run Dashboard.py --server.port 8080
    ```

5. Access the dashboard at `http://localhost:8080`.

## Project Structure
- `Dashboard.py`: Streamlit app script.
- `fl.py`: Flask API for data retrieval.
- `README.md`: Instructions for running the project.

## Dashboard Preview
![Animation](https://github.com/user-attachments/assets/6371da21-826b-4572-b6e6-51e30aadcbe5)
