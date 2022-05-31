from flask_restplus import Namespace, fields, Resource
from request_models import *
from app_helper import *

def get_message_namespace(app_api):

    message_namespace = Namespace("Message", description = "Message Management Applicaiton like Create, Retrieve and delete Messages")

    ERROR_RESPONSE_MODEL = message_namespace.model('ErrorMessageModel', {
        'message': fields.String(required=True, description='Message for the thrown error.')
    })  

    GETMESSAGE_RESPONSE_MODEL = message_namespace.model('GetMessageResponseModel', {
        'User': fields.String(required=True, description='User of the Person who has posted the messages'),
        'Message': fields.String(required=True, description='Message'),
        'Palindrome': fields.String(required=True, description='Palindrome check')
    })

    ALLMESSAGE_RESPONSE_MODEL = message_namespace.model('ListAllMessagesResponseModel', {
        'Results': fields.Raw(required=True, description='List out all the messages from application'),
        'Count': fields.Integer(required=True, description='Length of Users or Messages')
    })

    @message_namespace.route("/a1/post_messages")
    class PostMessageResource(Resource):
        @message_namespace.doc(description = "Posting User to application")
        @message_namespace.doc(parser=POSTMESSAGE_REQUEST_MODEL)
        @message_namespace.response(500, 'Internal server error',ERROR_RESPONSE_MODEL)
        @message_namespace.response(400, 'Data or Configuration Issue',ERROR_RESPONSE_MODEL)
        def post(self):
            args = POSTMESSAGE_REQUEST_MODEL.parse_args()
            try:
                Postvariables = PostValues.post_variables(args["User"], args["Message"])
                if Postvariables:
                    return "{} details entered successfully".format(args["User"])
            except Exception as err:
                message_namespace.abort(400, str(err))

    @message_namespace.route("/a2/get_messages")
    class GetMessageResource(Resource):
        @message_namespace.doc(description = "Retrieve Message details from application")
        @message_namespace.doc(parser=GETMESSAGE_REQUEST_MODEL)
        @message_namespace.marshal_with(GETMESSAGE_RESPONSE_MODEL, code=200, description="Messages posted successfully")
        @message_namespace.response(500, 'Internal server error',ERROR_RESPONSE_MODEL)
        @message_namespace.response(400, 'Data or Configuration Issue',ERROR_RESPONSE_MODEL)
        def get(self):
            args = GETMESSAGE_REQUEST_MODEL.parse_args()
            user = args["User"]
            palindromecheck = args["PalindromeCheck"]
            try:
                return GetValues.get_request_variables(user, palindromecheck)
            except Exception as err:
                message_namespace.abort(400, str(err))

    @message_namespace.route("/a3/delete_messages")
    class DeleteMessageResource(Resource):
        @message_namespace.doc(description = "Delete Message from application")
        @message_namespace.doc(parser=DELETEMESSAGE_REQUEST_MODEL)
        @message_namespace.response(500, 'Internal server error',ERROR_RESPONSE_MODEL)
        @message_namespace.response(400, 'Data or Configuration Issue',ERROR_RESPONSE_MODEL)
        def delete(self):
            args = DELETEMESSAGE_REQUEST_MODEL.parse_args()            
            try:
                for key in args["User"]:
                    del_redis(key)
                return "{} details deleted successfully".format(args["User"])
            except Exception as err:
                message_namespace.abort(400, str(err))

    @message_namespace.route("/a2/listout_all_messages")
    class GetAllMessageResource(Resource):
        @message_namespace.doc(description = "List all Messages from application")
        @message_namespace.doc(parser=GETALLMESSAGES_REQUEST_MODEL)
        @message_namespace.marshal_with(ALLMESSAGE_RESPONSE_MODEL, code=200, description="Messages posted successfully")
        @message_namespace.response(500, 'Internal server error',ERROR_RESPONSE_MODEL)
        @message_namespace.response(400, 'Data or Configuration Issue',ERROR_RESPONSE_MODEL)
        def get(self):
            args = GETALLMESSAGES_REQUEST_MODEL.parse_args()            
            try:
                return GetAllValues.get_all_variables(args["Available"])
            except Exception as err:
                message_namespace.abort(400, str(err))
                
    return message_namespace