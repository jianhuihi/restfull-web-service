#!/bin/env python
#coding = utf-8

import sys
import tornado.httpserver
import tornado.ioloop
import tornado.web

from test import MainHandler, TestHandler, TradeHandler, TestGetHandler, GoHandler, TestModHandler

def main():
    listen_port =  sys.argv[1]
    application = tornado.web.Application([
        ('/favicon.ico', tornado.web.ErrorHandler, dict(status_code=404)), 
        (r"/", MainHandler),
        (r"/test", TestHandler),
        (r"/trade", TradeHandler),
        (r"/testget/([0-9]+)", TestGetHandler),
        (r"/testget/(\w+)", TestGetHandler),
        (r"/go/(\w+)/(\w+)/(\w+)", GoHandler),
        (r"/testmod/(\w+)", TestModHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(listen_port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()