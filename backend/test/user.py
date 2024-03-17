from test import BaseTestCase


class UserTest(BaseTestCase):
    def test_get_user_by_id(self):
        response = self.client.get("/user/1")
        self.assert200(response)
        self.assertEqual(response.json, {"name": "Gabriel"})
