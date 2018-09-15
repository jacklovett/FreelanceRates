# National Insurance Contributions Class
class NicModel():   
    # Class2 Threshold
    class2_threshold = 6205
    # Class4 Thresholds
    class4_threshold = 8424
    class4_higher_threshold = 46350
    # Used for class 2
    per_week_value = 2.95

    def __init__(self, profit):
        self.profit = profit        

    def get_nic_class(self):
        if self.class2_threshold <= self.profit <= self.class4_threshold:
            return 2
        else:
            return 4
    
    def get_nic_amount(self):
        if self.get_nic_class == 2:
            return self.get_class2_amount()       
        return self.get_class4_amount()
    
    def get_class2_amount(self):
        return self.per_week_value * 52

    def get_class4_amount(self):
        if self.class4_higher_threshold < self.profit:
            amount_above_higher_threshold = (self.profit - self.class4_higher_threshold) * 0.02
            amount_below_higher_threshold = (self.class4_higher_threshold - self.class4_threshold) * 0.09
            return amount_below_higher_threshold + amount_above_higher_threshold            
        return (self.profit - self.class4_threshold) * 0.09       

