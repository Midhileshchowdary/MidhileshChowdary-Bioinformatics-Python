'''
you have participated in your college level coding fest which was there for 6 days
write a py prog to give the final report which includes
1) Activities for the day including timeline
2) Number of teams/participants of the day
3) Project name
4) technologies used
5) PPT demonstration given
6) Winner of day
7) Runner up of the day
8) Best Performer of the day
9) Host of the program for that day
'''
class Coding_fest():
    def __init__(self,Day,Activities,NTeams,ProName,TechUsed,Ppt,Winner,Runner,BPerformer,Host):
        pass
        self.Day=Day
        self.Activities=Activities
        self.NTeams=NTeams
        self.ProName=ProName
        self.TechUsed=TechUsed
        self.Ppt=Ppt
        self.Winner=Winner
        self.Runner=Runner
        self.BPerformer=BPerformer
        self.Host=Host
def Report(self):
    print(f"Day : {self.Day}")
    print(f"Activities : {self.Activities}")
    print(f"Number of teams/participants of the day : {self.NTeams}")
    print(f"Project name : {self.ProName}")
    print(f"Technologies used : {self.TechUsed}")
    print(f"PPT demonstration : {self.Ppt}")
    print(f"Winner of day : {self.Winner}")
    print(f"Runner up of the day {self.Day} : {self.Runner}")
    print(f"Best Performer for the day {self.Day} : {self.BPerformer}")
    print(f"Host of the program for the day {self.Day}: {self.Host}")
    print("-------------------")
# Creating 6 Report objects
R1 = Coding_fest("1", "Opening Ceremony, Team Introductions", 10, "Project A, Project B", "Python, JavaScript", "Yes", "Team Alpha", "Team Beta", "Alice", "John")
R2 = Coding_fest("2", "Workshops on Python and Web Development", 12, "Project C, Project D", "Python, HTML/CSS", "Yes", "Team Gamma", "Team Delta", "Bob", "Sarah")
R3 = Coding_fest("3", "Hackathon Begins, Team Collaboration", 15, "Project E, Project F", "Python, Flask", "Yes", "Team Epsilon", "Team Zeta", "Charlie", "Emma")
R4 = Coding_fest("4", "Midway Checkpoint, Team Presentations", 14, "Project G, Project H", "Python, Django", "Yes", "Team Eta", "Team Theta", "David", "Olivia")
R5 = Coding_fest("5", "Final Coding Sessions, Debugging", 13, "Project I, Project J", "Python, React", "Yes", "Team Iota", "Team Kappa", "Eve", "Liam")
R6 = Coding_fest("6", "Closing Ceremony, Awards Distribution", 16, "Project L, Project M", "Python, Node.js", "Yes", "Team Lambda", "Team Mu", "Frank", "Sophia")
Report(R1)
Report(R2)
Report(R3)
Report(R4)
Report(R5)
Report(R6)