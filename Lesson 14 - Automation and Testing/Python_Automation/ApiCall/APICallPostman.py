# Basic API Requests

import requests
import json

def GET():

    url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

    # # print as dict 
    # response = response.json()
    # for header, value in response.items():
    #     print(header, ':', value)

# did not work
def POST():

    url = "https://postman-echo.com/post"

    payload = 'foo1=bar1&foo2=bar2'

    headers= {}

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

# did not work either, probably needs auth
def PUT():

    url = "https://postman-echo.com/put"

    payload = "This is expected to be sent back as part of response body."
    headers= {}

    response = requests.request("PUT", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

def PATCH():

    url = "https://postman-echo.com/patch"

    payload = "This is expected to be sent back as part of response body."
    headers= {}

    response = requests.request("PATCH", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

def HEADERS():

    url = "https://postman-echo.com/headers"

    payload = {}
    files = {}
    headers = {
    'my-sample-header': 'Lorem ipsum dolor sit amet'
    }

    response = requests.request("GET", url, headers=headers, data = payload, files = files)

    print(response.text.encode('utf8'))


def HEADERS_with_params():

    url = "https://postman-echo.com/headers/response-headers?Content-Type=text/html&test=response_headers"

    payload = "My personal payload"
    files = {}
    headers= {'foo': 'bar1'}

    response = requests.request("GET", url, headers=headers, data = payload, files = files)

    print(response.text.encode('utf8'))


# Basic auth, postman password
def AUTH():

    url = "https://postman-echo.com/basic-auth"

    payload = {"Test attempt" : "response attempt denem"}
    headers = {'Authorization' : 'Basic cG9zdG1hbjpwYXNzd29yZA=='}

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

def RESPONSE():

    url = "https://postman-echo.com/status/200"

    payload = {"name":"denem"}
    files = {}
    headers= {"my-sample-header":"denem-header"}

    response = requests.request("GET", url, headers=headers, data = payload, files = files)

    print(response.text.encode('utf8'))


def POST_POSTMAN():

    url = "http://3.13.86.142:3000/contacts"
    payload = "{\n    \"firstName\": \"Dingo\",\n    \"lastName\": \"Ahiri\",\n    \"email\": \"dingo@software.com\",\n    \"location\": {\n        \"city\": \"Izmir, IZ\",\n        \"country\": \"TR\"\n    },\n    \"employer\": {\n    \t\"jobTitle\": \"Software Tester\",\n    \t\"company\": \"Microsoft\"\n    }\n}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

POST_POSTMAN()