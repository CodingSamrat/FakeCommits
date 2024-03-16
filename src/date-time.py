"""
      _____
     /  ___|
     \ `--.   __ _  _ __ ___
      `--. \ / _` || '_ ` _ \
     /\__/ /| (_| || | | | | |
     \____/  \__,_||_| |_| |_|
"""

import random
from datetime import datetime
from time import localtime


def generate_random_date(start_date: tuple,
                         end_date: tuple,
                         sep: str = "-",
                         mkdict: bool = False
                         ) -> tuple[str, dict[str, int]] | str:
    """
    Generate a random date between ``start_date`` and ``end_date``.

    Date formate should be (YYYY, MM, DD).

    You can also specify ``Separator``, (-) is default.

    :param start_date: From where iteration will start.
    :param end_date: Last date to generate.
    :param sep: Separator to separate year, month & day.
    :param mkdict: (Optional) return a dict of time if True.
    :return: Random date in string formate ``YYYY-MM-DD``.
    """

    # Getting year, month & day of Start Date
    s_y = start_date[0]
    s_m = start_date[1]
    s_d = start_date[2]

    # Getting year, month & day of End Date
    e_y = end_date[0]
    e_m = end_date[1]
    e_d = end_date[2]

    # Convert date-time into epoch seconds.
    s_date_sec = int(datetime(s_y, s_m, s_d).timestamp())
    e_date_sec = int(datetime(e_y, e_m, e_d).timestamp())

    # Check if end_date is earlier than start_date
    if s_date_sec > e_date_sec:
        raise ValueError("Start date should be earlier that end date.")

    # Generate random date
    rand_date = localtime(random.randint(s_date_sec, e_date_sec))

    # Get Year, Month & Day of random date
    Y = rand_date.tm_year
    M = rand_date.tm_mon
    D = rand_date.tm_mday

    if len(str(Y)) == 4: Y = f"{Y}"
    if len(str(M)) == 1: M = f"0{M}"
    if len(str(D)) == 1: D = f"0{D}"

    # Create date string
    result = f"{Y}{sep}{M}{sep}{D}"
    result_dict = {
        "Y": Y,
        "M": M,
        "D": D
    }
    if mkdict:
        return result, result_dict
    else:
        return result


def generate_random_time(time_format: str = "24") -> str:
    """
    Generate a random time of day.

    :param time_format: If 12h or 24h.

    :return: Random time as string HH:MM:SS.
    """

    # Generate random Hour, Minute, Second.
    H = random.randint(0, 23)
    M = random.randint(0, 59)
    S = random.randint(0, 59)

    # Check time format
    if time_format == "12":
        H = random.randint(0, 11)

    # Making all double-digit.
    if len(str(H)) == 1: H = f"0{H}"
    if len(str(M)) == 1: M = f"0{M}"
    if len(str(S)) == 1: S = f"0{S}"

    # String format time
    _time = f"{H}:{M}:{S}"
    return _time


if __name__ == "__main__":
    s_date = (2022, 2, 12)  # Starting date of commit   -> (YYYY, MM, DD)
    e_date = (2023, 1, 20)  # Ending date of commit   -> (YYYY, MM, DD)

    date = generate_random_date(s_date, e_date, sep=":")
    time = generate_random_time()

    print(f"Date => {date}")
    print(f"Time => {time}")
