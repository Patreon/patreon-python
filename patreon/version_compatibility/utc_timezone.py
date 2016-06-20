def utc_timezone():
    try:
        # python3
        from datetime import timezone
        return timezone.utc
    except ImportError:
        from datetime import tzinfo, timedelta

        class UTCTimezone(tzinfo):
            def __init__(self):
                pass

            def utcoffset(self, dt):
                return timedelta(0)

            def dst(self, dt):
                return timedelta(0)

            def tzname(self, dt):
                return "UTC"

        return UTCTimezone()
