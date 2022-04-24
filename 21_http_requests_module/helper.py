import requests

url = "https://icanhazdadjoke.com/search"


def get_jokes(term):
    resp = requests.get(url, headers={
                        "accept": "application/json"}, params={"term": term, "limit": 30}).json()

    return resp


if __name__ == '__main__':
    get_jokes("cat")
