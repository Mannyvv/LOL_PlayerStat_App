import inspect
import pprint
# pylint: disable=E1101


class PlayerStats():
    def __init__(self, player_data) -> None:
        """recieves player json data and initiates variables with json dictionary keys and value (i.e Rank, Tier, ID, wins,losses, ets)"""
        for  key, value in  player_data[0].items():
            setattr(self,key, value)
        #TODO - Add PUIID attribute 
        print("Player Tier: " , self.tier)
        print("Player Rank: ", self.rank)

    def player_info(self):
        pprint.pprint(inspect.getmembers(self))
    

class Match():
    def __init__(self,match_data) -> None:
        pass

        

class Champion():
    def __init__(self) -> None:
        pass

