from flask import Flask, render_template
from operator import itemgetter
import json

app = Flask(__name__)


@app.route('/')
def index(user='shweta'):
    return render_template('index.html', name=user)


@app.route('/flights')
def flights(flight_id=None):
    flight_data = [{'id': 1, 'source': 'New York', 'destination': 'New Delhi', 'duration': 489},
                   {'id': 2, 'source': 'Tokyo', 'destination': 'New York', 'duration': 789},
                   {'id': 3, 'source': 'San Jose', 'destination': 'New Delhi', 'duration': 490},
                   {'id': 4, 'source': 'San Francisco', 'destination': 'New Delhi', 'duration': 478}]
    return render_template('flights.html', flights=flight_data)


@app.route('/flight/<int:flight_id>')
def flight(flight_id):
    if flight_id:
        flight_data = {'id': 1, 'source': 'New York', 'destination': 'New Delhi', 'duration': 489}
        return render_template('flight.html', flight=flight_data)
    else:
        return render_template('error.html')


@app.route('/book/<int:flight_id>')
def book(flight_id):
    if flight_id:
        #flight_data = [{'id': 1, 'source': 'New York', 'destination': 'New Delhi', 'duration': 489},
        #               {'id': 2, 'source': 'Tokyo', 'destination': 'New York', 'duration': 789},
        #               {'id': 3, 'source': 'San Jose', 'destination': 'New Delhi', 'duration': 490},
        #               {'id': 4, 'source': 'San Francisco', 'destination': 'New Delhi', 'duration': 478}]

        flight_data = [{1: {'id': 1, 'source': 'New York', 'destination': 'New Delhi', 'duration': 489}},
                       {2: {'id': 2, 'source': 'Tokyo', 'destination': 'New York', 'duration': 789}},
                       {3: {'id': 3, 'source': 'San Jose', 'destination': 'New Delhi', 'duration': 490}},
                       {4: {'id': 4, 'source': 'San Francisco', 'destination': 'New Delhi', 'duration': 478}}]

        selected_flight = flight_data.pop(int(flight_id)-1)
        print(selected_flight)
        return render_template('book.html', flights=flight_data, selected_flight=selected_flight[flight_id]['source']+' - '+selected_flight[flight_id]['destination'])
    else:
        return render_template('error.html')



