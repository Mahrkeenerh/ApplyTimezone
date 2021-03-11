from dateutil.parser import parse


def outputString(datetime_with_timezone):

    out = datetime_with_timezone - datetime_with_timezone.utcoffset()

    return out.strftime("%Y-%m-%d %H:%M:%S.%f")


def outputDatetime(datetime_with_timezone):

    out = datetime_with_timezone - datetime_with_timezone.utcoffset()

    return out.replace(tzinfo=None)
