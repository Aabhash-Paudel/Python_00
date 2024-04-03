class rect1:
    def __init__(self,l,b,h,r):
        self.l,self.b,self.h,self.r=l,b,h,r
        
    def rectangle(self):
        print("The area of given rectangle is",self.l*self.b*self.h)
    def tr(self):
        print("the area of trangle: ",0.5*self.b*self.h)
    def cir(self):
        print("THe are of circle",3.1415*(self.r**2))


len=int(input("enter the length: "))
rad=int(input("enter the radius: "))
bread=int(input("Enter breadth: "))
heigh=int(input("Enter the height: "))
a1=rect1(len,bread,heigh,rad)
a1.rectangle()
a1.tr()
a1.cir()