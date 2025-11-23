import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1"
PARAMS_PARIS = "/current.json?key={key}&q={city}"


def get_weather() -> None:
    key = os.environ["API_KEY"]
    url = BASE_URL + PARAMS_PARIS.format(key=key, city="Paris")
    res = requests.get(url)
    print(res.json())


if __name__ == "__main__":
    get_weather()
