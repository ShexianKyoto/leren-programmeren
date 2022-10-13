from RobotArm import RobotArm
r = RobotArm('exercise 7')
for i in range(1,6):
    r.moveRight()
    for i in range(1,7):
        r.grab()
        r.moveLeft()
        r.drop()
        r.moveRight()
    r.moveRight()
r.wait()