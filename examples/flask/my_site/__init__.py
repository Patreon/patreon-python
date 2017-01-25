from . import config_defaults

try:
    from . import config
except ImportError:
    class PlainObject(object):
        pass
    config = PlainObject()

for attrname in dir(config_defaults):
    if not hasattr(config, attrname):
        setattr(config, attrname, getattr(config_defaults, attrname))
