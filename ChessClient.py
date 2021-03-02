# pip instal chess.com
import chessdotcom
import discord

class ChessClient():
    def getLeaderboards(self):
        Leaderboards = chessdotcom.get_leaderboards().json
        print(Leaderboards)
        return Leaderboards

    def displayPlayerInfo(self, userinfo):
        pass

    def getPlayerInformation(self, username):
            PlayerInformation = chessdotcom.get_player_profile(username).json
            print(PlayerInformation)
            return PlayerInformation

class Chessplayer():
    def __init__(self, playerStats):
        self.url = playerStats['url']
        self.username = playerStats['username']
        self.avatarurl = playerStats['avatar']
        self.followers = playerStats['followers']
        self.embedname = f"{self.username}'s Info and Stats"
        self.color = 0x7fa650