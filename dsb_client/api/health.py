from swagger_client.api.health_api import HealthApi

class Health:
    def __init__(self, health_api:HealthApi) -> None:
        self.health = health_api

    async def check(self):
        thread = self.health.health_controller_check(async_req=True)
        return thread.get()
