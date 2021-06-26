from aiohttp import web


class Application(web.Application):
    def __init__(self):
        super().__init__()

    def run(self):
        return web.run_app(self, host="129.107.208.214", port=8000)


application = Application()

if __name__ == '__main__':
    application.run()


"""
Output:

(hm) wxf@CBD-007:~/grpc_prj/medium$ /home/wxf/anaconda3/envs/hm/bin/python /home/wxf/grpc_prj/medium/aiohttp-grpc-ebs/web_app/application.py
======== Running on http://129.107.208.214:8000 ========
(Press CTRL+C to quit)
"""
