from aiohttp import web


class HelloWorldView(web.View):
    async def get(self) -> web.Response:
        return web.Response(text="Hello World!")


class Application(web.Application):
    def __init__(self):
        super().__init__()
        self.add_routes()

    def add_routes(self):
        self.router.add_view('/helloworld', HelloWorldView)

    def run(self):
        web.run_app(self, host="129.107.208.214", port=8000)
        # web.run_app(self, port=8000)


application = Application()
if __name__ == '__main__':
    application.run()

# Restart the server and enter the following url: ‘http://localhost:8000/helloworld’
# in your browser. Voila, you should now see a “Hello World!” text on the page, sweet!
