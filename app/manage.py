from flask import Flask
from flask_script import Manager

def main():
    app = Flask(__name__)
    manager = Manager(app)
    manager.run()

if __name__ == '__main__':
    main()
