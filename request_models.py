from flask_restplus import reqparse

POSTMESSAGE_REQUEST_MODEL = reqparse.RequestParser()
POSTMESSAGE_REQUEST_MODEL.add_argument("User", action="append", type = str, required=True, help="Enter User")
POSTMESSAGE_REQUEST_MODEL.add_argument("Message", action="append", type = str, required=True, help="Enter Message")

GETMESSAGE_REQUEST_MODEL = reqparse.RequestParser()
GETMESSAGE_REQUEST_MODEL.add_argument("User", type = str, required=True, help= "Search with User")
GETMESSAGE_REQUEST_MODEL.add_argument("PalindromeCheck", required=True, help= "Palindrome Check flag",choices=("Yes", "No"), default = "Yes")

DELETEMESSAGE_REQUEST_MODEL = reqparse.RequestParser()
DELETEMESSAGE_REQUEST_MODEL.add_argument("User", action="append", type = str, required=True, help="Enter User")

GETALLMESSAGES_REQUEST_MODEL = reqparse.RequestParser()
GETALLMESSAGES_REQUEST_MODEL.add_argument("Available", required=True, help="Select value from dropdown", choices=("USERS", "MESSAGES", "ALL"), default = "USERS")