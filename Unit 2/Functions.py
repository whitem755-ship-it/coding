# function- is a set of instructions labled under
# a custom name that the computer will run.

# Function syntax (rules of how its written)
# function have 2 phases: function definition and
# function call

# Phase 1:function defintion
# we are describing the instruction for our custom code.
# we are adding logic to th\e computers vocbulary.
# this code does not run- it only give the computer the meaning
# not the action

def example():
        print('good morning.') # 1 instruction: print good morning

 # phase 2: function call
 # once we have the definition, we can run the instructions
# by writting the function name.

example()

# we indent to inform the computer that we are about to write
# code instructions. if we don't, we will get an error
def example2():
   print('good day')
   a = input ('enter a number:')
   print(a)

example2()

def math():
      a = input("please enter a number:")
      b = 30
      print("here is your result!")
      print(int(a) + b)
 

math()

# create a function that will calculate 2 numbers
# with different arithmetic operators
def calculate():
    numx = input('please enter a number:')
    numy = input('please enter anthor number:')
    print(numx, numy)

calculate()

# The function definition is the play that the team learns
# The function invocation/ call is when your actually using it
# A function parameter is a part of the function definition
# the parameter is a placeholder for data that will be actually used
# A function argument goes into the function invocation or call. This is real data

