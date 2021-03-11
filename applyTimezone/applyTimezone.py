from dateutil.parser import parse


def dt2str(datetime_with_timezone):

    out = datetime_with_timezone - datetime_with_timezone.utcoffset()

    return out.strftime("%Y-%m-%d %H:%M:%S.%f")


def dt2dt(datetime_with_timezone):

    out = datetime_with_timezone - datetime_with_timezone.utcoffset()

    return out.replace(tzinfo=None)


def str2str(datetime_string_with_timezone):

    out = parse(datetime_string_with_timezone) - parse(datetime_string_with_timezone).utcoffset()

    return out.strftime("%Y-%m-%d %H:%M:%S.%f")


def str2dt(datetime_string_with_timezone):

    out = parse(datetime_string_with_timezone) - parse(datetime_string_with_timezone).utcoffset()

    return out.replace(tzinfo=None)
