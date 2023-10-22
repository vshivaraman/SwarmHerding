import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpat
import sympy as syp

# Sheep class
# Dog class
# Rungekutta function (sheep)
# Equation Solver for delta
# Find dog position
# Rungekutta function (dog)

step = 0.01

class sheep_dog:

    def __init__(self,init_pos,num_dogs):
        self.sheep_position = init_pos # numpy Array (x,y)
        self.Ks = 0.04 # Put value
        self.num_dogs = num_dogs
        self.angle_encir = np.pi/4 # In radians
        self.dog_angle = np.arctan(init_pos.item(1)/init_pos.item(0))+self.angle_encir*np.linspace(-1/2,1/2,self.num_dogs)
        print(self.dog_angle)
        self.radius_encir = 2# Some value
        self.dog_position = (init_pos+self.radius_encir*np.array([np.cos(self.dog_angle),np.sin(self.dog_angle)])).T
        self.Kd = 3# Put value

        self.switch = False
        self.handle = [0]*(num_dogs+1) 

        self.fig,self.ax = plt.subplots()
        self.ax.set_xlim(-10,10)
        self.ax.set_ylim(-10,10)
        self.ax.set_title('Simulation')
        self.ax.grid()

    def cont_func(self,u,K):
        return -K*u

    def rk4(self,pos,K):
        k1 = self.cont_func(pos,K)
        k2 = self.cont_func(pos+step*k1/2,K)
        k3 = self.cont_func(pos+step*k2/2,K)
        k4 = self.cont_func(pos+step*k3,K)
        pos += 1/6*step*(k1+2*k2+2*k3+k4)
        return pos

    def req_dog_pos(self,num_dogs,radius,position):
        Ks = 0.04
        d = syp.Symbol('d')
        rhs = Ks*np.linalg.norm(position)

        angle_encir = float(syp.nsolve(syp.sin(num_dogs*d/(2-2*num_dogs))/(radius**2*syp.sin(d/(2-2*num_dogs)))+rhs,d,4))#+np.pi/180
        req_angle = np.arctan(position.item(1)/position.item(0))+np.pi+angle_encir*np.linspace(-1/2,1/2,num_dogs)
        
        #print(req_angle.shape)
        # Error in line 57
        req_dog_pos = (position+radius*np.array([np.cos(req_angle),np.sin(req_angle)])).T
        #print(req_dog_pos)

        return req_dog_pos

    def animate(self,req_dog_pos):
        r = 0.1
        r1 = 0.1
        count = 0

        if self.switch == False:
            self.handle[0] = mpat.Circle((self.sheep_position[0],self.sheep_position[1]),r,color='red')
            self.ax.add_patch(self.handle[0])
            
            for i in range(1,num_dogs+1):
                self.handle[i]  = mpat.Circle((self.dog_position[count][0],self.dog_position[count][1]),r1)
                self.ax.add_patch(self.handle[i])
                count += 1

            self.switch = True
        else:
            self.handle[0].set_center((self.sheep_position[0],self.sheep_position[1]))
            
            for i in range(1,num_dogs+1):
                self.handle[i].set_center((self.dog_position[count][0],self.dog_position[count][1]))
                count += 1

num_dogs = 4

sh = sheep_dog(np.array([[3.],[4.]]),num_dogs)
#sh1 = sheep_dog(np.array([[2.],[1]]),num_dogs)
print(sh.dog_position)
#plt.scatter

t = 0.01
#x = []
#y = []
radius = 1 

i = 0
#sh.animate(sh.dog_position)
#plt.show()

while t < 50:

    t_next = t + 0.1
    while t < t_next:
        sh.sheep_position = sh.rk4(sh.sheep_position,sh.Ks)
        req_dog_pos = sh.req_dog_pos(num_dogs,radius,sh.sheep_position)
        #print(req_dog_pos)
        sh.dog_position = sh.rk4(req_dog_pos-sh.dog_position,sh.Kd) #+ 3
        t += 0.01
    i+=1

    sh.animate(sh.dog_position)

    plt.pause(0.01)

t = np.arange(0,10,0.01)


