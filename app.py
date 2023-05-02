import requests
import json
from decouple import config
import pprint

#set globals for api, summoner name, and first half of api url calls
api_key = config('RIOT_API_KEY')
params  = {"api_key": api_key}
summoner_name = config('SUMMONER_NAME')
league_url = "https://na1.api.riotgames.com"



##Obtain summoner encrypted id key
url =f"{league_url}/lol/summoner/v4/summoners/by-name/{summoner_name}"
lol_na1_api = "https://na1.api.riotgames.com"
response = requests.get(url, params=params).json()
encryptedSummonerId = response["id"]
print(encryptedSummonerId)

# url = f"{league_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}"
# response = requests.get(url,params=params).json()
# pprint.pprint(response)


# url = f"{league_url}/lol/league-exp/v4/entries/RANKED_SOLO_5x5/SILVER/II"  #can probably use for data for game type,ranke, and level
# response = requests.get(url,params=params).json()

# pprint.pprint(response)


# url = f"{league_url}/lol/league/v4/entries/by-summoner/{encryptedSummonerId}"
# response = requests.get(url, params=params).json()
# pprint.pprint(response)


url = f"{league_url}/lol/summoner/v4/summoners/{encryptedSummonerId}"
response = requests.get(url,params=params).json()
##pprint.pprint(response)
encryptedPUUID = response['puuid']
puuid = encryptedPUUID


url = f"{league_url}/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}"
response = requests.get(url, params=params).json()
##pprint.pprint(response)


url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20"
response = requests.get(url, params=params).json()








# pprint.pprint(len(response["info"]["frames"]))


# pprint.pprint(len(response["info"]["frames"][1]))

# pprint.pprint(response["info"]["frames"][1]["timestamp"])

# for x in response["info"]["frames"][1]:
#     print(x)

# pprint.pprint(response["info"]["frames"][1]["events"][1])



list_keys = []
for x in response["info"]["frames"][5]["events"][:]:
    for keys in x.keys():
        list_keys.append(keys)
print(list(set(list_keys)))