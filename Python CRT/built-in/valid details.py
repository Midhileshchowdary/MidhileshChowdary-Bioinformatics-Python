## write py program to read name contact number mail id and password make sure thant contact number has 10 gits and mail should have crct structure
#  name@org.com and password should have atlease 3 uppercase 3 lowercase 3splchr and  1 num and passs length should not be less than 10 
name=input("Enter the name :")
number=input("Enter the number")
mail=input("Enter the mail_id :")
password=input("Enter the password :")
u_count=0
s_count=0
spl_char = "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
l_count=0
n_count=0
num='123456789'
if len(number)==10:
  print(number)
else:
  print("Invalid phone number ")
if '@' not in mail or '.' not in mail:
  print("Invalid mail")
if len(password)<10:
  print("Invalid password")
else:
  for ch in password:
    if ch.isupper():
      u_count+=1
    elif ch.islower():
      l_count+=1
    elif ch in spl_char:
      s_count+=1
    elif ch in num:
      n_count+=1

  if u_count<3:
    print("There must be 3 uppercase letters")
  elif l_count<3:
    print("There must be 3 lower letters")
  elif s_count<3:
      print("There must be three spl character")
  elif n_count<1:
      print("There must be one number")
  else:
      print("Password is valid")