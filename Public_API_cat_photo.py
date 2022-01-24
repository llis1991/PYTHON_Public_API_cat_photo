import requests
import json
import webbrowser

params = {
    "breed_id": "sibe",
    "limit": 3
}


r = requests.get("https://api.thecatapi.com/v1/images/search", params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("nieprawidlowy format pliku")
else:
    for photoUrl in content:
        #photoUrl["url"] = newWebsiteToOpen
        webbrowser.open(str(photoUrl["url"]), new=1)
