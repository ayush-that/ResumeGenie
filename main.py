import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

linkedin_profile_url = "https://www.linkedin.com/in/ayush-that/"
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

params = {
    "url": linkedin_profile_url,
    "fallback_to_cache": "on-error",
    "use_cache": "if-present",
    "skills": "include",
    "inferred_salary": "include",
    "extra": "include",
    "personal_email": "include",
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
}

response = requests.get(api_endpoint, params=params, headers=headers)

if response.status_code == 200:
    profile_data = response.json()

    with open("profile_data.json", "w") as json_file:
        json.dump(profile_data, json_file, indent=4)
else:
    print(f"Error: {response.status_code}")
