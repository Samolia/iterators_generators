import json


class LinksCreator:

    def __init__(self, path):
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
        self.url = 'https://en.wikipedia.org/wiki/'
        self.iter_countries = (country['name']['official'] for country in data)

    def __iter__(self):
        return self

    def __next__(self):
        country = next(self.iter_countries)
        country_links = f'{self.url}{country.replace(" ", "_")}'
        return f'"{country}" <==> "{country_links}"'
