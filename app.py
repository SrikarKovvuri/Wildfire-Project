import time
from threading import Thread, Event

import pandas as pd
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

class DataThread(Thread):
    def __init__(self):
        self.delay = 1
        super(DataThread, self).__init__()

    def fetchData(self):
        """
        Get data from API, in this case, simply generate random numbers
        """
        while not thread_stop_event.isSet():
            data = pd.read_csv('https://firms.modaps.eosdis.nasa.gov/api/area/csv/e37426bd3839b651a03d67a1c0bee54e/VIIRS_SNPP_NRT/world/1/2023-07-11')
            socketio.emit('newdata', {'data': data.to_dict()}, namespace='/test')
            time.sleep(self.delay)

    def run(self):
        self.fetchData()

@app.route('/')
def index():
    return render_template('wildfires.html')

@app.route('/data')
def get_data():
    data = load_data()
    return jsonify(data[['Latitude', 'Longitude']].to_dict(orient='records')) if data is not None else jsonify({'error': 'Failed to load data.'})

@app.route('/data/visualization')
def data_visualization():
    data = load_data()
    if data is None:
        return jsonify({'error': 'Failed to load data.'})
    satellite_counts = data['satellite'].value_counts().reset_index()
    satellite_counts.columns = ['Satellite', 'Count']
    json_data = satellite_counts.to_json(orient='records')
    return json_data

@app.route('/heatmap')
def generate_heatmap():
    data = load_data()
    if data is None:
        return jsonify({'error': 'Failed to load data.'})
    heatmap_data = data[['Latitude', 'Longitude']].values.tolist()
    return jsonify({'heatmap_data': heatmap_data})

def load_data():
    try:
        data = pd.read_csv('https://firms.modaps.eosdis.nasa.gov/api/area/csv/e37426bd3839b651a03d67a1c0bee54e/VIIRS_SNPP_NRT/world/1/2023-07-11')
        data.columns = data.columns.str.strip()
        data['Latitude'] = data['latitude']
        data['Longitude'] = data['longitude']
    except Exception as e:
        print("An error occurred while loading the CSV file:", e)
        return None
    return data

if __name__ == '__main__':
    socketio.run(app)
