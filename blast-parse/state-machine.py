#--------------------------------------------------------------------
#
# BIOL / CMPU 353
# Spring 2020
#
# Algorithm by: Jodi Schwarz and Marc Smith
# Written by: Marc Smith and Jodi Schwarz
#
# State machine simulation
#
# Description: program that cycles between a fixed number of 
#              states a fixed number of times.
#
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# States: Each state represents the line being searched for
#         in the BLAST search results file.
#
#         There are four possible states: S1, S2, S3, and S4.
#         Initial state is S1. Here is the state transition 
#         diagram: (this is equivalent to drawing a state
#         transition diagram, which is hard to do in a text file)
#
#         From-State  ->  To-State  
#         ----------      --------  
#             S1      ->     S2
#             S2      ->     S3
#             S3      ->     S4
#             S4      ->     S1
#
#--------------------------------------------------------------------
S1 = 1;  # you determine what each state means
S2 = 2;  # and document that meaning
S3 = 3;  # for each state
S4 = 4;  # 

# state keeps track of the current state
state = S1 # initial state is S1

# Print header line
print("Beginning execution of our state machine...")

# transition between states a fixed number of times
for i in range(1,42):
		
	# print current state
	print("state %d" % (state))
		
	# if we're in state 1...
	if state == S1: 
		# transition to state 2...
		state = S2
	
	# else if we're in state 2...
	elif state == S2: 
		# transition to state 3...
		state = S3
		
	# else if we're in state 3...
	elif state == S3:  
		# transition to state 4...
		state = S4

	# else if we're in state 4...
	elif state == S4:
		# transition back to state 1...
		state = S1

	else:
		print("===> Error transitioning between states!")

  
print("You now know the answer to life, the universe, and everything...")
print("But what is the question???")
