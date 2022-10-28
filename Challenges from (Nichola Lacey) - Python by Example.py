# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#005
Firstnum=int(input("Enter one number: "))
Secondnum=int(input("Enter another number: "))
answer= Firstnum + Secondnum
print("The answer is", answer)

#008
bill= int(input("How much is the bill? "))
diners= int(input("How many people dined at the table? "))
each= bill//diners
print("Each person should pay", each, "$.")

# 009
days= int(input("Please enter a number od days: "))
hours= days*24
minutes= hours*60
seconds= minutes*60
print("The number of days you entered are:" ) 
print(hours, "in hours")
print(minutes, "in minutes")
print(seconds, "in seconds")

# 011
Firstnum= int(input("Please enter a number over a 100: "))
Secondnum= int(input("Please enter a number under 10: "))
Result = Firstnum//Secondnum
print(Firstnum, "goes into", Secondnum, Result, "times.")

#012 (Modified)
num1=input("Please enter a number: ")
num2=input("Please enter another number: ")
if num1>num2:
    print(num2, num1)
elif num1==num2:
    print("Please enter different numbers.")
else:
    print(num1, num2)

#013
num1= int(input("Please enter a number under 20: "))
if num1 >= 20:
    print("The number you have entered is too high.")
else:
    print("Thank You .")
    
#014
num=int(input("Please enter a number between 10 and 20: "))
if num>10 and num<20:
    print("Thank you.")
else:
    print("Incorrect answer.")
    
#015 (Modified)
col=input("Please enter your favourite colour: ")
if col=="red" or col=="RED" or col=="Red":
    print("Red is my favourite colour too !")
else:
    print(col, "is okay, but i prefer red.")
   
#016
text1=input("Is it rining at the moment? ")
text1=str.lower(text1)
if text1=="yes":
    text2=input("Is it windy? ")
    text2=str.lower(text2)
    if text2=="yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")

#017
age=input("Please enter your age: ")
if age>=18:
        print("You can vote.")
elif age==17:
        print("You can learn to drive.")
elif age==16:
        print("You can buy a lottery ticket")
elif age<16:
        print("You can go Trick - or - Treating.")
        
#018 (Modified)
num=int(input("Please enter a number betweem 10 and 20: "))
if num<10:
    print("Too low.")
elif num>=10 and num<=20:
    print("Correct.")
else:
    print("Too high.")

#019 (Modified)
num=input("Please enter one of these numbers, 1,2 or 3: ")
if num=="1":
    print("Nicely Done.")
elif num=="2":
    print("Well Done.")
elif num=="3":
    print("Jollygood.")
else:
    print("Error.")
    
#020
firstname=input("Please enter your first name: ")
length=len(firstname)
print(length)
 
#021
firstname=input("Please enter your first name: ")
surname=input("Please enter your surname: ")
wholename= firstname + " " + surname
print(wholename)
length=(len(wholename))
print(length)

#022
firstname=input("Please enter your firstname in lower case: ")
surname=input("Please enter your surname in lower case: ")
firstname=firstname.title()
surname.title()
wwholename= firstname + " " + surname
print(wholename)

#024
word=input("Please enter a word of your choosing: ")
word=word.upper() 
print(word)
  
#025
firstname=input("Please enter your firstname: ")
length=len(firstname)
if length<5:
    surname=input("Please enter your surname: ")
    wholename=firstname + surname
    wholename=wholename.upper()
    print(wholename)
#Μπορώ επίσης να γράψω: print(firstname.upper())
elif length>=5:
#Μπορώ απλά να γράψω: else
    firstname=firstname.lower()
    print(firstname)
#Μπορώ επίσης να γράψω: print(firstname.lower())
    
#027
#Δεν χρειαζεται 'import math' στο συγκεκριμένο πρόγραμμα.
num=float(input("Please enter a number with lots of decimal places: "))
print(num*2)

