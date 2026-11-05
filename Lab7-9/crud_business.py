from time import strftime, gmtime


def valid_date(input_date, other_date = None, finish_date = None):
    """
    Returns a tuple with a bool and a feedback, indicating the validness of the input_date
    :param input_date: str
    :param other_date: str | None
    :param finish_date: str | None
    :return: str
    """

    if not input_date or len(input_date.split("/")) != 3:
        return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

    input_day, input_month, input_year = input_date.split("/")
    current_day, current_month, current_year = strftime("%d/%m/%Y", gmtime()).split("/")

    if not input_day.isdigit() or not input_month.isdigit() or not input_year.isdigit() or len(input_day) != 2 or len(input_month) != 2 or len(input_year) != 4:
        return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"


    input_day = int(input_day)
    input_month = int(input_month)
    input_year = int(input_year)

    current_day = int(current_day)
    current_month = int(current_month)
    current_year = int(current_year)

    if input_day > 31 or input_month > 13:
        return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

    if current_year > input_year:
        return False, "be after the current date"
    elif current_year == input_year:
        if current_month > input_month:
            return False, "be after the current date"
        elif current_month == input_month:
            if current_day > input_day:
                return False, "be after the current date"

    return True, ""

def get_id():
    current_day, current_month, current_year = strftime("%d/%m/%Y", gmtime()).split("/")
    current_hour, current_minutes, current_second = strftime("%H/%M/%S", gmtime()).split("/")
    return "".join([current_day, current_month, current_year, current_hour, current_minutes, current_second])
