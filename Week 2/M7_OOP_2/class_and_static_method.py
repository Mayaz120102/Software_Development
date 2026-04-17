class StarTech:
    location = {} #static attribute/class attribute

    def __init__(self,address, floor):
        self.address = address #instance attribute
        self.floor = floor
    
    @classmethod
    def sell(self, Pc, monitor, mobile):
        self.Pc = Pc
        self.monitor = monitor
        self.mobile = mobile
        print(f'buying : {Pc},{monitor} {mobile}')
    
    @staticmethod
    def purchase(item , price,amount):
        remaining = amount - price
        print(f'{item} {amount} {remaining}')


# StarTech.sell(2,3,4) #class method need no instance 
StarTech.purchase(3,4,5)
