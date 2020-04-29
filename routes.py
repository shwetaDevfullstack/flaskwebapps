from flask import render_template
from models import *


def route(app):
    @app.route('/')
    def index(user='shweta'):
        return render_template('index.html', name=user)

    @app.route('/flights')
    def flights():
        flight_data = Flight.query.all()
        return render_template('flights.html', flights=flight_data)

    @app.route('/flight/<int:flight_id>')
    def flight(flight_id):
        if flight_id:
            flight_data = Flight.query.get(flight_id)
            # flight_data = {'id': 1, 'source': 'New York', 'destination': 'New Delhi', 'duration': 489}
            return render_template('flight.html', flight=flight_data)
        else:
            return render_template('error.html')

    @app.route('/book/<int:flight_id>')
    def book(flight_id):
        if flight_id:
            flight_data = Flight.query.all()
            selected_flight = Flight.query.get(flight_id)

            # flight_data = [{1: {'id': 1, 'source': 'New York', 'destination': 'New Delhi', 'duration': 489}},
            #                {2: {'id': 2, 'source': 'Tokyo', 'destination': 'New York', 'duration': 789}},
            #                {3: {'id': 3, 'source': 'San Jose', 'destination': 'New Delhi', 'duration': 490}},
            #                {4: {'id': 4, 'source': 'San Francisco', 'destination': 'New Delhi', 'duration': 478}}]
            # selected_flight = flight_data.pop(int(flight_id)-1)

            return render_template('book.html', flights=flight_data, selected_flight=selected_flight.origin+' - '+selected_flight.destination)
        else:
            return render_template('error.html')