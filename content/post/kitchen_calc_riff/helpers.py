class BaseTimeFrame:
    def __init__(self, ndays) -> None:
        """Base data for a time frame

        Args:
            ndays (int): Number of days in the timeframe
        """
        self.ndays = ndays

    def __str__(self):
        return f'Number of days: {self.ndays}'
        
    def __truediv__(self, other):
        return self.ndays / other.ndays

# $5 2 times a week vs. $100 per month

class Consumption:
    """ Eating 2 apples 3 times per week.
    
    """
    def __init__(self, freq, units) -> None:
        self.freq = freq
        self.units = units # Should be an instance of BaseTimeFrame

    def __truediv__(self, other):
        print(f'a happens {self.freq / self.units.ndays} times.')
        print(f'b happens {other.freq / other.units.ndays} times.')
        return self.units / other.units