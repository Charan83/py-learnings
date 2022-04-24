#   requests module
#       - install requests : python3 -m pip install requests
#
#


import requests

# example : request, simple get
resp = requests.get("https://api.github.com/events")
print(f"resp : {resp}")
print(f"resp.headers : {resp.headers}")
print(f"resp.ok : {resp.ok}")
print(f"resp.status_code : {resp.status_code}")
# print(f"resp.text : {resp.text}")

# example : request with headers
dad_joke_url = "https://icanhazdadjoke.com/"
dad_joke_resp = requests.get(dad_joke_url, headers={
                             "Accept": "application/json"})
print(f"dad_joke_resp.text : {dad_joke_resp.text}")  # text format
print(f"dad_joke_resp.json() : {dad_joke_resp.json()}")  # dictionary format
data = dad_joke_resp.json()
print(f"data.get('joke') : {data.get('joke')}")

# example : request with query strings
qs_url = "https://icanhazdadjoke.com/search"
qs_term = input("enter the search term : ")
qs_resp = requests.get(
    qs_url, headers={"Accept": "application/json"}, params={"term": qs_term, "limit": 2}).json()
print(f"qs_resp : {qs_resp}")
jokes_list = qs_resp.get("results")
print(f"jokes_list : {[joke['joke'] for joke in jokes_list]}")
