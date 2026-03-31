'''
You are attending a skill develepoment trainining for 15 days on python Programming Language
TASK:-
Write py prog to give the detailed report of 15 days Python training which includes
    1) Day
    2) Topic
    3) Efficiency(Rate of efficiency and grip on topic learnt on a scale of 5)
    4) Number of assignment questions solved
    5) Number of Hackerrank questions solved
    6)Ratings achieved on  Hackerank for that particular day
    7) Certifications completed(include name of certificate
    8) Duration of class
    9) Rate the session on scale of 5
         1- being worst
         2- being bad
         3- being average 
         4- being good
         5- being best
'''
class SkillDevop:
    def __init__(self,Day,Topic,Efficiency,AssNo,HackNo,HackRate,Certification,Duration,SessionRate):
        pass
        self.Day=Day
        self.Topic=Topic
        self.Efficiency=Efficiency
        self.AssNo=AssNo
        self.HackNo=HackNo
        self.HackRate=HackRate
        self.Certification=Certification
        self.Duration=Duration
        self.SessionRate=SessionRate
def Report(self):
    print (f"Report of day {self.Day}")
    print (f"Topic of the day : {self.Topic}")
    print (f"Efficiency(1-5) : {self.Efficiency}")
    print (f"Assignment questions solved : {self.AssNo}")
    print (f"Hackerrank questions solved : {self.HackNo}")
    print (f"Ratings achieved on  Hackerank on {self.Day} : {self.HackRate}")
    print (f"Certifications completed(include name of certificate) : {self.Certification}")
    print (f"Duration of class : {self.Duration}")
    print("-------------------------------------------")
    if self.SessionRate==1:
        print (f"Rate the session on scale of 5 : {self.SessionRate} - being worst ")
    elif self.SessionRate==2:
        print (f"Rate the session on scale of 5 : {self.SessionRate} - being bad ")
    elif self.SessionRate==3:
        print (f"Rate the session on scale of 5 : {self.SessionRate} - being average ")
    elif self.SessionRate==4:
        print (f"Rate the session on scale of 5 : {self.SessionRate} - being good ")
    else: 
        print (f"Rate the session on scale of 5 : {self.SessionRate} - being best ")
D1=SkillDevop(1,"Basics",4,21,5,"1-Star",2,"3 hours",1)
D2=SkillDevop(2,"Introduction",4,10,5,"2-Star",2,"3 hours",2)
D3=SkillDevop(3,"loops",4,11,5,"2-Star",2,"3 hours",3)
D4=SkillDevop(4,"conditions",4,20,5,"2-Star",2,"3 hours",4)
D5=SkillDevop(5,"lists",4,5,5,"3-Star",2,"3 hours",4)
D6=SkillDevop(6,"strings",4,7,5,"3-Star",2,"3 hours",3)
D7=SkillDevop(7,"tuples",4,8,5,"3-Star",2,"3 hours",2)
D8=SkillDevop(8,"sets",4,18,5,"3-Star",2,"3 hours",1)
D9=SkillDevop(9,"Dictionary",4,13,5,"3-Star",2,"3 hours",2)
D10=SkillDevop(10,"bool",4,16,5,"1-Star",2,"3 hours",3)
D11=SkillDevop(11,"oops",4,9,5,"1-Star",2,"3 hours",4)
D12=SkillDevop(12,"lambda",4,19,5,"1-Star",2,"3 hours",4)
D13=SkillDevop(13,"Built-in",4,20,5,"1-Star",2,"3 hours",3)
D14=SkillDevop(14,"class,object",4,2,5,"1-Star",2,"3 hours",4)
D15=SkillDevop(15,"Projects",4,6,5,"1-Star",2,"6 hours",5)
Report(D1)
Report(D2)
Report(D3)
Report(D4)
Report(D5)
Report(D6)
Report(D7)
Report(D8)
Report(D9)
Report(D10)
Report(D11)
Report(D12)
Report(D13)
Report(D14)
Report(D15)