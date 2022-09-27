from RobotArm import RobotArm

r = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

r.grab();
r.moveRight();
r.moveRight();
r.drop();
r.moveLeft();
r.moveLeft();
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
r.moveLeft();

# Na jouw code wachten tot het sluiten van de window:
r.wait()