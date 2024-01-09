from sanic import Sanic
from sanic.response import text

app = Sanic("TestServer")

@app.route("/")
async def root(request):
    return text("This is a web page", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
