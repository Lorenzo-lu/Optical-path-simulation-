import numpy as np;
import matplotlib.pyplot as plt;

print('running');


class lens:
    def __init__(self,x,f):
        self.posit = x;
        self.focus = x + f;
        # minus f if concave lens; plus f if convex lens
        

class beams:
    def __init__(self,origin,direction,lens):
        self.x = [origin[0]];
        self.y = [origin[1]];
        self.lens = lens; 
        self.direction = direction;
        
        for L in lens:            
            self.nodes_at_len(L);
            #self.nodes_converge(L);
        
    def nodes_at_len(self,Len):
        # nodes at the len
        x = Len.posit;
        y = (x - self.x[-1]) / self.direction[0] * self.direction[1] + self.y[-1];
        self.x += [x];
        self.y += [y];
        self.nodes_converge(Len);
        
        
    def nodes_converge(self,Len):
        # this function is called by the last one
        # don't worry
        
        focus = [Len.focus,0];
        center = [Len.posit,0];
        posi0 = [self.x[-2],self.y[-2]];# from the previous len
        posi1 = [Len.posit,self.y[-2]]; # on current len

        if posi0[1] == center[1]:
            # when posi0 and the focus of this len overlap
            # it means d1 = 2f
            self.direction[1] *= -1;
            return;       

        M = np.array([[posi0[0],1],[center[0],1]]);
        z = np.array([[posi0[1]],[center[1]]]);
        
        inv_M = np.linalg.pinv(M);
        k1 = inv_M.dot(z);
        #k1 = v[0,0];
        #b1 = v[1,0];
        
        # calculate the line2 expression: connecting the posi1 and the focus;
        M = np.array([[posi1[0],1],[focus[0],1]]);
        z = np.array([[posi1[1]],[focus[1]]]);
        
        inv_M = np.linalg.pinv(M);
        
        k2 = inv_M.dot(z);
        #k2 = v[0,0];
        #b2 = v[1,0];
        
        # calculate the intersection of these two beams
        M = np.array([[-k1[0,0],1],[-k2[0,0],1]]);
        z = np.array([[k1[1,0]],[k2[1,0]]]);

        if np.linalg.matrix_rank(M) <2:
            delta_x = focus[0] - posi1[0];
            delta_y = focus[1] - posi1[1];
            self.direction = [delta_x,delta_y];
            return;
        
        inv_M = np.linalg.pinv(M);
        
        coord = inv_M.dot(z);
        
        x = coord[0,0];
        y = coord[1,0];
        
        delta_x = x - self.x[-1];
        delta_y = y - self.y[-1];
        self.direction = [delta_x,delta_y];
        
# example
L1 = lens(10,5);
L2 = lens(20,5);
L3 = lens(30,5);
L4 = lens(45,5);

B1 = beams([0,5],[10,0],[L1,L2,L3])
B2 = beams([0,5],[10,-5],[L1,L2,L3]); # with small bug here (singular value)
#print(B.x,B.y)
print(B1.x,B1.y);
print(B2.x,B2.y);

plt.figure();
plt.plot(B1.x,B1.y);
plt.plot(B2.x,B2.y);
plt.show();
