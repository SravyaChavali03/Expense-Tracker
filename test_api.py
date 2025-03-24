import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/categorize"

# Define multiple test cases
test_cases = [
    {"description": "Pizza Hut"},
    {"description": "Shell Gas Station"},
    {"description": "Netflix Subscription"},
    {"description": "Walmart"},
    {"description": "Uber"},
    {"description": ""},  # Empty description
    {"description": 12345}  # Invalid type
]

# Test each case
for case in test_cases:
    print(f"Testing: {case}")
    response = requests.post(url, json=case)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    print()