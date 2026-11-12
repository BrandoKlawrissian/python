#Reeborg's World - Hurdle 6
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():
#     move() #comment this out for the while loop
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for jump in range(0, 6):
#     hurdle()

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     hurdle()
#     number_of_hurdles -= 1
#     print(number of hurdles)

# while not at_goal():
#     while front_is_clear() and not at_goal():
#         move()
#     if not at_goal():
#         hurdle()

######################################################
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while not right_is_clear():
#         move()       
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

##########################################################
#Reeborg's Maze Challenge
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear() and not at_goal():
#     move()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()