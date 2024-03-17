from test import BaseTestCase


class UserTest(BaseTestCase):
    # SIGNIN
    def test_signup_existing_user(self):
        user_data = {
            "name": "Roberto1",
            "email": "roberto@gmail.com",
            "password": "Senha123!",
        }
        response = self.client.post("/signup", json=user_data)
        self.assertStatus(response, 400)
        self.assertEqual(
            response.json, {"message": "Email já cadastrado.", "code": 400}
        )

    def test_signup_weak_password(self):
        user_data = {
            "name": "Roberto",
            "email": "roberto2@gmail.com",
            "password": "senha123",
        }
        response = self.client.post("/signup", json=user_data)
        self.assertStatus(response, 400)
        self.assertEqual(response.json, {"message": "Senha fraca", "code": 400})

    def test_signup_success(self):
        user_data = {
            "name": "Roberto",
            "email": "contato.robertoluis@gmail.com",
            "password": "Newpassword1!",
        }
        response = self.client.post("/signup", json=user_data)
        self.assertStatus(response, 201)
        self.assertEqual(
            response.json, {"message": "Usuário cadastrado com sucesso", "code": 201}
        )

    # LOGIN
    def test_login_incorrect_password(self):
        user_data = {"email": "siron@gmail.com", "password": "pASSWORD1!"}
        response = self.client.post("/signin", json=user_data)
        self.assertStatus(response, 401)
        self.assertEqual(response.json, {"message": "Senha incorreta", "code": 400})

    def test_login_user_not_found(self):
        user_data = {"email": "marcone_ribeiro@gmail.com", "password": "Password1!"}

        response = self.client.post("/signin", json=user_data)
        self.assertStatus(response, 401)
        self.assertEqual(
            response.json, {"message": "Usuário não encontrado", "code": 401}
        )

    def test_login_successful(self):
        user_data = {"email": "roberto@gmail.com", "password": "Password1!"}
        response = self.client.post("/signin", json=user_data)
        self.assertStatus(response, 200)
        self.assertEqual(response.json, {"message": "Login bem-sucedido", "code": 200})
