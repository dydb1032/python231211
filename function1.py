# function1.py

def times(a=10,b=20):
    return a*b

print(times())
print(times(5))

print(times(5,6))

def connectURI(server, port):
    strURL = 'http://' + server + ':' + port
    return strURL

print(connectURI('multi.com', "80"))
print(connectURI(port = '8080', server = "multi.com"))