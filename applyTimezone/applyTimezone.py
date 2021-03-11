from dateutil.parser import parse


def dt2str(input_datetime):

    offset = input_datetime.utcoffset()

    if offset == None:
        return input_datetime

    out = input_datetime - offset

    return out.strftime("%Y-%m-%d %H:%M:%S.%f")


def dt2dt(input_datetime):

    offset = input_datetime.utcoffset()

    if offset == None:
        return input_datetime

    out = input_datetime - input_datetime.utcoffset()

    return out.replace(tzinfo=None)


def str2str(input_datetime):

    offset = parse(input_datetime).utcoffset()

    if offset == None:
        return input_datetime

    out = parse(input_datetime) - offset

    return out.strftime("%Y-%m-%d %H:%M:%S.%f")


def str2dt(input_datetime):

    offset = parse(input_datetime).utcoffset()

    if offset == None:
        return input_datetime

    out = parse(input_datetime) - offset

    return out.replace(tzinfo=None)
