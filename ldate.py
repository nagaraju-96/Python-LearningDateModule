# A simple date class for Learning to write classes

class LDate:

    # **class** method
    @classmethod
    def is_leap_year(cls,year: int) -> bool:
        """Return True if year is a leap year, False otherwise
           This should be a **class** method"""
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            return True
        return False
 
    # **class** method
    @classmethod
    def days_in_month(cls,year,  month):
        """ Return the number of days in the requested month"""
        days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if LDate.is_leap_year(year) and month ==2:
            return 29
        return days_list[month]

    # **class** method
    @classmethod
    def is_valid_date(cls,year, month, day):
        """ Return whether year-month-day represents a valid date.
            This should be a **class** method """
        if year <0 or month <0 or month >12:
            return False
        if day > LDate.days_in_month(year,month) or day<0:
            return False
        return True


    def __init__(self, year: int, month: int, day: int):
        """ Constructor 
            Raise a ValueError if year-month-day is not a valid date (e.g., 2022-15-27)
        """
        if LDate.is_valid_date(year,month,day):
            self.year =year
            self.month = month
            self.day = day
        else:
            raise ValueError


    def ordinal_date(self) -> int:
        """ Return the number of days elapsed since the beginning of the year, including any partial days.
            For example, the ordinal date for 1 January is 1."""
        number_of_days = 0
        for mon in range(1, self.month):
            number_of_days += LDate.days_in_month(self.year, mon)
        number_of_days += self.day
        return number_of_days


    def __eq__(self, other) -> bool:
        """ return whether the two objects represent the same date.
            return False if other is not an LDate. """
        if(type(other) == LDate):
            return self.year == other.year and self.month == other.month and self.day == other.day
        return False

        
    def __lt__(self, other) -> bool:
        """ return whether self < other.  
            Raise a ValueError of other is not an LDate """
        if not type(other) == LDate:
            raise ValueError
        else:
            if self.year < other.year:
                return True
            elif self.year == other.year:
                if self.month <other.month:
                    return True
                elif self.month == other.month:
                    return self.day<other.day
            return False

    def __le__(self, other) -> bool:
        """ return whether self <= other.  
            Raise a ValueError of other is not an LDate
            Use the methods above.  Don't re-implement the < algorithm! """
        if LDate.__lt__(self,other) or LDate.__eq__(self,other):
            return True
        return False


    def days_since(self, other) -> bool:
        """ Return the number of days that have elapsed since other.
            (In other words, when other < self, the result should be positive.)
        """
        if LDate.__eq__(self,other):
                return 0
        small =other
        large =self
        flag = False
        if LDate.__lt__(self,other):
            small =self
            large =large
            flag = True
        if small.year == large.year:
            return LDate.ordinal_date(large) - LDate.ordinal_date(small)
        temp = LDate(small.year,12,31)
        count = LDate.ordinal_date(temp) - (LDate.ordinal_date(small))
        for year in range(small.year + 1, large.year):
            count += 365
            if LDate.is_leap_year(year):
                count+=1 
        count += LDate.ordinal_date(large)
        if flag:
            count = count - (count*2)
        return count

    _DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    def day_of_week(self) -> str:
        """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
            Hint 1: 1 January 1753 was a Monday.
            Hint 2: Use the methods you've already written."""
        temp = LDate(1753,1,1)
        number_of_days = LDate.days_since(self,temp)
        day = number_of_days % 7

        return LDate._DAYS_OF_WEEK[day]



    def __str__(self) -> str:
        """ Return this date as string of the form "Wednesday, 07 March 1833"."""
        mnt_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        d_name = LDate.day_of_week(self)
        m_name = mnt_names[self.month]
        return f"{d_name}, {self.day:02d} {m_name} {self.year}"

    def __add__(self, days):
        """ Return a new LDate object that is the requested number of days after self. """
        year = self.year
        month = self.month
        day = self.day

        days_left = days+day
        
        while days_left > LDate.days_in_month(year,month):
            days_left -= LDate.days_in_month(year,month)
            month += 1

            if month > 12:
                month = 1
                year += 1

        return LDate(year, month, days_left)


    
if __name__ == '__main__':
    d1 = LDate(1941, 12, 7)
    d2 = LDate(2023, 11, 1)
    print(d1)
    print(d2)
    print(d2.days_since(d1)) 
