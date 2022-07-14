
class Film:
    def __init__(self, director, producer, release_date):
        self.director = director
        self.producer = producer
        self.release_date = release_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__