#029
import math
num=int(input("Please enter an integer that is over 500: "))
answer=math.sqrt(num)
print(round(answer, 2))

#031
import math
rad=int(input("Please enter the radius of a circle: "))
area=math.pi*(rad**2)
print(area)

#032
import math
radius=int(input("Please enter the radius of the cylinder: "))
depth=int(input("Please enter the depth of the cylinder: "))
area=math.pi*(radius**2)
volume=area*depth
print(round(volume, 3))

#033
num1=int(input("Please enter a number: "))
num2=int(input("Please enter another number: "))
ans1=num1//num2
ans2=num1%num2
print(num1, "divided by", num2, "is", ans1, "with", ans2, "remaining.")

#034
import math
print("1) Square")
print("2) Triangle")
print()
selection=int(input("Please enter a number: "))
if selection==1:
    length=int(input("Please enter the legth of the squaere's side: "))
    area1=length**2
    print("The chosen square has an area of", area1) 
elif selection==2:
    base=int(input("Please enter the base of the triangle: "))
    height=int(input("Please enter the height of the triangle: "))
    area2=base*height
    print("The chosen triangle has an area of", area2)
else:
    print("Error.")
    
#035
users_full_name=input("Please enter your full name: ")
for i in range(0,3) :
    print(users_full_name)
    
#036
full_name=input("Please enetr your full name: ")
num_repeat=int(input("Please enter trhe number of times you want to have your name displayed: "))
for i in range(num_repeat):
    print(full_name)
 
#037
full_name=input("Please enter your full name: ")
for i in full_name :
    print(i)
 
#038 (Modified)
first_name=input("Please enter your first name: ")
first_name=first_name.title()
last_name=input("Please enter your last name: ")
last_name=last_name.title()
full_name= first_name + " " + last_name
num_repeat=int(input("Please enter the number of times you would like to have your name displayed: "))
for i in range(0,num_repeat):
    for i in full_name:
        print (i)
    print("\n")    

#040
num=int(input("Please enter a number that is below 50: "))
for i in range(50, num-1, -1):
    print(i)

#41
name=input("Please enter your name: ")
number=int(input("Please enter a number: "))
if number<10:
    for i in range(0, number+1):
        print(name)
else:
    for i in range (0, 4):
        print("Too high")
        
#042 (Modified)
total=0
for i in range(0,5):
    num=int(input("Please enter a number: "))
    question=input("Would you like to add this number to your total?(Answer this question with yes or no): ")
    print(question)
    question=question.title()
    if question== "Yes":
        total=total+num
#ΕΊΝΑΙ ΠΕΡΙΤΤΕΣ ΟΙ ΓΡΑΜΜΕΣ 255 & 256    
    elif question== "No":
        total=total
print (total)

#043
direction=input("Which way do you want to count, up or down?: ")
direction=direction.title()
if direction=="Up":
    top_num=int(input("Please enter the top number: "))
    for i in range(0, top_num): 
        print(i)
elif direction=="Down":
    num=int(input("Please enter a number: "))
    for i in range(num, -1, -1):
        print(i)
else:
    print("Error")      
  
#044 (Modified)
invitees=int(input("Please enter the number of you people you want to invite to your party: "))
if invitees<=10:
    print("Please enter the invitees names on by one.")
    for i in range(0, invitees):
     name=input("Please enter an invitee's name: ")
     print(name + " " + "has been invited")
else:
    print("Too many people.")     
       
    
#045
total=0
while total<=50:
    num=int(input("Please enter a number: "))
    total=total+num
    print("The total is ", total)

#046
num=0
while num<=5:
    num=int(input("Please enter a number: "))
print("The last number you entered was", num)

#047
num1=int(input("Please enter a number: "))
total=num1
question="Yes"
while question=="Yes":
    num2=int(input("Please enter another number: "))
    question=input("Would you like to add another number? (Answer this question with yes or no): ")
    question=question.title()
    total=total + num2
