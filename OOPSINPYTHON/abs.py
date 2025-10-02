class Car:
    def _init__(self):
     self.acc= False
     self.brk = False
     self.clutch= False
   def start(self):
      self.clutch= True
      self.acc = True
      print("car started..")
carnew = Car()
carnew.start()