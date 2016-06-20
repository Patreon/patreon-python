def utc_timezone():
    try:
        # python3
        from datetime import timezone
        return timezone.utc
    except ImportError:
        from datetime import tzinfo, timedelta
        class UTCTimezone(tzinfo):
            def utcoffset(self, dt):
                return timedelta(0)
            def dst(self, dt):
                return timedelta(0)
        return UTCTimezone()
