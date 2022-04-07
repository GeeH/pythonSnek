from bottle import (post, request, response, route, run, )


@route('/')
def home():
    return {
         "apiversion": "1",
         "author": "GeeH",
         "color": "#F22F46",
         "head": "sand-worm",
         "tail": "coffee",
         "version": "0.0.1"
    }


@post('/start')
def start():
    return {}


@post('/end')
def end():
    return {}


@post('/move')
def move():
    return {
        "move": "down",
        "shout": "Down down down down down down"
    }


if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, debug=True, reloader=True)
