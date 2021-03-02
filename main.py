# pip instal chess.com
import chessdotcom
import discord

class ChessClient():
    def getLeaderboards(self):
        Leaderboards = chessdotcom.get_leaderboards().json
        print(Leaderboards)
        return Leaderboards

    def displayPlayerInfo(self, userinfo):


    def getPlayerInformation(self, username, client):
        PlayerInformation = chessdotcom.get_player_profile(username).json
        print(PlayerInformation)
        return PlayerInformation

ChessClient = ChessClient()

username = "Kaweees"
data = ChessClient.getPlayerInformation(username, client)