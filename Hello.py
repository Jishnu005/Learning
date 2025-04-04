class Number:
    def __init__(self, num, max=0, min=9):
        self.num = num
        self.max = max
        self.min = min

    def check_max(self, number=None):
        if number == None:
            number = self.num
        if number==0:
            number = self.num
            return self.max
        
        last_di = number%10
        if last_di > self.max:
            self.max = last_di
        number //= 10
        return self.check_max(number)
    
    def check_min(self, number=None):
        if number == None:
            number = self.num
        if number==0:
            return self.min
        first_di = number%10
        if first_di<self.min:
            self.min = first_di
        number //= 10
        return self.check_min(number)
    
n = Number(int(input("Enter any number:")))
print(f"The maximum value of digit:{n.check_max()} in number:{n.num}")
print(f"The minimum value of digit:{n.check_min()} in number:{n.num}")