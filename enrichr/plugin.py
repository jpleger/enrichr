#!/usr/bin/env python3
import logging
from inspect import isclass
from functools import wraps
from enrichr import dispatcher
from enrichr import config
from enrichr.datatypes import BaseDataType

plugin_logger = logging.getLogger('enrichr.plugin')

def enrichment(datatype, default=False, bulk=False, *args, **kwargs):
    plugin_logger.debug('enrichment decorator: %s, %s, %s' % (datatype, args, kwargs))
    if not isclass(datatype) or not issubclass(datatype, BaseDataType):
        raise TypeError("@enrichment must be passed a valid datatype (was '%s'), for example @enrichment(IPv4Address)" % datatype)
    def _enrichment_decorator(func):
        # Register the function with the dispatcher
        dispatcher.register_enrichment(func, datatype)
        @wraps(func)
        def _enrichment_wrapped_function(*f_args, **f_kwargs):
            plugin_logger.debug('Function Args/Kwargs: %s, %s' % (f_args, f_kwargs))
            plugin_logger.debug('Parent Args/Kwargs: %s, %s' % (args, kwargs))
            return func(*f_args, **f_kwargs)
        return _enrichment_wrapped_function
    return _enrichment_decorator

def autoload_plugins():
    pass

class Plugin:
    namespace = None
    config = config
    version = None
    plugin_license = None
    maintainer = None
    description = None
    meta = {}  # License, Author, Description, etc.

    def __init_subclass__(cls, /, **kwargs):
        # Register the plugin as being loaded
        dispatcher.register_plugin(cls)
        if hasattr(cls, 'load_plugin'):
            cls.load_plugin()
        super().__init_subclass__()

    @property
    def configured(self):
        missing_attrs = []
        # Check required config
        for attr in ['version', 'license', 'maintainer', 'description']:
            if getattr(self, attr) is not None:
                missing_attrs.append(attr)
        if missing_attrs:
            plugin_logger.critical('Plugin (%s) is not configured correctly, missing: %s' % (self.__qualname__, ','.join(missing_attrs)))
            return False
        # We should use the self.config object to verify that everything is configured for the namespace we are operating in.
        return True
    
    @classmethod
    def load_plugin(cls):
        pass


