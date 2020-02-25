import discord

def parse(name, team_details, embed=False):

    if embed == False:
        team_name = name

        msg = "Takim: " + name + "\n"
        print(msg)
        msg += "Pos 1: " + team_details['team_roster'][0]['ID'] + " (" + team_details['team_roster'][0]['Name']  + ")" +"\n"
        msg += "Pos 2: " + team_details['team_roster'][1]['ID'] + " (" + team_details['team_roster'][1]['Name']  + ")" +"\n"
        msg += "Pos 3: " + team_details['team_roster'][2]['ID'] + " (" + team_details['team_roster'][2]['Name']  + ")" +"\n"
        msg += "Pos 4: " + team_details['team_roster'][3]['ID'] + " (" + team_details['team_roster'][3]['Name']  + ")" +"\n"
        msg += "Pos 5: " + team_details['team_roster'][4]['ID'] + " (" + team_details['team_roster'][4]['Name']  + ")" +"\n"

    else:
        #embed = discord.Embed(title=msg, description=msg2, color=0x00ff00)
        msg = "Takim: " + name + "\n"
        #embed.add_field(title=msg)
        msg2  = "Pos 1: " + team_details['team_roster'][0]['ID'] + " (" + team_details['team_roster'][0]['Name']  + ")" +"\n"
        msg2 += "Pos 2: " + team_details['team_roster'][1]['ID'] + " (" + team_details['team_roster'][1]['Name']  + ")" +"\n"
        msg2 += "Pos 3: " + team_details['team_roster'][2]['ID'] + " (" + team_details['team_roster'][2]['Name']  + ")" +"\n"
        msg2 += "Pos 4: " + team_details['team_roster'][3]['ID'] + " (" + team_details['team_roster'][3]['Name']  + ")" +"\n"
        msg2 += "Pos 5: " + team_details['team_roster'][4]['ID'] + " (" + team_details['team_roster'][4]['Name']  + ")" +"\n"
        print(msg, msg2)
        embed = discord.Embed(title=msg, description=msg2, color=0x00ff00)
        msg = msg + msg2
    return embed

