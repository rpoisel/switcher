from flask.ext.restful import Resource
from flask.ext.restful.reqparse import RequestParser


class BusConfig(Resource):

    def get(self):
        return {
            'i2c': '1',
            'status': 'online',
            }


class FetchRange(Resource):

    def get(self):
        return {'eins': 'zwo'}


class Report(Resource):

    def __init__(self):
        super(Report, self).__init__()
        self.__mParser = RequestParser()
        self.__mParser.add_argument('success', type=str, required=True)
        self.__mParser.add_argument('message', type=str)
        self.__mParser.add_argument('rangeId', type=int, required=True)

    def get(self):
        lArgs = self.__mParser.parse_args()
        lSuccess = lArgs['success']
        lMessage = lArgs['message']
        lRangeId = lArgs['rangeId']
        return {}


class Progress(Resource):
    def get(self):
        return {
            'value': 5,
            'message': "Not so interesting"
        }


class Reset(Resource):
    def get(self):
        return {}



