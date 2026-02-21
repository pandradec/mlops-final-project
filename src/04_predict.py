import json
import requests

my_dict = {
    "dataframe_split": {
        "columns": ["experience" , "test_score" , "interview_score"],
        "data": [[1,34,2] , [2,36,4]]
    }
}

payload = json.dumps(my_dict)
response = requests.post(
    url=f"http://localhost:1234/invocations",
    data=payload,
    headers={"Content-Type": "application/json"},
)
print(response.json())