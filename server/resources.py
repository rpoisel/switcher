import os

from flask.ext.restful import Resource
from flask.ext.restful.reqparse import RequestParser

from smbus import SMBus


class Busses(Resource):

    def get(self):
        lDevFiles = os.listdir('/dev')
        lI2cDevs = [
            dev.replace('i2c-', '')
            for dev in lDevFiles if dev.find('i2c') == 0
            ]
        lI2cDevs.sort()
        return {
            'i2c': {
                'buses': lI2cDevs,
                #'status': 'online',
                }
            }


class Get(Resource):

    def __init__(self):
        super(Get, self).__init__()
        self.__mParser = RequestParser()
        self.__mParser.add_argument('bus_id', type=str, required=True)
        self.__mParser.add_argument('address', type=str, required=True)
        self.__mParser.add_argument('cmd', type=str)

    def get(self):
        lStatus = "ok"
        lCommand = ""
        lValue = ""
        lArgs = self.__mParser.parse_args()
        lBusId = int(lArgs['bus_id'], 0)
        lBus = SMBus(lBusId)

        lAddress = int(lArgs['address'], 0)
        try:
            if lArgs['cmd'] is None:
                lValue = lBus.read_byte(lAddress)
            else:
                lCommand = int(lArgs['cmd'], 0)
                lValue = lBus.read_byte_data(lAddress, lCommand)
        except IOError, pExc:
            lStatus = "Error reading from bus: " + str(pExc)

        return {
            'bus_id': lBusId,
            'address': lAddress,
            'cmd': lCommand,
            'value': lValue,
            'status': lStatus
            }


class Set(Resource):

    def __init__(self):
        super(Set, self).__init__()
        self.__mParser = RequestParser()
        self.__mParser.add_argument('bus_id', type=str, required=True)
        self.__mParser.add_argument('address', type=str, required=True)
        self.__mParser.add_argument('value', type=str, required=True)
        self.__mParser.add_argument('cmd', type=str)

    def get(self):
        lStatus = 'ok'
        lArgs = self.__mParser.parse_args()
        lBusId = int(lArgs['bus_id'], 0)
        lAddress = int(lArgs['address'], 0)
        lValue = int(lArgs['value'], 0)
        lBus = SMBus(lBusId)

        try:
            if lArgs['cmd'] is None:
                lBus.write_byte(lAddress, lValue)
            else:
                lCommand = int(lArgs['cmd'], 0)
                lBus.write_byte_data(lAddress, lCommand, lValue)
        except IOError, pExc:
            lStatus = "Error writing data: " + str(pExc)

        return {
            'bus_id': lBusId,
            'address': lAddress,
            'cmd': lCommand,
            'value': lValue,
            'status': lStatus
            }


class Dump(Resource):
    def get(self):
        return {
            'value': 5,
            'message': "Not so interesting"
        }


class Detect(Resource):
    def get(self):
        return {}



