from Models import *

MicroalgaePBR1 = Model_Microalgae(D=0,X=0.2,Q=8.8,S=100)


# Run the update method multiple times
for _ in range(60000):
    newX, newQ, newS = MicroalgaePBR1.update_tertiolecta(D=0.5, dt=0.001)
    print(newX, newQ, newS)