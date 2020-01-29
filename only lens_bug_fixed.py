
import matplotlib.pyplot as plt;

print('running');


class lens:
    def __init__(self,center,f):
        self.posit = center;#in the form of [x,y]
        x = self.posit[0];
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
        x = Len.posit[0];
        y = (x - self.x[-1]) / self.direction[0] * self.direction[1] + self.y[-1];
        self.x += [x];
        self.y += [y];
        #self.nodes_converge(Len);
        self.refraction_at_len(Len);

    def refraction_at_len(self,Len):
        u = Len.posit[0] - self.x[-2];
        f = Len.focus - Len.posit[0];

        v_inv = 1/f - 1/u;
        if v_inv == 0:
            # item right on the focus
            self.direction = [u,Len.posit[1] - self.y[-2]];
            return
        v = 1/v_inv;

        self.direction = [v,(-(self.y[-2] - Len.posit[1]) * v / u - self.y[-1])];        

        
# example
L1 = lens([10,0],10);
L2 = lens([20,0],10);
L3 = lens([30,0],10);
L4 = lens([40,0],10);
L5 = lens([50,0],10);
Lens = [L1,L2,L3,L4,L5];

B1 = beams([0,5],[10,-.000],Lens);
B2 = beams([0,5],[10,-5.],Lens); 
#print(B.x,B.y)
print(B1.x,B1.y);
print(B2.x,B2.y);

plt.figure();
plt.plot(B1.x,B1.y);
plt.plot(B2.x,B2.y);
plt.show();