print("Your total is", total )


#048
count=0
question="Yes"
while question=="Yes":
    invitee=input("Enter the name of the person you would like to invite to your party: ")
    invitee=invitee.title()
    question=input("Would you like to invite anyone else? (Answer this question with yes or no): ")
    question=question.title()
    count=count + 1
    print(invitee ,"  has been invited.")
print("You have invited ", count, " people in total.\n\t Enjoy your party !")

#049
print("Try and guess the number I am thinking of.")
compnum=50
count=0
count1=0
count2=0
guess=int(input("Please enter a number: "))
while guess!=compnum:
    if guess<compnum:
        print("Your guess is too low.")
        count1=count1+1
        guess=int(input("Have another guess: "))
    elif guess>compnum:
        print("Your guess is too high.")
        count2=count2+1
        guess=int(input("Have another guess: "))
count=count1 + count2 + 1 #Το (+1) το έχω βάλει για να μετρήσω ως attetmpt και την σωστή απάντηση. 
print("Well done ! You guessed the number I was thinking of and it only took you ",count, "  attempts.")
    
#050
num=int(input("Please enter a number between 10 and 20: "))
while num<10 or num>20:
    if num<10:
        print("Too low.")
        print("Please try again.")
        num=int(input("Enter a number between 10 and 20: "))
    elif num>20:
        print("Too high.")
        print("Please try again.")
        num=int(input("Enter a number between 10 and 20: "))
print("Thank you.") #Γίνεται και με λιγότερες γραμμές κώδικα(βλ.Λύση βιβλίου)

#052
import random
num=random.randint(1,100)
print(num)

#053
import random
fruit=random.choice(["orange","apple","watermelon","mango"])
print(fruit)

#054(Modified)
import random
my_choice=random.choice(["Heads","Tails"])
users_choice=input("Please choose Heads or Tails: ")
users_choice=users_choice.title()
if my_choice==users_choice:
    print("Congratulations ! You win.")
if my_choice!=users_choice:
    print("Bad Luck.")
print("The computer selected",my_choice,", while you selected", users_choice, ".")

#055 (Modified)
import random
random_num=random.randint(1,10)
users_num=int(input("Please pick a whole number: "))
if random_num==users_num:
    print("Well Done.")
elif random_num>users_num:
    print("Too Low.")
    new_users_num=float(input("Have one more try: "))
    if new_users_num==random_num:
        print("Correct.")
    elif new_users_num!=random_num:
        print("You Lose.")
elif random_num<users_num:
    print("Too High.")
    new_users_num=float(input("Have one more try: "))
    if new_users_num==random_num:
        print("Correct.")
    elif new_users_num!=random_num:
        print("You Lose.")

#056
import random
random_num=random.randint(1,10)
answer=False #Θέτω την μεταβλητη answer για να μπορέσω να αρχίσω το while loop με μία έγκυρη και εύκολα διαχειρίσημη συνθήκη.
while answer==False :
    num=int(input("Enter a number: "))
    if random_num==num:
        answer=True
print("Congratulations !")

#057(Ουσιαστικά 056 expanded)
import random
random_num=random.randint(1,10)
answer=False
while answer== False:
    num=int(input("Please enter a number: "))
    if random_num>num:
        print("Too low.")
    elif random_num<num:
        print("Too high.")
    else: #(ή elif random_num==num:)
        answer=True
print("Congratulations !")

#058
import random
score=0
for i in range(1,6):#5 Επαναλήψεις
    random_num1=random.randint(1,1000)
    random_num2=random.randint(1,1000)
    correct= random_num1 + random_num2
    print(random_num1, "+", random_num2, "= ?")
    answer=int(input("Please enter your answer: "))
    print() #Αφήνει μία κενή γραμμή
    if answer==correct:
        score+=1 #Αυξάνω το score κατά 1
print("You scored", score, "out of 5.")

