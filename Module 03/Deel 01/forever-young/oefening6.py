from RobotArm import RobotArm

r = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for x in range(1,8):
    r.moveRight();
for x in range(1,9):    
    r.grab();
    r.moveRight();
    r.drop();
    r.moveLeft();
    r.moveLeft();

# Na jouw code wachten tot het sluiten van de window:
r.wait()