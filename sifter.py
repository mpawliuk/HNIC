import datetime

# Open file
infile = open("2017_2018_NHL_Schedule.csv")
# https://leftwinglock.com/files/2017_2018_NHL_Schedule.csv

teams = [
'Calgary Flames',"Edmonton Oilers",'Montreal Canadiens', 'Ottawa Senators', 'Winnipeg Jets', 'Toronto Maple Leafs', 'Vancouver Canucks',
'Boston Bruins', 'San Jose Sharks', 'Minnesota Wild','Chicago Blackhawks', 'Arizona Coyotes', 'Anaheim Ducks', 
'Philadelphia Flyers', 'Los Angeles Kings', 'Columbus Blue Jackets', 'Florida Panthers', 'Tampa Bay Lightning', 'Vegas Golden Knights', 'Dallas Stars', 
'New York Rangers', 'Detroit Red Wings', 'Colorado Avalanche', 'New Jersey Devils', 'Buffalo Sabres','New York Islanders', 
'Nashville Predators', 'Pittsburgh Penguins', 'St. Louis Blues', 'Carolina Hurricanes', 'Washington Capitals'
]

subreddit = {
'Calgary Flames': '[](/r/calgaryflames)',
"Edmonton Oilers": '[](/r/edmontonoilers)',
'Montreal Canadiens': '[](/r/habs)', 
'Ottawa Senators': '[](/r/ottawasenators)', 
'Winnipeg Jets': '[](/r/winnipegjets)', 
'Toronto Maple Leafs': '[](/r/leafs)', 
'Vancouver Canucks': '[](/r/canucks)',
'Boston Bruins': '[](/r/bostonbruins)', 
'San Jose Sharks': '[](/r/sanjosesharks)', 
'Minnesota Wild': '[](/r/wildhockey)',
'Chicago Blackhawks': '[](/r/hawks)', 
'Arizona Coyotes': '[](/r/coyotes)', 
'Anaheim Ducks': '[](/r/anaheimducks)', 
'Philadelphia Flyers': '[](/r/flyers)', 
'Los Angeles Kings': '[](/r/losangeleskings)', 
'Columbus Blue Jackets': '[](/r/bluejackets)', 
'Florida Panthers': '[](/r/floridapanthers)', 
'Tampa Bay Lightning': '[](/r/tampabaylightning)', 
'Vegas Golden Knights': '[](/r/goldenknights)', 
'Dallas Stars': '[](/r/dallasstars)', 
'New York Rangers': '[](/r/rangers)', 
'Detroit Red Wings': '[](/r/detroitredwings)', 
'Colorado Avalanche': '[](/r/coloradoavalanche)', 
'New Jersey Devils': '[](/r/devils)', 
'Buffalo Sabres': '[](/r/sabres)',
'New York Islanders': '[](/r/newyorkislanders)', 
'Nashville Predators': '[](/r/predators)', 
'Pittsburgh Penguins': '[](/r/penguins)', 
'St. Louis Blues': '[](/r/stlouisblues)', 
'Carolina Hurricanes': '[](/r/canes)',
'Washington Capitals': '[](/r/caps)'
}

can_teams = teams[:7]
data = []
sample_game = ['2017-10-04', '7:00 PM', 'Toronto Maple Leafs', 'Winnipeg Jets']

HNIC_data = {team:[] for team in can_teams }

def on_sat(game_date):
	"""Is this date a saturday?"""
	return datetime.date(int(game_date[0:4]), int(game_date[5:7]), int(game_date[8:10])).weekday() == 5

def is_HNIC(game_info):
	"""See if the game is a 7pm or 10pm Sat game."""
	#print game_info
	# Is there a Canadian team?
	if not game_info[2] in can_teams and not game_info[3] in can_teams:
		return False
	# Is it at the right time?
	if not game_info[1] in ('7:00 PM', '10:00 PM'):
		return False
	# Is it on a Saturday?
	if not on_sat(game_info[0]):
		return False
	
	# Now we update the teams
	if game_info[2] in can_teams:
		HNIC_data[game_info[2]].append(game_info[3])
	if game_info[3] in can_teams:
		HNIC_data[game_info[3]].append(game_info[2])
	
	return None

# Edit data
for row in infile:
	data.append(row.split(','))
	data[-1][-1] = data[-1][-1][:-1] # Remove \n
	is_HNIC(data[-1])

for team in HNIC_data.keys():
	games = ''
	for opp in HNIC_data[team]:
		games += subreddit[opp] + ' '
	print team, '|', len(HNIC_data[team]), '|', games
