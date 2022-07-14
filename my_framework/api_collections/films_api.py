from my_framework.utilities.base_api import BaseAPI


class FilmsApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.films_url = "/api/films/"

    def get_films(self, episode_id):
        return self.get(url=f"{self.films_url}{episode_id}")
