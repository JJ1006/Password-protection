n=3
p="Joshi@1*2"
print("\nPlease enter the password of your account to gain access : ")

while n>=0:

    password=input()

    if password==p:
        print("\nCONGRATULATIONS, ACCESS GRANTED\n")

    if password!=p:
        n=n-1
        print(f"\nPassword is incorrect. You have {n} turns left to try")
        print("\nPlease try again\n")
        
    if n==0 and password!=p:
        print("\nYOUR ACCOUNT HAS BEEN BLOCKED!!!\n")
        break