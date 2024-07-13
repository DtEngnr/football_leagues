import requests
from config import API_TOKEN, BASE_URL

def test():
    endpoint = '/leagues'
    include = "country"

    
    print("List of Football Leagues:")
    leagues = []
     
    URL = f"{BASE_URL}{endpoint}?api_token={API_TOKEN}&include={include}"
    response = requests.get(url=URL)
    if response.status_code == 200:
        data = response.json()
        for league in data['data']:
            league_info = {
                'name': league['name'],
                'active': league['active'],
                'type': league['type'],
                'sub_type': league['sub_type'],
                'last_played_at': league['last_played_at'],
                'country_id': league['country']['id'],
                'country_name': league['country']['name'],
                'country_iso2': league['country']['iso2']
            }
            leagues.append(league_info)
    else:
        print(f"Failed to retrieve data. Status code:", response.status_code)
    return leagues