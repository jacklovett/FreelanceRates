from constants import Constants as constants
class NicController():
    """
    National Insurance Contributions Class
    """  
    def __init__(self, profit):
        self.profit = profit        

    def get_nic_class(self):
        if constants.class4_threshold <= self.profit:
            return 4
        elif constants.class2_threshold <= self.profit:
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
        return constants.per_week_value * 52

    def get_class4_amount(self):
        if constants.class4_higher_threshold <= self.profit:
            return self.get_class4_higher_amount()                      
        return (self.profit - constants.class4_threshold) * 0.09

    def get_class4_higher_amount(self):
        amount_above_higher_threshold = (self.profit - constants.class4_higher_threshold) * 0.02
        amount_below_higher_threshold = (constants.class4_higher_threshold - constants.class4_threshold) * 0.09
        nic_amount = amount_below_higher_threshold + amount_above_higher_threshold
        return round(nic_amount, 2)