from redis_helper import *

class PostValues:
    """
        POst Values to application in key and values format    
    """
    def post_variables(user, messages):
        if len(user) == len(messages):
            for i in range(0, len(user)):                   
                set_redis(user[i], messages[i])
        else:
            for i in range(0, len(user)):                   
                set_redis(user[i], messages[0])
        return True

class GetValues:
    """
        Retrieve Values from application and check Palindrome or not
    """
    def get_request_variables(user, palindromecheck):
        palindrome = "Palindrome check is not requested"
        message = get_redis(user)
        if palindromecheck.upper() == "YES":
            if message.lower() == message[::-1].lower():
                palindrome = "Message is a palindrome"
            else:
                palindrome = "Message is not a palindrome"
        return GetValues(user, message, palindrome)

    def __init__(self, user, message, palindrome):
        self.User = user
        self.Message = message
        self.Palindrome = palindrome

class GetAllValues:
    """
        Retrieve all the Values from application
    """
    def get_all_variables(retrievevalue):
        #results = None
        count = 0
        results = get_all_keys(retrievevalue)
        count = len(results)
        return GetAllValues(results, count)

    def __init__(self, results, count):
        self.Results = results
        self.Count = count
