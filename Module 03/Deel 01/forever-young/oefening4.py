from RobotArm import RobotArm

r = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(1, 3):
    r.grab();
    r.moveRight();
    r.moveRight();
    r.drop();
    r.moveLeft();
    r.moveLeft();
r.grab();
r.moveRight();
r.drop();
r.moveRight();
r.grab();
r.moveLeft();
r.drop();
r.moveRight();
r.grab();
r.moveLeft();
r.drop();

# Na jouw code wachten tot het sluiten van de window:
r.wait()