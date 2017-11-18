import requests

#get method
#r = requests.get("https://www.pivotaltracker.com")
#print("Values \n", r.text)
#print("CONTENT \n", r.content)
#print("CODE \n", r.status_code)

# post considerar un payload
#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.post("https://www.pivotaltracker.com", data=payload)
#print(r.text)

#headers
url = 'https://www.pivotaltracker.com/services/v5/me'
headers = {'X-TrackerToken': '2a6118f239fa9083cf56206082f3eefe'}
response = requests.get(url,headers=headers )
print("Values \n", response.text)
print("CONTENT \n", response.content)
print("CODE \n", response.status_code)
print("Json \n", response.json())

def request_get(method, headers=None):
    print("reqquest1")


def perform_request(method, endpoint, body=None, headers=none):
    if (method == "GET"):
        requests.get(endpoint, headers)
    elif(method == "POST"):
        requests.get(endpoint,payLoad=body, headers=headers )

def add_header(host):


