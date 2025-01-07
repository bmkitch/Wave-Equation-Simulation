import numpy as np
import math


class WaveSim:
    #initialization
    def __init__(self, x, y, gridLength, M, stopWaveTime, timestep) -> None:
        self.XLENGTH = x
        self.YLENGTH = y
        self.GRIDLENGTH = gridLength
        self.TIMESTEP = timestep
        self.STOPWAVETIME = stopWaveTime

        self.M = M #Note: M is of the form c^2

        self.field = np.zeros((x, y))

        self.fieldT = np.zeros((x, y))

    #iterating
    def iterate(self, time):
        #setting up the initial conditions for a wave (wave origin boundary conditions) 3140
        if(time < self.STOPWAVETIME):
            self.field[0, :] = math.sin(time*self.TIMESTEP)
        else:
            self.field[0, :] = 0


        #finding first directional derivatives
        xGrad = np.gradient(self.field, axis=0) / self.GRIDLENGTH
        yGrad = np.gradient(self.field, axis=1) / self.GRIDLENGTH
        
        

        #finding the second directional derivatives
        xxGrad = np.gradient(xGrad, axis=0)
        yyGrad = np.gradient(yGrad, axis=1)
        

        
        #finding new first time derivatives
        self.fieldT = self.fieldT + self.M * (xxGrad + yyGrad) * self.TIMESTEP
        self.field = self.field + self.fieldT * self.TIMESTEP

        #Boundary conditions where wave doesn't originate
        self.field[self.XLENGTH-1, :] = 0
        self.field[:, 0] = 0
        self.field[:, self.YLENGTH-1] = 0
