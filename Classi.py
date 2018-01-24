class my_class:

    t=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        my_class.t+=1

    def printTotal(self):
        print ("totali:", my_class.t)


    def displayXY(self):
        print "x ", self.x, "y ", self.y


class Child(my_class): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

   def printTotal(self):
       print 'override'

   def displayXY(self):
       print 'nuovo'