#059(Modified)
import random
random_colour=random.choice(["Green", "Red", "Blue", "Black", "Brown"])
print("Pick a colour: Green, Red, Blue, Black or Brown.")
answer=True
while answer==True:
    users_choice=input("Enter a colour: ")
    users_choice=users_choice.title()
    if users_choice!=random_colour:
        if random_colour=="Green":
            print("I bet you are green with envy right now.")
        elif random_colour=="Red":
            print("I can see your face turning red from frustration.")
        elif random_colour=="Blue":
            print("You are propably feeling pretty blue right now.")
        elif random_colour=="Black":
            print("I like my coffe black. What about you?")
        elif random_colour=="Brown":
            print("You must be feeling pretty shitty right now.")
        else:
            print("Incorrect answer.")
    elif random_colour==users_choice:    
        answer=False
        print("Your guess was correct.")

#060 & 070
countries_tuple=("Greece", "Germany", "France", "Russia")
print(countries_tuple)
users_country=input("Please enter one of the displayed countries: ")
users_country=users_country.title()
print(countries_tuple.index(users_country))
country_pos=int(input("Please enter a number: "))
print(countries_tuple[country_pos])

#071
sports=["football", "tennis"]
sports.append(input("Enter your favourite sport: "))
sports.sort() # Οι γραμμές 469 και 470 μπορούν να συνδυαστούν σε μία γραμμή ως εξής: print(sorted(sports))
print(sports)

#072
school_subjects=["Physics", "Chemistry", "Geometry", "Philosophy", "History", "Algebra"]
print(school_subjects)
users_subject=input("Which of the above subjects is your least favourite? : ")
users_subject=users_subject.title()
school_subjects.remove(users_subject)
print(school_subjects)

#073
food_dict={}
food_1=input("Please enter one of your favourite foods: ")
food_dict[1]=food_1
food_2=input("Please enter one of your favourite foods: ")
food_dict[2]=food_2
food_3=input("Please enter one of your favourite foods: ")
food_dict[3]=food_3
food_4=input("Please enter one of your favourite foods: ")
food_dict[4]=food_4
print(food_dict)
nope=input("Please enter the food you want to remove from the list: ")
del food_dict[nope]
print(sorted(food_dict.values()))

#074
colours = ["red", "green" , "blue", "yellow", "white" , "black", "magenta", "purple", "pink", "orange"]
start_num = int(input("Please enter a number between 0 and 4 : "))
end_num = int(input("Please enter a number between 5 and 9 : "))
print(colours[start_num:end_num + 1])

#075
list = [101, 202, 303, 404]
for num in list:
    print(num)
num = int(input("Please enter a three-digit number: "))
if num in list:
    print(list.index(num))
else:
    print("That is not in the list.")
    
#076 & 077 (Modified and Fortified)
guests = input("Please enter the names of three people you want to invite to your party (with spaces in between, no comas): ")
guests = guests.title()
guests = guests.split()
if len(guests) != 3:
    print("Invalid input.")
    
