import requests
import json
from decouple import config
import pprint
from lol_classes import PlayerStats
import time

#set globals for api, summoner name, and first half of api url calls

params  = {"api_key": config('RIOT_API_KEY')}
summoner_name = config('SUMMONER_NAME')
region = "na1"
league_url = f"https://{region}.api.riotgames.com"
continent = "americas"
league_url_continent =f"https://{continent}.api.riotgames.com"


 
def player_id_info_summonername(summoner_name : str):
    """Calls LOL API to obtain Summoner ID and PUUID
    Parameter: Summoner Name
    Returns Encrypted Summoner ID and PUUID
    """
    url =f"{league_url}/lol/summoner/v4/summoners/by-name/{summoner_name}"
    player_ids_response = requests.get(url, params=params).json()
    encrypted_summonerid = player_ids_response["id"]
    encrypted_puuid = player_ids_response["puuid"]
    return encrypted_summonerid,encrypted_puuid

def player_id_info_puuid(encrypted_puuid : str):
    """Calls LOL API to obtain Summoner ID
    Parameter: PUUID
    Returns Encrypted Summoner ID
    """
    url =f"{league_url}/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}"
    player_puuids_response = requests.get(url, params=params).json()
    encrypted_summonerid = player_puuids_response["id"]
    return encrypted_summonerid

def player_stats_info(encrypted_summonerid : str):
    url = f"{league_url}/lol/league/v4/entries/by-summoner/{encrypted_summonerid}"
    player_stats_response = requests.get(url, params=params).json()
    return player_stats_response


def player_last20_games(encrypted_PUUID : str):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{encrypted_PUUID}/ids?start=0&count=20"
    last_20_games_response = requests.get(url, params=params).json()
    return last_20_games_response

# p_id,p_puuid = player_id_info(summoner_name=summoner_name)
# last_20 = player_last20_games(p_puuid)
# print(last_20)


def load_champions():
    list_of_champions_response = requests.get("http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion.json").json()
    with open('json_files/champion_list.json', 'w', encoding='utf-8') as file:
        json.dump(list_of_champions_response, file, ensure_ascii=False, indent=4)

def get_champion_info(champion_name : str):
        champion_selected = requests.get(f"http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion/{champion_name}.json").json()
        pprint.pprint(champion_selected['data'][champion_name].keys())
        with open('json_files/champion.json', 'w', encoding='utf-8') as file:
            json.dump(champion_selected, file, ensure_ascii=False, indent=4)

#TODO: Obtain ranked solo 5x5 games only. You are pulling all que types with
#       def player_stats_info():

def get_match_summary(match_id : str):
    if type(match_id) != str:
         return print("Argument must be of type string")
    url = f"{league_url_continent}/lol/match/v5/matches/{match_id}"
    match_summary = requests.get(url,params=params).json()
    with open(f'json_files/{match_id}_match_summary.json', 'w', encoding='utf-8') as file:
         json.dump(match_summary, file, ensure_ascii=False,indent=4)
    return match_summary

match_summ = get_match_summary('NA1_4664438761')

# print(match_summ.keys())
# pprint.pprint(match_summ['metadata'].keys())
# print(type(match_summ['metadata']['participants']))

for participant_puuid in match_summ['metadata']['participants']:
     player_id_info = player_id_info_puuid(participant_puuid)
     time.sleep(1)
     pprint.pprint(player_stats_info(player_id_info))
     print('\n\n')
     








def get_match_timeline(match_id):
     url = f"{league_url}/lol/match/v5/matches/{match_id}/timeline"
     match_timeline = requests.get(url,params=params).json()











# pprint.pprint(len(response["info"]["frames"]))


# pprint.pprint(len(response["info"]["frames"][1]))

# pprint.pprint(response["info"]["frames"][1]["timestamp"])

# for x in response["info"]["frames"][1]:
#     print(x)

# pprint.pprint(response["info"]["frames"][1]["events"][1])





