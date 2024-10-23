import requests

url = 'http://educem.net/moodle'
# Get Web Page
response = requests.get(url)
# Print HTML Code
print(response.text)