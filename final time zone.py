import time
class person:
    def __init__(self, idnum,name,tz):

     self.idnum= idnum
     self.name= name
     self.tz=tz

#ename= str(input("enter name"))
#pid= int(input("enter id num"))




p1= person(1,"bob", -5)
p2= person(2,"mike",+2)

def menue():
    global choice 
   
    print("**************************************")
    print("*1. display all users                *")
    print("*2. add new user                     *")
    print("*3. display all time zone            *")
    print("*4. save users                       *")
    print("*5. quit                             *")
    print("**************************************")
    choice = input("enter option 1-5")
    return choice

def alluser():
   print("all user(s)")
   for i in range (len(people)):
      print(people[i].name)


def new_user():
   addid = int(input("enter you id: "))
   addname= input("enetr name: ")
  
   time_zone= int(input("enter your time zone: "))
   return person(addid, addname, time_zone)




def alltz():
    global timenow
    timenow= time.strftime("%H:%M:%S", time.localtime)
    print("current time: ", timenow)


def save_user():
    with open('users.txt', 'w') as file:
        for person in people:
            file.write(F"id:{person.idnum},name:{person.name},time zone{person.tz}")




people =[]

people.append(p1)
people.append(p2)

#main
running = True
while running == True:
   choice=menue()
   if (choice =="1"):
      alluser()
   if (choice == "2"):
      people.append(new_user())
   
   
   if (choice==4):
      save_user()
      print("SAVED")
    
   if (choice=="5"):
      running = False

print("Thanks for yousing the programme")

#for x in range (len(people)):
  #print("Id:",people[x].idnum)
   #print("name:",people[x].name)
  # print("zone:",people[x].tz)

