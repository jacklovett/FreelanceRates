class CommonsClass():
    """ Class to store common methods that will be used throughout the project """
    @staticmethod
    def value_or_zero(val_1, val_2):
        if val_1 > val_2:
            return val_1 - val_2
        return 0
