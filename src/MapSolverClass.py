from GameMapClass import GameMap
from AlgoClass import Algo

class MapSolver:
    """
    MapSolver class. Make calculations to interact with map.
    """

    def __init__(self, string_map: str = 'Default MapSolver'):
        self._current_map = GameMap(string_map)
        self._map_after_turn = None

    def set_map(self, game_map: GameMap):
        self._current_map = game_map

    def set_map_after_turn(self, game_map: GameMap):
        self._map_after_turn = game_map

    def get_map(self) -> GameMap:
        return self._current_map

    def get_map_before_turn(self) -> GameMap:
        return self._current_map

    def get_map_after_turn(self) -> GameMap:
        return self._map_after_turn

    def scan_map(self) -> GameMap:
        """
        Algo for scan map
        :return: new map after turn
        """
        result: GameMap = GameMap("поле после скана")
        self._map_after_turn = result
        return self._map_after_turn

    def shoot_at(self, position) -> GameMap:
        """
        Algo for shoot at enemy
        :return: new map after turn
        """
        result: GameMap = GameMap("поле после выстрела")
        self._map_after_turn = result
        return self._map_after_turn

    def calculate_smth(self) -> GameMap:
        """
        Algo for Hackathon
        :return: new map after turn
        """
        result: GameMap = GameMap("поле после хода")
        self._map_after_turn = result
        return self._map_after_turn

