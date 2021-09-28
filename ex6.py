#assigning a value to the variablel 
types_of_poeple = 10
#assigning strings into the below variables with format strings within the strings  
x = f"There are {types_of_poeple} types of poeple."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#printing the variable set erier  
print(x)
print(y)
#printing the veriables using the format string function
print(f"I said: {x}")
print(f"I also said '{y}'")

hilarious = False 
joke_evaluation = "Isnt that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of...."
e = "a string with a right side."

print (w + e)


