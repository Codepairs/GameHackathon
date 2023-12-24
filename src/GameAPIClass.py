import config
from LoggerClass import Logger
from pprint import pprint
from json import dumps
import requests


class GameAPI:
    """
    GameAPI class. Used to send and receive requests from remote GAME coordinator.
    """

    def __init__(self):
        self._url = 'https://datsblack.datsteam.dev'
        self._token = config.token
        self._ships = []
        self._logger = Logger('GameAPI')

    def deathmatch_registration_request(self) -> bool:
        """
        '/api/deathMatch/registration' Register team
        :return: result of request
        """
        api_extension = '/api/deathMatch/registration'
        headers = {
            'X-API-Key': self._token
        }
        self._logger.send_message("Отправляем запрос на регистрацию на DeathMatch", "info")
        registration_response = requests.post(url=self._url + api_extension, headers=headers)

        if registration_response.ok:
            errors = registration_response.json()["errors"]
            result = registration_response.json()["success"]
            self._logger.send_message(f"Регистрация прошла успешно! Ошибки: {errors}", "info")
            return result
        else:
            self._logger.send_message("Ошибка при регистрации!", "error")
            return False

    def battleroyal_registration_request(self) -> bool:
        """
        '/api/battleRoyal/registration' Register team in battle royal
        :return: result of request
        """
        api_extension = '/api/royalBattle/registration'
        headers = {
            'X-API-Key': self._token
        }
        self._logger.send_message("Отправляем запрос на регистрацию на BattleRoyal", "info")
        registration_response = requests.post(url=self._url + api_extension, headers=headers)
        if registration_response.ok:
            errors = registration_response.json()["errors"]
            result = registration_response.json()["success"]
            self._logger.send_message(f"Регистрация прошла успешно! Ошибки: {errors}", "info")
            return result

        else:
            self._logger.send_message("Ошибка при регистрации! Плохой ответ...", "error")
            return False

    def leave_request(self) -> bool:
        """
        '/api/deathMatch/exitBattle' Exit from DeathMatch and RoyalBattle
        :return: result of request
        """
        api_extension = '/api/deathMatch/exitBattle'
        headers = {
            'X-API-Key': self._token
        }
        self._logger.send_message("Отправляем запрос на выход из DeathMatch", "info")
        leave_response = requests.post(url=self._url + api_extension, headers=headers)
        if leave_response.ok:
            errors = leave_response.json()["errors"]
            result = leave_response.json()["success"]
            self._logger.send_message(f"Выход из DeathMatch прошел успешно! Ошибки: {errors}", "info")
            return result
        else:
            self._logger.send_message("Ошибка при выходе! Плохой ответ...", "error")
            return False

    def map_request(self) -> bool:
        """
        '/api/map' Scan whole map
        :return: result of request
        """
        api_extension = '/api/map'
        headers = {
            'X-API-Key': self._token
        }
        self._logger.send_message("Отправляем запрос на сканирование DeathMatch", "info")
        scan_response = requests.get(url=self._url + api_extension, headers=headers)
        if scan_response.ok:
            map_url = scan_response.json()["mapUrl"]
            errors = scan_response.json()["errors"]
            self._logger.send_message(f"Сканирование DeathMatch прошел успешно! Ошибки: {errors}", "info")
            return map_url
        else:
            self._logger.send_message("Ошибка при сканировании DeathMatch! Плохой ответ...", "error")
            return False

    def scan_around_ships_requests(self) -> tuple | bool:
        """
        '/api/scan' Scan around ally_ships
        :return: my_ships, enemy_ships, zone, tick
        """
        api_extension = '/api/scan'
        headers = {
            'X-API-Key': self._token
        }
        self._logger.send_message("Отправляем запрос на сканирование вокруг кораблей", "info")
        scan_response = requests.get(url=self._url + api_extension, headers=headers)
        if scan_response.ok:
            print(scan_response)
            print(scan_response.json())
            scan = scan_response.json()["scan"]

            my_ships = scan["myShips"]
            enemy_ships = scan["enemyShips"]
            try:
                zone = scan["zone"]
            except KeyError:
                zone = None
            tick = scan["tick"]
            self._logger.send_message("Сканирование вокруг кораблей прошло успешно!", "info")
            return my_ships, enemy_ships, zone, tick
        else:
            self._logger.send_message("Ошибка при сканировании DeathMatch! Плохой ответ...", "error")
            return False

    def scan_at_point_request(self, x: int, y: int):
        """
        '/api/longScan' Scan at x, y
        :param x: coordinate x
        :param y: coordinate y
        :return: success
        """

        api_extension = '/api/longScan'
        headers = {
            'X-API-Key': self._token
        }

        data = dumps({
            'x': x,
            'y': y
        })
        self._logger.send_message("Отправляем запрос на сканирование DeathMatch", "info")
        scan_response = requests.post(url=self._url + api_extension, headers=headers, data=data)
        if scan_response.ok:
            success = scan_response.json()["success"]
            tick = scan_response.json()["tick"]
            errors = scan_response.json()["errors"]
            self._logger.send_message(f"Сканирование DeathMatch прошло успешно!Ошибки: {errors}", "info")
            return success
        else:
            self._logger.send_message("Ошибка при сканировании DeathMatch! Плохой ответ...", "error")
            return False

    def create_changes(self, id, changeSpeed, rotate, x, y):
        if x is None or y is None:
            return {
                "id": id,
                "changeSpeed": changeSpeed,
                "rotate": rotate
            }
        else:
            return {
                "id": id,
                "changeSpeed": changeSpeed,
                "rotate": rotate,
                "cannonShoot": {
                    "x": x,
                    "y": y
                }
            }

    def ships_control_request(self, ships: list):
        """
        '/api/shipCommand' Control ally_ships
        "ally_ships": [
        {
        "id": 34,
        "changeSpeed": 3,
        "rotate": -90,
        "cannonShoot": {
            "x": 30,
            "y": 34
                }
            }
        ]
        :param ships: list of ally_ships
        :return: result of request
        """
        api_extension = '/api/shipCommand'
        headers = {
            'X-API-Key': self._token
        }
        data = dumps({
            'ships': ships
        })
        self._logger.send_message("Отправляем запрос на контроль кораблей", "info")
        control_response = requests.post(url=self._url + api_extension, headers=headers, data=data)
        if control_response.ok:
            errors = control_response.json()["errors"]
            result = control_response.json()["success"]
            tick = control_response.json()["tick"]
            self._logger.send_message(f"Контроль кораблей прошел успешно! Ошибки: {errors}", "info")
            return result
        else:
            self._logger.send_message("Ошибка при контроле кораблей! Плохой ответ...", "error")
            return False
