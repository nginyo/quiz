print("Welcome to my Computer Quiz!")

playing=input("Do you Want to Play:  ").lower()
if playing!="yes":
    quit()

print("Okay! lets play :)")
score=0

answer=input("What does CPU stand for? ").lower()
if answer=="central processing unit":
    print('correct')
    score+=1
else:
    print("incorrect")

answer=input("What does GPU stand for? ").lower()
if answer=="graphic processing unit":
    print('correct')
    score+=1
else:
    print("incorrect")

answer=input("What does RAM stand for? ").lower()
if answer=="random access memory":
    print('correct')
    score+=1
else:
    print("incorrect")

answer=input("What does PSU stand for? ")
if answer=="power supply":
    print('correct')
    score+=1
else:
    print("incorrect")

print("You got "+str(score)+" questions correct!" )
print(str(score/4*100) +'%.')