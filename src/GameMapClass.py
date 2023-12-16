class GameMap:
    """
    GameMap class. Make calculations to interact with map.
    """

    def __init__(self, string_map: str = 'Default GameMap'):
        self._string_map = string_map

    def set_map(self, string_map: str):
        self._string_map = string_map

    def get_sting_map(self) -> str:
        return self._string_map

    def calculate_smth(self):
        """
        Main Algo for Hackathon
        :return:
        """
        pass
