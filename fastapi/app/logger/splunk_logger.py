import logging
import asyncio


class SplunkLogger:
    def __init__(self, url):
        self.url = url

    async def send_log(self, message, level=logging.INFO):
        data = {
            "host": "your_microservice_name",
            "source": "your_app_name",
            "sourcetype": "microservice_logs",
            "message": message,
            "level": level
        }
        headers = {"Content-Type": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=data, headers=headers) as response:
                if response.status != 200:
                    print(f"Error sending log: {await response.text()}")
