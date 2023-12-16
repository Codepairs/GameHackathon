from flask import Flask, request
from LoggerClass import Logger
from GameMapClass import GameMap


class Server:
    """
    Server class. Used to send and receive requests from remote GAME server.
    """
    def __init__(self):
        self.game_map = GameMap()
        self._logger = Logger('Server')
        self._flask_app = Flask(__name__)
        # Need to add requests to our server here
        """
        @self._flask_app.route('/bot/turn', methods=["POST"])
        def make_turn():
            current_game_field = request.json.get("game_field")
            server_response = Test.make_algo_move(current_game_field, self._figure, self._opposite_figure())
            self._logger.send_message(f"Запрос {request} был принят! Ответ сервера: {server_response}", "info")
            return {"game_field": server_response}
            """
        """
        @self._flask_app.route('/bot/turn', methods=["POST"])
        def make_turn():
        current_game_field = request.json.get("game_field")
            server_response = Test.make_algo_move(current_game_field, self._figure, self._opposite_figure())
            self._logger.send_message(f"Запрос {request} был принят! Ответ сервера: {server_response}", "info")
            return {"game_field": server_response}
            """

    def scan_request(self):
        """
        Scan map
        :return:
        """
        self._logger.send_message("Сканируем карту!", "info")
        # do scan
        self._logger.send_message("Карта сканирована успешно. Ответ: {такой то такой то}", "info")

    def shoot_request(self):
        """
        Shoot at smb
        :return:
        """
        self._logger.send_message("Выполняем Атаку!", "info")
        # do shot
        self._logger.send_message("Атака прошла успешно. Ответ: {такой то такой то}", "info")

    def run(self):
        self._logger.send_message("Сервер запущен!", "info")
        self._flask_app.run(host='127.0.0.1', port=5000)


