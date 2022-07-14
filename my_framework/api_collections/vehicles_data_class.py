class Vehicles:
    def __init__(self, name, model, max_atmosphering_speed):
        self.name = name
        self.model = model
        self.max_atmosphering_speed = max_atmosphering_speed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
