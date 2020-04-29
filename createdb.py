from application import *


def main():
    # execute & create all model classes in db
    db.create_all()


if __name__ == "__main__":
    # allow us to on CLI(command line) interact to flask application
    with app.app_context():
        main()




