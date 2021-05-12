from src.Servicies import get_map_constructor


class game():

    def __init__(self):
        self.countries = get_map_constructor().get_countries()
        self.players = {}

