from flask import Flask
app = Flask(__name__)
app.secret_key = "No secrets here..."
DATABASE = "dojos_and_ninjas_schema"
