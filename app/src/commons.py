class Commons:
    """
    Class to group together common methods and variables that can
    be used throughout the application
    """
    # Constants

    # TaxController    
    tax_free_amount = 11850
    # Boundaries
    higher_rate_threshold = 34500
    additional_rate_threshold = 150000

    # NicController
    # Thresholds
    # Class2 Threshold
    class2_threshold = 6205 # change to contant value + 1 (when adding constants class)
    # Class4 Thresholds
    class4_threshold = 8424
    class4_higher_threshold = 46350
    # Used for class 2 calculation
    per_week_value = 2.95 

    # StudentLoanController
    # payment free amounts
    payment_plan1_threshold = 18330
    payment_plan2_threshold = 25000

    @staticmethod
    def diff_or_zero(val_1, val_2):
        if val_1 > val_2:
            return val_1 - val_2
        return 0