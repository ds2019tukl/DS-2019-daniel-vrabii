from datetime import datetime as dt
import matplotlib.pyplot as plt

def time_stamp_to_date(time_stamp):
    """
    Converts time stamp string to datetime.

    :param time_stamp: Time stamp in format "%Y-%m-%d %H:%M:%S."
    :type time_stamp: str
    :return: datetime
    """

    time_stamp = time_stamp.split(".")[0]
    time = dt.strptime(time_stamp, "%Y-%m-%d %H:%M:%S")
    return time

def time_stamp_to_week(time_stamp):
    """
    Converts time stamp string to week in year.

    :param time_stamp: Time stamp in format "%Y-%m-%d %H:%M:%S."
    :type time_stamp: str
    :return: String of year and week in year
    """

    time_stamp = time_stamp.split(".")[0]
    time = dt.strptime(time_stamp, "%Y-%m-%d %H:%M:%S")
    week = time.isocalendar()[1]
    year = time.year
    return (str(year) + " Week: " + str(week))

def get_min(df, lower_bound):
    """
    Get minimum value of a dataframe, bigger than lower bound.

    :param df: Dataframe to get min from
    :type df: Pandas Dataframe
    :param lower_bound: Values smaller or equal are excluded from min
    :type lower_bound: int
    :return: Minimum
    """

    return df.loc[df > lower_bound].min()
    
def time_stamp_to_day(time_stamp):
    """
    Returns date in form "%Y-%m-%d"

    :param time_stamp: Time stamp in format "%Y-%m-%d %H:%M:%S."
    :type time_stamp: str
    :return: date
    """

    time = time_stamp.split(" ")[0]
    return time