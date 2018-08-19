# National Insurance Contributions Class
class NicModel():    
    def __init__(self, profit):
        self.profit = profit
        self.per_week_value = 2.85 # used for NI Class 2
        # Thresholds
        self.lower_threshold = 6025
        self.higher_threshold = 8164 
        self.nic_amount = self.set_nic_amount()
            
    def set_nic_amount(self):
        if self.lower_threshold <= self.profit <= self.higher_threshold:
            return self.set_class2()        
        return self.set_class4()
    
    def set_class2(self):
        return self.per_week_value * 52
    
    def set_class4(self):
        return (self.profit - self.lower_threshold) * 0.09