from RobotArm import RobotArm
r = RobotArm('exercise 11')
for i in range(9): 
    r.grab()
    kleur = r.scan()
    if kleur == 'white': r.moveRight(), r.drop(), r.moveRight()
    else: r.drop(), r.moveRight()
r.wait()