'''
Design a backend system to manage multiplayer game tournaments, Players register play natches, and earn points, The system should rank them, handle tiebreakers, and simulate knockout rounds.
Features:
Player registration with unique usernames.
Match results entry and automatic point updates.
Leaderboard sorted by score. 
Sinulate knockout using recursion.Export match history.
Tech Stack:
Core Python (Lists, Dictionaries, Tuples)00P (Player, Match, Tournament classes)Recursion (Knockout simulation)
Sorting Algorithms (Leaderboard)
File Handling (History logs)
Optional: pandas for final score export
'''
import random
class Player:
    def __init__(self,username):
        self.username=username
        self.score=0
class Match:
    def __init__(self,player1,player2,winner):
        self.player1=player1
        self.player2=player2
        self.winner=winner
class Tournament:
    def __init__(self):
        self.player={}
        self.matches=[]
    def register_player(self,username):
        if username in self.player:
            print(f"{username} already registered.")
        else:
            self.player[username]=Player(username)
            print(f"{username} registered")
    def add_match_results(self,username1,username2,winner_name):
        if winner_name not in [username1,username2]:
            print("Winner must be one of the two players")
            return
        if username1 not in self.player or username2 not in self.player:
            print("Player(s) not registered.")
            return
        winner=self.player[winner_name]
        winner.score+=3
        match=Match(username1,username2,winner_name)
        self.matches.append(match)
        print(f"{username1} vs {username2} => {winner_name}")
    def display_leaderboard(self):
        sorted_players=sorted(self.player.values(),key=lambda p: (-p.score,p.username))
        for i, player in enumerate(sorted_players,1):
            print(f"{i}, {player.username} - {player.score}")
    def simulate_knockout(self,player_list=None,round_num=1):
        if player_list is None:
            player_list=list(self.player.keys())
            if len(player_list)%2!=0:
                print("Even number of players required.")
                return
        winners=[]
        for i in range(0,len(player_list),2):
            p1=player_list[i]
            p2=player_list[i+1]
            winner=random.choice([p1,p2])
            print(f"{p1} vs {p2} => {winner}")
            self.add_match_results(p1,p2,winner)
            winners.append(winner)
        if len(winners)==1:
            print(f"Champion : {winners[0]}")
        else:
            self.simulate_knockout(winners,round_num+1)
    def export_history(self,filename="match_history.txt"):
        with open(filename, "w") as f:
            for match in self.matches:
                f.write(f"{match.player1} vs {match.player2} => {match.winner}\n")
        print(f"History exported to {filename}")
t=Tournament()
t.register_player("Alice")
t.register_player("Bob")
t.register_player("charlie")
t.register_player("Diana")
t.add_match_results("Alice","Bob","Alice")
t.add_match_results("Charlie","Diana","Charlie")
t.display_leaderboard()
t.simulate_knockout()
t.export_history()