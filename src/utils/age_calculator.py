from datetime import datetime as dt
import dateutil.parser as dparser

from logs.logger import Logger


def calculate_age(birth_date: str, logger: Logger = None) -> int:
    if logger:
        logger.info(f"Calculating age for birth date: {birth_date}")
    birth_date_datetime = dparser.parse(birth_date)
    today_datetime = dt.today()
    age = today_datetime.year - birth_date_datetime - ((today_datetime.month, today_datetime.day) < (birth_date_datetime.month, birth_date_datetime.day))
    if logger:
        logger.info(f"Birth date calculated is {age}")
    return age