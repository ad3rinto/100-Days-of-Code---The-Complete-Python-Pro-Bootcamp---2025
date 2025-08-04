def is_leap_year(year):
    """Check if a year is a leap year."""
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return "Leap Year"
    elif year % 4 != 0:
        return "Not a leap year"
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return "Not a leap year"
    else:
        return "leap year"



print(is_leap_year(2000))