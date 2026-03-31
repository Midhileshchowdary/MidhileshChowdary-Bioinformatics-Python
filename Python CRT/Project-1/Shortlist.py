Job_Roles = [
    'Full Stack Developer', 'Data Engineer', 'Java Developer','Data Analyst', 'HR', 'Data Scientist', 'Team Lead'
]
Can_App = {
    'Jyothi': ['jyothi@gmail.com', 1234567890, 'Data Analyst'],
    'Niharika': ['niharika@mail.com', 9123458908, 'Java Developer'],
    'Nadeem': ['nadeem@gmail.com', 89453256776, 'Data Engineer'],
    'Sravya': ['sravya@gmail.com', 78462672398, ['Full Stack Developer', 'HR']],
    'Harshith': ['harshith@gmail.com', 79124867983, 'Team Lead']
}
Shortlisted_App = {
    'Jagadeesh': ['abc@gmail.com', 68251432876, 'Tech Support'],
    'Shraddha': ['xyz@gmail.com', 2635116747, 'SQL Admin']
}
Completed = {
    'Jyothi': ['jyothi@gmail.com', 1234567890, 'Data Analyst'],
    'Niharika': ['niharika@mail.com', 9123458908, 'Java Developer']
}
def View_Details():
    print("\nApplied Candidates:")
    print("--------------------------")
    for name, details in Can_App.items():
        print(f"{name}: {details}")
    print("\nShortlisted Candidates:")
    print("--------------------------")
    for name, details in Shortlisted_App.items():
        print(f"{name}: {details}")
    print("\nFinalized Candidates (Level 3 Qualified):")
    print("--------------------------")
    for name, details in Completed.items():
        print(f"{name}: {details}")
    print("\nAvailable Job Roles:")
    print("--------------------------")
    for role in Job_Roles:
        print(role)
def Shortlist_Profile():
    Name = input("Enter the Candidate Name to evaluate: ")
    if Name in Can_App:
        decision = input("Enter 'Yes' if the profile meets criteria, else 'No': ")
        if decision.lower() == "yes":
            Shortlisted_App[Name] = Can_App[Name]
            print(f" {Name}'s profile has been shortlisted.")
        else:
            print(f"{Name}'s profile has not been shortlisted.")
    else:
        print("Candidate not found in applications list.")
def Schedule_Call():
    Name = input("Enter the Candidate Name to schedule interview: ")
    if Name in Shortlisted_App:
        print(f"Interview Scheduled: {Name}, please be available for Level-1 interview.")
    else:
        print(f" {Name} is not in the shortlisted candidates.")
def Update_Status():
    Name = input("Enter the Candidate Name: ")
    Status = input("Enter 'Yes' if qualified in Level-1 interview, else 'No': ")
    if Status.lower() == "yes":
        print(f" {Name} has qualified Level-1 Interview. Proceeding to next round.")
    else:
        print(f"{Name} has not qualified in Level-1 Interview.")
def Send_OfferLetter():
    Name = input("Enter the Candidate Name: ")
    Status = input("Enter 'Yes' if the candidate has cleared all 3 levels of interview, else 'No': ")
    if Status.lower() == "yes":
        Completed[Name] = Shortlisted_App.get(Name, Can_App.get(Name, ['Unknown', 0, 'Unknown']))
        print(f"Congratulations {Name}, your offer letter will be sent shortly.")
    else:
        print(f"{Name} is not eligible for an offer letter at this stage.")

while True:
    print("\n------------------------------------------------------")
    print("Operations - Vignan Software Solutions")
    print("------------------------------------------------------")
    print("1. View Candidate Applications, Shortlists, and Job Roles")
    print("2. Shortlist a Candidate Profile")
    print("3. Schedule Interview for Shortlisted Candidates")
    print("4. Update Level-1 Interview Status")
    print("5. Send Offer Letter to Final Candidates")
    print("6. Exit")
    print("------------------------------------------------------")
    try:
        Choice = int(input("Enter Your Choice (1-6): "))
        if Choice == 1:
            View_Details()
        elif Choice == 2:
            Shortlist_Profile()
        elif Choice == 3:
            Schedule_Call()
        elif Choice == 4:
            Update_Status()
        elif Choice == 5:
            Send_OfferLetter()
        elif Choice == 6:
            print(" Exiting HR Operations. Have a great day!")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 6.")
    except ValueError:
        print("Please enter a valid numeric input.")
