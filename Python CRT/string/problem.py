'''
write py program to read mail id as input from the user and print user name and organization name based on mail.id (name@orgname.com)
'''
Mail=input(" Enter the mail id in format (name@orgname.com):")
List=Mail.split('@')
print(List)
print(f"Username : {List[0]}")
org=List[1]
List=org.split('.')
print(f"organization : {List[0]}")