# calculating my GPA

print "Enter your password: "
password = raw_input()

while (password != "sami013"):
    print "Your password is wrong. Please try again"
    print"Enter your password: "
    password = raw_input()
print "Welcome to the Final Grade Calculator"  #once password was correct

""
""

print "Hey Samira just a reminder:" \
      " Every grade count in a dfferent weight"

print ""

print "Enter the number of grades: "
numberOfGrades = int(raw_input())  #7 grades

sum = 0.0

#the for loop to compute the data entred
for element in range(1, numberOfGrades + 1):  #cause the right limitis not inclusive
    print "Grade", element , "is: " # pritning the index basically. Note that I set the range from 1
    grade = int(raw_input())
    if (element == 1 or element == 2 or element == 3 or element == 4 or element == 6):
        weight = grade * (20.0 / 100)
        print weight
        while(element <= 4):
            subSum = 0.0
            subSum = (subSum + weight) #/ subElements
            weight = subSum / 4
            element+=1
            print "Average of assigments" , weight
    else:                #element 5 . first midterm
        weight = grade * (25.0 /  100)
        print weight
  #  else:
    #    weight = (grade * 35) / 100
    #    print weight


print "" \
      ""

sum = (sum + weight) / 6
print "Your average for now is: " , sum


#GPA = sum/ numberOfGrades
#print "GPA", GPA
raw_input( "Please press <enter> to finalize the program")