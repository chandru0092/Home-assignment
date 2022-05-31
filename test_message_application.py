###################### Unit Testing ############################

import unittest
import start_app

User = "qlik"
Message = "Information Technology"

class TestMessage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        start_app.app.testing = True
        cls.app = start_app.app.test_client()

    def test_a1_post_messages(self):
        response = self.app.post(
                "Message/a1/post_messages?User={}&Message={}".format(User, Message))
        assert response.status_code == 200

    def test_a2_get_messages(self):
        response = self.app.get(
                "Message/a2/get_messages?User={}&PalindromeCheck=Yes".format(User))
        assert response.status_code == 200

    def test_a2_list_messages(self):
        response = self.app.get(
                "Message/a2/listout_all_messages?Available=USERS")
        assert response.status_code == 200

    def test_a3_delete_messages(self):
        response = self.app.delete(
                "/Message/a3/delete_messages?User={}".format(User))
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()