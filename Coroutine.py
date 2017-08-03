#!bin/env Python3
#-*-coding:utf-8 -*-
#Filename:Coroutine.py

#The coroutine is better than mutipleline
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...'%n)
        r='200 ok'

def produce(c):
    c.send(None)  #This would make beginning
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...'%n)
        r=c.send(n)
        print('[PRODUCE] Consumer return: %s'%r)
    c.close()

c=consumer()
produce(c)

#asynic
import asyncio
@asyncio.coroutine
def hello():
    print('Hello world!')
    r=yield from asyncio.sleep(1)
    print('Hello world again!')

#get Eventloop
loop=asyncio.get_event_loop()
#excutive coroutine
looprun_until_complete(hello())
loop.close()
"""
#Make tasks to package two different coroutines
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)'%threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello agaio! (%s)'%threading.currentThread())

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

import asyncio
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com',
'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
"""

#practise asynico aiohttp
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text='<h1>hello, %s!</h1>'%request.match_info['name']
    return web.Reponse(body=text.encode('utf-8'))
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