else:
    question_1 = input("Would you like to enter another name to the guest list for your party ?(Answer with Yes or No) : ")
    question_1 = question_1.title()
    
    if question_1 == "Yes":
        
        while question_1 == "Yes" :
            extra_guest = input("Please enter the name of the person you want to add to the guest list for your party: ")
            extra_guest = extra_guest.title()
            guests.append(extra_guest)
            question_1 = input("Would you like to enter another name to the guest list for your party ?(Answer with Yes or No")
            question_1 = question_1.title()    
        length = len(guests)
        print(f"You have invited {length} people to your party.")
        print("Namely, the people you have invited are:")
         
        for name in guests:
            print(name)
            
        question_2 = input("Would you like to make any changes to your guest list ? (Answer with yes or no) : ")
        question_2 = question_2.title()
        
            
        if question_2 == "Yes":
            question_3_a = input("Would you like to remove someone from the guest list ? (Answer with yes or no) : ")
            question_3_a =question_3_a.title()
        
            if question_3_a == "Yes":
                out = input("Please enter the name of the person you want to remove from your guest list: ")
                out = out.title()
                guests.remove(out)
                question_4 = input("Would you like to remove another person ? (Answer with yes or no) : ")
                question_4 = question_4.title()
                
                while question_4 == "Yes":
                    out = input("Please enter the name of the person you want to remove from your guest list: ")
                    out = out.title()
                    guests.remove(out)
                    question_4 = input("Would you like to remove another person ? (Answer with yes or no) : ")
                    question_4 = question_4.title()
                    
                length = len(guests)
                print("Your invitation is looking something like this: ")
                print(f"You have invited {length} people to your party.")
                print("Namely, the people you have invited are:")
                
                for name in guests:
                    print(name)
                    
                #question_2 = input("Would you like to make any changes to your guest list ? (Answer with yes or no) : ")
                #question_2 = question_2.title()
                #ΠΑΛΙ ΘΕΛΩ ΜΙΑ ΕΝΤΟΛΗ Ή ΚΑΤΙ ΓΙΑ ΝΑ ΚΑΝΩ Go to.
                
                
                # if question_2 == "Yes":
                #    print("")
                #elif question_2 == "No":
                    #ΜΕ ΚΑΠΟΙΟ ΤΡΟΠΟ ΘΕΛΩ : μία εντολή go to ή να καλέσω μία συνάρτηση εφόσον έχω ορίσει το πάνω κομμάτι ως μία Def. 
                    # Δηλαδή να με ξανα ρωτάει το πρόγραμμα εάν θέλω να κάνω remove ή add άτομα στην λίστα guests και να ξαναρχίζει 
                    # η διαδικασία από την αρχή, χωρίς να χρησιμοποιήσω τόσα πολλά if clauses.
                #else:
                #    print("Invalid answer. Answer with 'yes' or 'no'.")
                            
            elif question_3_a == "No":
                question_3_b = input("Would you like to add someone to your guest list ? (Answer with yes or no) : ")
                question_3_b = question_3_b.title()
                
                if question_3_b == "Yes":
                    more = input("Please enter the name of the person you want to add to your guest list: ")
                    more = more.title()
                    guests.append(more)
                    question_5 = input("Would you like to add another person ? (Answer with yes or no) : ")
                    question_5 = question_5.title()
                
                    while question_5 == "Yes":
                        more = input("Please enter the name of the person you want to add to your guest list: ")
                        more = more.title()
                        guests.append(more)
                        question_5 = input("Would you like to add another person ? (Answer with yes or no) : ")
                        question_5 = question_5.title()
                
                elif question_3_b == "No":
                    length = len(guests)
                    print("Your invitation is looking something like this: ")
                    print(f"You have invited {length} people to your party.")
                    print("Namely, the people you have invited are:")

                    for name in guests:
                        print(name)
                    
                    #question_2 = input("Would you like to make any changes to your guest list ? (Answer with yes or no) : ")
                    #question_2 = question_2.title()
                    #ΠΑΛΙ ΘΕΛΩ ΜΙΑ ΕΝΤΟΛΗ Ή ΚΑΤΙ ΓΙΑ ΝΑ ΚΑΝΩ Go to.
                
                else:
                    print("Invalid answer. Answer with 'yes' or 'no'.")  
            
            elif question_2 == "No":
                length = len(guests)
                print("Your invitation is looking something like this: ")
                print(f"You have invited {length} people to your party.")
                print("Namely, the people you have invited are:")

                for name in guests:
                    print(name)
                
                #question_2 = input("Would you like to make any changes to your guest list ? (Answer with yes or no) : ")
                #question_2 = question_2.title()
                #ΠΑΛΙ ΘΕΛΩ ΜΙΑ ΕΝΤΟΛΗ Ή ΚΑΤΙ ΓΙΑ ΝΑ ΚΑΝΩ Go to.

            else:
                print("Invalid answer. Answer with 'yes' or 'no'.")     
                
        elif question_2 == "No":
            length = len(guests)
            print("Your invitation is looking something like this: ")
            print(f"You have invited {length} people to your party.")
            print("Namely, the people you have invited are:")

            for name in guests:
                print(name)
        
        else:
            print("Invalid answer. Answer with 'yes' or 'no'.")         
                 
    elif question_1 == "No":
        length = len(guests)
        print("Your invitation is looking something like this: ")
        print(f"You have invited {length} people to your party.")
        print("Namely, the people you have invited are:") 
        
        for name in guests:
            print(name)
        
        #question_2 = input("Would you like to make any changes to your guest list ? (Answer with yes or no) : ")
        #question_2 = question_2.title()
        #ΠΑΛΙ ΘΕΛΩ ΜΙΑ ΕΝΤΟΛΗ Ή ΚΑΤΙ ΓΙΑ ΝΑ ΚΑΝΩ Go to.
    
    else:
        print("Invalid answer. Answer with 'yes' or 'no'.")  
                      
            
