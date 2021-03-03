# pip instal chess.com
import chessdotcom
import discord

import json
from urllib.request import urlopen
import requests

import time

class ChessClient():
    def getLeaderboards(self):
        Leaderboards = chessdotcom.get_leaderboards().json
        # print(Leaderboards)
        return Leaderboards

    def getPlayerStats(self, username):
        PlayerStats = chessdotcom.get_player_stats(username).json
        # print(PlayerStats)
        return PlayerStats

    def getPlayerInformation(self, username):
        PlayerInformation = chessdotcom.get_player_profile(username).json
        # print(PlayerInformation)
        return PlayerInformation

class Chessplayer():
    def __init__(self, playerStats):
        self.url = playerStats['url']
        self.username = playerStats['username']
        self.followers = playerStats['followers']
        self.embedname = f"{self.username}'s Info and Stats"
        self.color = 0x7fa650
        self.country = playerStats['country']

        self.lastOnline = playerStats['last_online']
        self.lastOnline = time.gmtime(self.lastOnline)
        self.lastOnline = time.strftime("%a %x", self.lastOnline)

        self.dateJoined = playerStats['joined']
        self.dateJoined = time.gmtime(self.dateJoined)
        self.dateJoined = time.strftime("%a %x", self.dateJoined)

        try:
            self.avatarurl = playerStats['avatar']
        except:
            self.avatarurl = "https://kaweees.github.io/assets/images/default-profile-pic.png"

    def updatePlayerStats(self, playerStatsData):
        try: 
            self.chessTacticsBest = ((playerStatsData['tactics']['highest']['rating'] + playerStatsData['tactics']['lowest']['rating']) / 2)
        except:
            self.chessTacticsBest = "N/A"
        try: 
            self.chessLessonsBest = ((playerStatsData['lessons']['highest']['rating'] + playerStatsData['lessons']['lowest']['rating']) / 2)
        except:
            self.chessLessonsBest = "N/A"
        try: 
            self.chessPuzzleRushBest = playerStatsData['puzzle_rush']['best']['score']
        except:
            self.chessPuzzleRushBest = "N/A"
        try: 
            self.chessRapidBest = playerStatsData['chess_rapid']['last']['rating']
        except:
            self.chessRapidBest = "N/A"
        try: 
            self.chessRapidBest = playerStatsData['chess_rapid']['last']['rating']
        except:
            self.chessRapidBest = "N/A"
        try: 
            self.chessBulletBest = playerStatsData['chess_bullet']['last']['rating']
        except:
            self.chessBulletBest = "N/A"
        try: 
            self.chessBlitzBest = playerStatsData['chess_blitz']['last']['rating']
        except:
            self.chessBlitzBest = "N/A"
        try: 
            self.chessDailyBest = playerStatsData['chess_daily']['last']['rating']
        except:
            self.chessDailyBest = "N/A"
        
        # self.chessLessonsBest = playerStatsData['lessons']['last']['rating']
        # self.chessPuzzleRushBest = playerStatsData['puzzle_rush']['last']['rating']

    def getCountry(self, site):
        r = requests.get(site)
        text = r.text
        countryISOData = json.loads(text)
        name = countryISOData['name']
        emoji  = f""":flag_{site.replace("https://api.chess.com/pub/country/", '').lower()}:"""
        specialString = f"{name} {emoji}"
        return specialString
    