import requests


def get_cat():
    apis = [
        "https://api.thecatapi.com/v1/images/search",
        "https://aws.random.cat/meow",
        "https://cataas.com/cat?json=true"
    ]

    try:
        r = requests.get(apis[0]).json()
        return r[0]["url"]
    except Exception:
        try:
            r = requests.get(apis[1]).json()
            return r["file"]
        except Exception:
            return "https://cataas.com/cat"
