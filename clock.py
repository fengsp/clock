# -*- coding: utf-8 -*-
"""
    clock
    ~~~~~

    Simple datetime library.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime, timedelta
import calendar

import pytz
import dateutil
from tzlocal import get_localzone


def utc(*args, **kwargs):
    """Convert to UTC.
    """
    _from_local()
    _from_timestamp()


def _from_local(dt, timezone=None):
    """Convert a local datetime to that datetime in UTC.
    """
    if timezone is not None:
        if dt.tzinfo is not None:
            raise ValueError('Explicit timezone cannot be used with '
                             'timezone-aware datetime')
        if isinstance(timezone, basestring):
            timezone = pytz.timezone(timezone)
        loc_dt = timezone.localize(dt)
    else:
        if dt.tzinfo is None:
            raise ValueError('Explicit timezone required')
        loc_dt = dt
    return loc_dt.astimezone(pytz.utc).replace(tzinfo=None)


def _from_timestamp(timestamp):
    """Convert a POSIX timestamp to the corresponding UTC datetime.
    """
    return datetime.utcfromtimestamp(float(timestamp))


def to(dt, timezone):
    """Convert datetime in UTC to a local datetime(timezone aware).
    """
    if dt.tzinfo is not None:
        raise ValueError('UTC datetime required')
    if isinstance(timezone, basestring):
        timezone = pytz.timezone(timezone)
    return pytz.utc.localize(dt).astimezone(timezone)


def to_timestamp(dt):
    """Convert a datetime to UTC POSIX timestamp."""
    return calendar.timegm(dt.utctimetuple())


def format(dt, timezone, fmt=None):
    """Convert datetime in UTC to a local datetime and show it.
    """
    local = to(dt, timezone)
    if fmt is None:
        return local.isoformat()
    else:
        return local.strftime(fmt)


now  = datetime.utcnow
localtimezone = get_localzone()
