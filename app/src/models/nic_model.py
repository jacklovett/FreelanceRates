class NicModel():
    """
    National Insurance Contributions Class
    """  
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
        if self.class4_threshold <= self.profit:
            return 4
        elif self.class2_threshold <= self.profit:
            return 2
        else:
            return 0
    
    def get_nic_amount(self):
        if self.get_nic_class() == 2:
            return self.get_class2_amount()
        elif self.get_nic_class() == 4:     
            return self.get_class4_amount()
        else:
            return 0
    
    def get_class2_amount(self):
        # is this correct? should it be per week works excluding holiday taken?
        return self.per_week_value * 52

    def get_class4_amount(self):
        if self.class4_higher_threshold <= self.profit:
            return self.get_class4_higher_amount()                      
        return (self.profit - self.class4_threshold) * 0.09

    def get_class4_higher_amount(self):
        amount_above_higher_threshold = (self.profit - self.class4_higher_threshold) * 0.02
        amount_below_higher_threshold = (self.class4_higher_threshold - self.class4_threshold) * 0.09
        nic_amount = amount_below_higher_threshold + amount_above_higher_threshold
        return round(nic_amount, 2)