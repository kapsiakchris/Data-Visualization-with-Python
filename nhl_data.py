import requests

url = 'https://api.nhle.com/stats/rest/en/leaders/skaters/goals?cayenneExp=season=20222023 and gameType=3'

r = requests.get(url)
print(f"Status code: {r.status_code}")

response = r.json()

for key in sorted(response.keys()):
    print(key)

print(f"Total values returned: {response['total']}")

data_dicts = response['data']

for player in data_dicts:
    print(f"{player['player']['fullName']} has {player['goals']} goals.")