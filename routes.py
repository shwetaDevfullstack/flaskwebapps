from flask import render_template, request, redirect, url_for, jsonify
from models import *


def route(app):
    @app.route('/')
    def index(user='shweta'):
        return render_template('index.html', name=user)

    @app.route('/success')
    def success():
        return render_template('success.html', message='Flight Booked Successfully!!!')

    @app.route('/flights')
    def flights():
        """List All Flights"""

        flight_data = Flight.query.all()
        return render_template('flights.html', flights=flight_data)

    @app.route('/flight/<int:flight_id>')
    def flight(flight_id):
        """Get Flight Data"""

        if flight_id:
            flight_data = Flight.query.get(flight_id)
            return render_template('flight.html', flight=flight_data)
        else:
            return render_template('error.html')

    @app.route('/book/<int:flight_id>')
    def book(flight_id):
        if flight_id:
            flight_data = Flight.query.all()
            selected_flight = Flight.query.get(flight_id)
            # get all passengers against that flight id
            passengers = selected_flight.passengers

            return render_template('book.html', flights=flight_data, selected_flight=selected_flight, passengers=passengers)
        else:
            return render_template('error.html')

    @app.route('/book', methods=['POST'])
    def book_flight():
        """Book a flight"""

        # Get form information
        name = request.form['name']
        try:
            flight_id = int(request.form['flt_id'])
        except ValueError:
            return render_template('error.html', message='Invalid flight id!')

        # checking flight-id exist or not
        flight = Flight.query.get(flight_id)
        if flight is None:
            return render_template('error.html', message='No such flight!')

        # Add Passenger
        flight.add_passenger(name)
        return redirect(url_for('success'))
        # passenger = Passenger(name, flight_id)
        # db.session.add(passenger)
        # db.session.commit()
        # return render_template("success.html", message="Flight booked!")

    @app.route('/api/flight/<int:flight_id>')
    def flight_api(flight_id):
        if flight_id:
            flight = Flight.query.get(flight_id)
            if flight is None:
                return jsonify({'error': 'No such flight!!!'})

            return jsonify({
                "origin": flight.origin,
                "destination": flight.destination,
                "duration": flight.duration
            })
        else:
            return jsonify({'error': 'Invalid flight id!!!'})
