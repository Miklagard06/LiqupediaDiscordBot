# Work with Python 3.6
import discord

TOKEN = 'NjgxNzAwODQ0OTgyMzcwMzM0.XlSS_g.5idFeXgNwPdhwOQdmFdRtAkXWmI'
client = discord.Client()

import dota
import team_parser

dota_obj = dota.dota("appname")
players = dota_obj.get_players()

#player_details = dota_obj.get_player_info('Miracle-',True)
#team_details = dota_obj.get_team_info('Team Liquid',False)

ORG_TEAMS = ['OG','Team Secret', 'Team Liquid']
TEAMS= ['!' + team.lower() for team in ORG_TEAMS]

print(TEAMS)
print(tuple(TEAMS))
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global TEAMS
    global ORG_TEAMS

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!help') or message.content.startswith('!komut'):
        msg  = '!hello' + ' '
        msg += '!pozisyon' + ' '
        msg += '!embed' + ' '
        msg += '!id' + ' '
        msg += '!player' + ' '
        msg += '!(TAKIM_ADI)' + ' '
        msg += '!major' + ' '
        msg = msg.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!pozisyon'):
        msg  = 'Pos 1: Hard Carry, takimin farm yukunu tutan oyuncusu\n'
        msg += 'Pos 2: Mid, takimin farm yukunu tutan oyuncusu\n'
        msg += 'Pos 3: Offlane, takimin farm yukunu tutan oyuncusu\n'
        msg += 'Pos 4: Soft Support, takimin farm yukunu tutan oyuncusu\n'
        msg += 'Pos 5: Hard Support, takimin farm yukunu tutan oyuncusu\n'

        msg = msg.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!takim'):
        msg = "Takimlar: " + " ".join(ORG_TEAMS) + "\n"
        msg += "Detayli bilgi icin !TAKIM_ADI" 
        await message.channel.send(msg.format(message))

    if message.content.startswith('!embed'):
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!id'):
        id = message.channel
        #print(id)
        msg = 'Channel ID: ' + str(id) + ' {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!player'):
        msg = 'Miracle {0.author.mention}'.format(message)
        #player_details = dota_obj.get_player_info('Miracle-',True)
        #print(player_details)
        await message.channel.send(msg)

    if message.content.lower().startswith(tuple(TEAMS)):

        myteam = ""
        for i, team in enumerate(TEAMS):
            if message.content.lower().startswith(team):
                myteam = ORG_TEAMS[i]
        #msg = 'Your team is ' + myteam  + ' {0.author.mention}'.format(message)
        team_details = dota_obj.get_team_info(myteam)
        
        embed = team_parser.parse(myteam, team_details, embed=True)
        #print(team_details)
        #msg = msg + ' {0.author.mention}'.format(message)
        await message.channel.send(embed=embed)

    if message.content.startswith('!major'):
         
        major = dota_obj.get_major_details()
        #msg = 'Major {0.author.mention}'.format(message)
        print(major['teams'])
        ORG_TEAMS = major['teams']
        TEAMS= ['!' + team.lower() for team in ORG_TEAMS]
        msg = " ".join(ORG_TEAMS) + " Majore katilacak" + ' {0.author.mention}'.format(message) 
        await message.channel.send(msg)

client.run(TOKEN)

#681700844982370334
#Second 681742378565894145