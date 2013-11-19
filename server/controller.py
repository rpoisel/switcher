import sys

from gevent import monkey
#from socketio import socketio_manage
from socketio.server import SocketIOServer
#from werkzeug.wsgi import SharedDataMiddleware

from flask import Flask, render_template  # , request
from flask.ext.restful import Api

#from rangemanager import RangeManager
from resources import Busses, Set, Get, Dump, Detect
#from namespaces import PushNamespace


def main():
    try:
        # init
#        lModel = RangeManager(int(sys.argv[1]), int(sys.argv[2]))

        monkey.patch_all()
        lApp = Flask(__name__)
        lApp.debug = True
        lApi = Api(lApp)
#        FetchRange.sModel = lModel
#        Report.sModel = lModel
#        Progress.sModel = lModel
#        Reset.sModel = lModel
#        PushNamespace.sModel = lModel

        #  routes
        lApp.add_url_rule('/',              'start', start)
#        lApp.add_url_rule('/socket.io/<path:path>', 'socket.io', run_socketio)

        lApi.add_resource(Busses,        '/busses')
        lApi.add_resource(Set,              '/set')
        lApi.add_resource(Get,              '/get')
        lApi.add_resource(Dump,             '/dump')
        lApi.add_resource(Detect,           '/detect')

        # go
#        lApp = SharedDataMiddleware(lApp, {})
        lServer = SocketIOServer(
            ('0.0.0.0', 5000),
            lApp,
            resource="socket.io",
            policy_server=False)
        lServer.serve_forever()
    except IndexError:
        print "Usage: " + sys.argv[0] + \
            " <number of ranges> <timeout per range>"
    except KeyboardInterrupt:
        lServer.stop()


def start():
    return render_template('start.html')


#def run_socketio(path):
#    socketio_manage(request.environ, {'': PushNamespace}, path)
#    # workaround to omit the "ValueError: View function did not
#    #     return a response" exception
#    return render_template('dummy.html')


if __name__ == '__main__':
    main()
