try:
    # python2
    from urllib import urlencode
except ImportError:
    # python3
    from urllib.parse import urlencode
