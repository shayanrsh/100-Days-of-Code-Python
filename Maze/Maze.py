def movement():
    wall_height = 0
    turn_left()
    while wall_on_right():
        move()
        wall_height += 1
    turn_right()
    move()
    turn_right()
    for height in range(wall_height):
        move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    elif right_is_clear():
        move()


  
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
