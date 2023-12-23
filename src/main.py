import time
from pprint import pprint
from GameAPIClass import GameAPI


if __name__ == '__main__':
    server = GameAPI()
    server.deathmatch_registration_request()
    server.leave_request()

