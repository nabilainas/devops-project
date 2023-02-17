import unittest
import requests

class TestEmployeeAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:8090/api/v1/employees'
        self.headers = {'Content-Type': 'application/json'}
        self.employee = {
            "firstName": "nabil",
            "lastName": "ainas",
            "emailId": "nabil@ainas",
        }
        res = requests.get(self.base_url)
        self.id_test = len(res.json())

    def test_1_get_employees(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_2_get_employee_by_id(self):
        response = requests.get(f'{self.base_url}/{self.id_test}')
        self.assertEqual(response.status_code, 200)
    
    def test_1_post_employee(self):
        response = requests.post(self.base_url, headers=self.headers, json=self.employee)
        self.assertEqual(response.status_code, 201)

    def test_4_put_employee_by_id(self):
        updated_employee = {
            "firstName": "nabileboss",
            "lastName": "ainas",
            "emailId": "leboss@ainas",
        }
        response = requests.put(f'{self.base_url}/{self.id_test}', json=updated_employee)
        self.assertEqual(response.status_code, 204)
    
    def test_5_delete_employee_by_id(self):
        response = requests.delete(f'{self.base_url}/{self.id_test}')
        print("hello")
        print("hello")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
