from RobotArm import RobotArm
r = RobotArm()
r.randomLevel(1,7)
x=0
for i in range(6):
    x+=1
    r.grab()
    for i in range(x):
        r.moveRight()
    r.drop()
    for i in range(x):
        r.moveLeft()
r.wait()