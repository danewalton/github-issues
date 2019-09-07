
import requests
import json
import yaml
from github import Github

url = Github("")

repo = url.get_repo("Azure/azure-iot-sdk-c")

issues = repo.get_issues(state='open')

for issue in issues:
    print(issue)
