# Program file for Birthday countdown app.
from datetime import date


def print_header():

    """
    Prints the app header to stdout.
    """

    print("----------------------")
    print("BIRTHDAY COUNTDOWN APP")
    print("----------------------")
    print()


def get_birthday() -> date:

    """
    Gets the user's birthday from stdin. Converts it into a datetime.date
    object and returns it.

    :return: The user's birthday.
    """

    print("Please specify your birthday!")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [mm]: "))
    day = int(input("Day [dd]: "))
    print()

    birthday = date(year, month, day)

    return birthday


def count_days_between_dates(birthday: date, compare_date: date) -> int:

    """
    Counts the number of days between two dates as if the two dates were in the
    same year.

    The return value is signed. A positive value means that the birthday comes
    before compare date. A negative value means that the birthday comes after
    compare date.

    :param birthday: user's birthday
    :param compare_date: date to compare the birthday to
    :return: Number of days.
    """

    # Get the compare date as if it was in the same year as the birthday.
    baseline_year = birthday.year
    compare_date_with_baseline = date(
        baseline_year, compare_date.month, compare_date.day
    )

    # Count the difference in days.
    date_delta = birthday - compare_date_with_baseline
    n_days = date_delta.days

    return n_days


def print_result(n_days: int):

    """
    Prints the result from this app, namely how many days between the birthday
    and today.

    :param n_days: number of days
    """

    if n_days > 0:
        print("Your birthday is in {} day(s).".format(n_days))
    elif n_days < 0:
        print("Your birthday was {} day(s) ago.".format(-n_days))
    else:
        print("Today is your birthday. Happy birthday!")


def main() -> int:

    """
    Main program flow.

    :return: Exit code. Always returns 0.
    """

    print_header()
    birthday = get_birthday()
    today = date.today()
    n_days = count_days_between_dates(birthday, today)
    print_result(n_days)

    return 0


# Run the app.
main()
