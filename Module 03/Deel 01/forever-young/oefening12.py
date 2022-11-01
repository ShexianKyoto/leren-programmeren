from RobotArm import RobotArm
r = RobotArm('exercise 11')
back = 9
r.speed=3
for i in range(9): 
    back-=1
    r.grab()
    kleur = r.scan()
    if kleur == 'red': 
        for i in range(9): r.moveRight()
        r.drop()
        for i in range(back): r.moveLeft()
    else: r.drop(), r.moveRight()
r.wait()