###########################
# players.py
#
# class to automate managing
# scores and picks.  Intended
# document template looks like the following:
#
###########################
from pymongo import MongoClient

class Players:
    def __init__(self):
        client = MongoClient()
        self.db = client.maynard
        players = self.db.players
        self.d_p = {}
        for p in players.find():
            self.d_p[p['name']] = p

    def new_player(self, str_last):
        self.last = str_last
        body = {'name': self.name, 'last': self.last, 'picks': {}, 'score': 0}
        self.d_p[body['name']] =  body
        self.db.players.insert_one(body)

    def make_picks(self, name, week, the_picks):
        #picks is a list of tuples -> (name of team, bool - is_prime, bool - is_lock)
        if name not in self.d_p:
            print "Error, player not in database"
            return
        picks = self.d_p[name]['picks']
        picks[str(week)] = {}
        for i in xrange(len(the_picks)):
            picks[str(week)][str(i)] = {'name': the_picks[i][0], 'is_prime': the_picks[i][1]==1, 'is_lock': the_picks[i][2]==1}

        #self.d_p[name]['picks'] = picks
        result = self.db.players.update_one(
            {"name":name},
            {
                "$set":{
                    "picks": picks
                }
            }
        )

    def get_all(self):
        return self.d_p

    def get_player(self, name):
        return self.d_p[name]
