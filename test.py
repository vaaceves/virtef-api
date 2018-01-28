import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/api'
    response = requests.get(url)

print(response)