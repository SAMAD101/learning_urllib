import urllib3

# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()

# Sending a GET request and getting back response as HTTPResponse object.
resp = http.request("GET", "https://httpbin.org/robots.txt")

print(resp.data)