class dota_major():

    def __init__(self):
        pass
		
    def get_teams(self,soup):
        #<div class="teamcard teamcardmix
        teams = []
        teams_data = soup.find_all('div', class_="teamcard teamcardmix toggle-area toggle-area-1")
        for team_data in teams_data:
            data = team_data.find_all('a')
            
            team = data[0].get('title')
            teams.append(team)
        teams = teams[:15]
        return teams

    def get_rankings(self,soup):
        teams = []
        rows = soup.findAll('tr')
        rows = [row for row in rows if len(row)>5]
        indexes = rows[0]
        index_values = []
        for cell in indexes.find_all('th'):
            value = cell.get_text()
            if len(value) < 2:
                try:
                    value = cell.find('a').get('title')
                except AttributeError:
                    value = 'TBD'	
            index_values.append(value.rstrip())
        rows = rows[1:]
        for row in rows:
            team = {}
            cells = row.find_all('td')	
            for i in range(0,len(cells)):
                value = cells[i].find(text=True, recursive=False)
                if value is None:
                    value = cells[i].get_text()
                if value == "99999":
                    team[index_values[i]] = 0
                else:
                    value = value.rstrip()
                    if len(value) > 0:
                        team[index_values[i]] = value
            teams.append(team)		