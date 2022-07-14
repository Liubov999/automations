from my_framework.utilities.base_api import BaseAPI


class VehiclesApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.vehicles_url = "/api/vehicles/"

    def get_vehicles(self, vehicles_id):
        return self.get(url=f"{self.vehicles_url}{vehicles_id}")