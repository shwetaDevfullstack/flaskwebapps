from flask import Flask
from models import *
from routes import route

# from operator import itemgetter
# import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://varunshweta:tidh@localhost/travelport'

# safely bind database handler to Flask
#  app in a way that manages connections
db.init_app(app)

# initializing & calling routes
route(app)


def main():
    pass

    # flights = Flight.query.all()
    # for flight in flights:
    #    print(flight)


if __name__ == "__main__":
    # allow us to on CLI(command line) interact to flask application
    with app.app_context():
        main()



