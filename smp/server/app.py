from flask import Flask
from server.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

