# National Insurance Contributions Class
class NicModel():   

    #Thresholds
    lower_threshold = 6025
    higher_threshold = 8164

    # For class 2
    per_week_value = 2.85

    def __init__(self, profit):
        self.profit = profit         
            
    def get_nic_amount(self):
        if self.lower_threshold <= self.profit <= self.higher_threshold:
            return self.class2()        
        return self.class4()
    
    def class2(self):
        return self.per_week_value * 52
    
    def class4(self):
        return (self.profit - self.lower_threshold) * 0.09