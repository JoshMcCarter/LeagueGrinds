class Match(object):
	def __init__(self, playerID, riotWatcher, data):
		self.lane = data['lane']
		self.championID = data['champion']
		self.matchID = data['matchId']
		self.timestamp = data['timestamp']
		self.playerID = playerID
		
		matchdata = riotWatcher.get_match(self.matchID);
		for player in matchdata['participantIdentities']:
			if player['player']['summonerId'] == playerID:
				participantID = player['participantId']
				break
		else:
			assert(False)
				
		self.kills   = matchdata['participants'][participantID-1]['stats']['kills']
		self.assists = matchdata['participants'][participantID-1]['stats']['assists']
		self.deaths  = matchdata['participants'][participantID-1]['stats']['deaths']		
		
		print self
		
	def __str__(self):
		output = "========= Printing Match Object =========\n"
		output+= "Player ID = " + str(self.playerID) +    "\n"
		output+= "Match  ID = " + str(self.matchID)  +    "\n"
		output+= "Champ  ID = " + str(self.championID) +  "\n"
		output+= "TimeStamp = " + str(self.timestamp) +   "\n"
		output+= "Kills     = " + str(self.kills) +       "\n"
		output+= "Deaths    = " + str(self.deaths) +      "\n"
		output+= "Assists   = " + str(self.assists) +     "\n"
		output += "======== End Printing for Match ========\n"
		return output