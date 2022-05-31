import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api
from message_namespace import *

# Common API initialization
app = Flask(__name__)

# Expand the Swagger UI when it is loaded: list or full
app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
# Globally enable validating
app.config["RESTPLUS_VALIDATE"] = True
# Enable or disable the mask field, by default X-Fields
app.config["RESTPLUS_MASK_SWAGGER"] = False

app_api = Api(
    app,
    title = "MESSAGE APPLICATION",
    contact = "message@qlik.com",
    description = "Simple message application which checks if a word is a palindrome."
    )

app_api.add_namespace(get_message_namespace(app_api))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)