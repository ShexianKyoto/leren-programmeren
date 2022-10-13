from RobotArm import RobotArm
r = RobotArm('exercise 8')
r.moveRight()
for i in range(1,8):
    r.grab()
    for i in range(1,9):
        r.moveRight()
    r.drop()
    for i in range(1,9):
        r.moveLeft()
r.wait()