import requests

url = "http://127.0.0.1:8000/"  # Adjust endpoint if it's not /predict
payload = {
    "YearsAtCompany": 0.1,
    "EmployeeSatisfaction": 2,
    "Position": "Manager",
    "Salary": 5
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:", response.json())
