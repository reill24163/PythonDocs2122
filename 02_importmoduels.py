#import the basics moduel to use its code
import basics

#make a new application object from the basics module
app = basics.newProgram()

#use a method that belongs to our new application object
app.print('yo mama')

#print a property of our new application object
app.print( app.debugging )

#This line won't print if app.debugging is False
app.debug("Hello")

#We'll enable debuggung for the application
app.debugging = True
app.debug('Now it works!')

#import a default Python module
import random

#Use a method from the random module
randomNumber = random.randint(1, 10)
app.print(randomNumber)
