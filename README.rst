Welcome to Clock
================

Clock is a nice datetime practice.

Guideline
---------

**Always handle time in UTC.**

Installation
------------

::
    
    $ pip install clock

Usage
-----

::
    
    import clock

    # Internally always use UTC, convert everything else to UTC
    # before manipulate or save datetime
    ## get current UTC datetime
    clock.utc()

    ## get one timestamp in UTC
    utc_dt = clock.utc(1400639252.963287)
    clock.utc(1400639252)
    clock.utc('1400639252.963287')
    clock.utc('1400639252')
    
    ## get one local datetime in UTC
    clock.utc(clock.datetime(2014, 5, 12, 11, 11, 11), clock.localtimezone)
    clock.utc(clock.datetime(2014, 5, 12, 11, 11, 11), 'US/Pacific')
    ## cannot use explicit timezone with timezone-aware datetime both
    clock.utc(clock.datetime.now().replace(tzinfo=clock.localtimezone))
    

    # Interfacing with the user, convert to local time
    local_dt = clock.local(utc_dt, clock.localtimezone)
    clock.local(utc_dt, 'US/Pacific')
    ## convert to POSIX timestamp
    clock.to_timestamp(utc_dt)
    ## then format it and show it to user
    >>> local_dt.strftime('%Y-%m-%d %H:%M:%S')
    '2014-05-21 10:27:32'
    ## actually clock comes with one shortcut for this, pass UTC datetime
    ## in and get local datetime format
    >>> clock.format(utc_dt, clock.localtimezone, '%Y-%m-%d %H:%M:%S')
    '2014-05-21 10:27:32'


    # utcnow and timedelta
    >>> clock.now()
    datetime.datetime(2014, 5, 21, 3, 27, 26, 580031)
    >>> clock.timedelta(days=1)
    datetime.timedelta(1)
    

    # get local timezone
    >>> clock.localtimezone
    <DstTzInfo 'Asia/Harbin' LMT+8:27:00 STD>

Better
------

If you feel anything wrong, feedbacks or pull requests are welcomed.
