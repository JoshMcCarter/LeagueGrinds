class Match(object):
	def __init__(self, playerID, riotWatcher, data):
		self.lane = data['lane']
		self.championID = data['champion']
		self.matchID = data['matchId']
		self.timestamp = data['timestamp']
		
		matchdata = riotWatcher.get_match(self.matchID);
		
		# Win / Loss
		# Kills
		# Assists
		# Deaths
		
		for f in matchdata:
			print f
		assert(False)
		
		
	def __str__(self):
		return self.data.__str__()