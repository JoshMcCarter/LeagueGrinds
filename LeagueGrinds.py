import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from riotwatcher import RiotWatcher
from GetDevKey import getDevKey
from Match import Match

class LeagueGrind(object):
	
	def __init__(self, spreadSheetName):
		# Establish Google Drive Connection
		json_key = json.load(open('credentials.json'))
		scope = ['https://spreadsheets.google.com/feeds']
		credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
		gc = gspread.authorize(credentials)
		self.spreadsheet = gc.open("League Grinds")
		
		#Establish Riot API Connection
		self.riotWatcher = RiotWatcher(getDevKey())		
		
	def update_player(self, playerName):
		player = self.riotWatcher.get_summoner(name=playerName)
		playerID = player['id']
		match_list = self.riotWatcher.get_match_list(playerID,region='na')
		matches = [Match(playerID,self.riotWatcher,f) for f in match_list['matches'] if f['season']=='SEASON2016']
		

LeagueGrind("League Grinds").update_player("toolbox97")

