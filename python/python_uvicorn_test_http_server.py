import uvicorn

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<html><body>This is a web page.</body></html>']

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
