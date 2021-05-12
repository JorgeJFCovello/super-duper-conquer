import requests


def get_map_constructor():
    if hasattr(get_map_constructor, 'instance'):
        return get_map_constructor.instance
    else:
        inst = get_map_constructor.instance = MapConstructor()
        return inst


class MapConstructor:

    def get_countries(self):
        url = "https://restcountries.eu/rest/v2/all"

        return requests.request("GET", url)


if __name__ == '__main__':
    print(get_map_constructor().get_countries().json()[0])
