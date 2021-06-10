class Car(object) :
    def __init__(self,company,model,color,speed_limit) :
        self.company=company
        self.model=model
        self.color=color
        self.speed_limit=speed_limit

    def start(self):
        print("Car Started")   

    def stop(self):
        print("Car Stoped")     

    def accelerate(self):
        print("Accelerating Car")  

    def change_gear(self,gear_type):
        print("Gear Changed To",gear_type)       

Mercedes_Benz=Car("Mercedes_Benz","Classic-1","Black",200)
Mercedes_Benz.start()
Mercedes_Benz.stop()    
Mercedes_Benz.accelerate()    
Mercedes_Benz.change_gear(4)                 