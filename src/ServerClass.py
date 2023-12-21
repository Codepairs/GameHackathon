from flask import Flask, request
from LoggerClass import Logger
from MapSolverClass import MapSolver
import requests


class Server:
    """
    Server class. Used to send and receive requests from remote GAME server.
    """

    def __init__(self):
        self._solver = MapSolver("Current Map")
        self._team_information = ''
        self._dats_black_url = ''
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
        try:
            self._logger.send_message("Сканируем карту!", "info")
            self._solver.scan_map()
            scan_response = requests.get(url=self._dats_black_url, data=self._team_information)
            self._logger.send_message(f"Карта сканирована успешно. Ответ: {scan_response}", "info")
        except:
            self._logger.send_message("Ошибка при сканировании карты!", "error")

    def shoot_request(self, position):
        """
        Shoot at smb
        :return:
        """
        try:
            self._logger.send_message("Выполняем Атаку!", "info")
            shoot_data = self._solver.shoot_at(position)
            shoot_response = requests.post(url=self._dats_black_url, data=shoot_data)
            self._logger.send_message(f"Атака прошла успешно. Ответ: {shoot_response}", "info")
        except:
            self._logger.send_message("Ошибка при выполнении атаки!", "error")

    def run(self):
        self._logger.send_message("Сервер запущен!", "info")
        self._flask_app.run(host='127.0.0.1', port=5000)
