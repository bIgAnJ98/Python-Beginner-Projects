#madlibs use string concatenation to program them in python.

#input for requesting words from the user
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")

madlib = f"We are our own {adj1} people and we love {noun1} and we will do anything for {verb1}"
madlib2 = "I love to sing {}".format(noun1)
madlib3 = "I love %s" % noun1
#print(madlib)
#print(madlib2)
print(madlib3)