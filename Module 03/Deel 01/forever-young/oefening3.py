from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')
r = robotArm
count = 1
# Jouw python instructies zet je vanaf hier:
while count != 5:
    r.grab();
    r.moveRight();
    r.drop();
    r.moveLeft();
    count += 1
    if count == 5: break
    continue

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()