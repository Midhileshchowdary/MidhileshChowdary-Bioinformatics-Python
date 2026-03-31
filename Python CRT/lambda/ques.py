'''
write py prog to write lamda function which prints good students if branch is bioinformatics else bad students
'''
branch=lambda x:print("Good Students") if(x=="Bioinformatics") else print("Bad Students")
branch("Bioinformatics")
branch("Biotechnology")