#                   ΣΧΟΛΙΑ
# 
#    ΘΑ ΜΠΟΡΟΥΣΑ ΝΑ ΧΡΗΣΙΜΟΠΟΙΗΣΩ ΑΝΤΙ ΓΙΑ ΠΟΛΛΑ INPUTS ΕΝΑ ΚΑΙ ΜΕΤΑ ΧΡΗΣΙΜΟΠΟΙΩΝΤΑΣ ΤΗΝ ΕΝΤΟΛΗ .split()
#ΝΑ ΤΟ ΕΚΑΝΑ ΛΙΣΤΑ ΚΑΙ ΜΕΤΑ ΝΑ <<ΠΡΟΣΘΕΤΑ >> Ή ΝΑ <<ΑΦΑΙΡΟΥΣΑ>> ΑΝΤΙΣΤΟΙΧΑ ΤΟ ΟΝΟΜΑΤΑ ΠΟΥ ΥΠΗΡΧΑΝ ΣΕ ΑΥΤΗΝ
#ΤΗΝ ΛΙΣΤΑ ΑΠΟ ΤΗΝ ΗΔΗ ΥΠΑΡΧΟΥΣΑ guests ΛΙΣΤΑ.
#
#    ΕΠΙΠΛΕΟΝ ΘΑ ΜΠΟΡΟΥΣΑ ΝΑ ΔΟΚΙΜΑΣΩ ΓΙΑ ΠΟΛΥ ΠΙΟ <<ΚΑΘΑΡΟ>>, ΑΛΛΑ ΚΑΙ <<ΒΕΛΤΙΣΤΟΠΟΙΗΜΕΝΟ>> ΚΩΔΙΚΑ
#ΝΑ ΔΟΥΛΕΨΩ ΜΕ Dictionairies ΚΑΙ ΜΕ ΣΥΝΑΡΤΗΣΕΙΣ ΤΥΠΟΥ Def. 
#

# 078
list = [ "Miracle Workers", "Lucifer", "Dopesick", "Band of Brothers"]
for show in list:
    print(show)
selection = input("Please enter a tv show of your choosing: ")
selection = selection.title()
index = int(input("Please enter the position to which you want your selected tv show to be inserted into the existing list: "))
list.insert(index, selection)
for show in list:
    print(show)

# 079
nums = []
choice = True
count = 0
while choice is True:
    if count < 3:
        num = int(input("Please enter a number: "))
        nums.append(num)
        count += 1
    else:
        choice = False
question = input("Would you like to remove the last number you added to the list ? (Answer with 'Y' or 'N' : ")
question = question.title()
if question == "Y":
    nums.remove(nums[2])
    print(nums)    
else:
    print(nums)    