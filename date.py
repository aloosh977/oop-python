def isLeapYear(year: int) -> bool:
    if year % 4 == 0:
        return True
    else:
        return False


def maxDays(month: int, year: int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        raise ValueError("Month must be between 1 and 12")


def dateCorrection(day: int, month: int, year: int):
    while month > 12:
        year += 1
        month -= 12
    while day > maxDays(month, year):
        day -= maxDays(month, year)
        month += 1
    while month > 12:
        year += 1
        month -= 12
    return Date(day, month, year)


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        if not (year > 1):
            raise ValueError("Year must be positive")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        mxdays = maxDays(month, year)
        if not (1 <= day <= mxdays):
            raise ValueError("Invalid Day value")
        self.day = day
        self.month = month
        self.year = year

    def __add__(self, duration):
        if not isinstance(duration, Duration):
            raise TypeError("You can only add Duration to Date")
        newDay: int = self.day + duration.day
        newMonth: int = self.month + duration.month
        newYear: int = self.year + duration.year
        newDate = dateCorrection(newDay, newMonth, newYear)
        return newDate

    def __str__(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"


class Duration:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)


today = Date(26, 12, 2025)
dur = Duration(21, 55, 2)
print(today + dur)
