import unittest
from manage import app


class DivisionComputationTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_divide_success(self):
        response = self.app.post("/api/divide", json={"dividend": 10, "divisor": 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 5.0})

    def test_divide_zero_divisor(self):
        response = self.app.post("/api/divide", json={"dividend": 10, "divisor": 0})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Division by zero is not allowed", response.json["error"])

    def test_divide_invalid_input(self):
        response = self.app.post("/api/divide", json={"dividend": "ten", "divisor": 2})
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Both dividend and divisor must be integers", response.json["error"]
        )
