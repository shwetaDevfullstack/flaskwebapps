import csv
from application import *
from models import *


def main():
    f = open('flights.csv')
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flit = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flit)
        db.session.commit()


if __name__ == "__main__":
    # allow us to on CLI(command line) interact to flask application
    with app.app_context():
        main()




