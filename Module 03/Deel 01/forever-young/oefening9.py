from RobotArm import RobotArm
r = RobotArm('exercise 9')
loop, x=0, 4
for i in range(10):
    loop+=1
    r.grab()
    for i in range(5): r.moveRight()
    r.drop()
    if loop == 4: x = 7
    elif loop == 5: x = 4
    elif loop == 7: x = 6
    elif loop == 8: x = 4
    elif loop == 9: x = 5
    for i in range(x): r.moveLeft()
r.wait()