import urllib3

resp = urllib3.request("GET", "https://www.google.com")
print(resp.status)
print(resp.data)