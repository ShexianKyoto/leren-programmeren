from RobotArm import RobotArm
r = RobotArm('exercise 10')
#r.speed = 3
direction=1
for i in range(4): r.moveRight()
for i in range(5):
    r.grab()
    for i in range(direction): r.moveRight()
    direction+=1
    r.drop()
    for i in range(direction): r.moveLeft()
    direction+=1
r.wait()