import re
import os
import logging
from enrichr.exceptions import NotConfiguredError

ENV_PREFIX = 'ENRICHR'
ENRICHR_NAMESPACE = 'ENRICHR'
ATTR_DELIMETER = '__'
config_logger = logging.getLogger('enrichr.config')


def valid_name(name):
    # Starts with a letter, and contains uppercase, numbers or _
    name_re = re.compile(r'^[A-Z][A-Z0-9_]*$')
    if name_re.match(name):
        return True
    else:
        return False

class Configuration(object):
    _config_values = {}
    _masked_values = []
    
    @classmethod
    def register_option(cls, option):
        # When we register options, we need to ensure that:
        #   - the objects namespace and name is present
        #   - The option is a ConfigOption
        if not isinstance(option, ConfigOption):
            raise Exception('ConfigOption is not a valid config.ConfigOption')
        # If the option exists, then update with the new option
        if hasattr(cls, option.attr_name):
            object.__getattribute__(cls, option.attr_name).update(option)
            return True
        setattr(cls, option.attr_name, option)
        return True

    @classmethod
    def mask_value(cls, value):
        # This is used for hiding sensitive fields from logging
        if value not in cls._masked_values:
            cls._masked_values.append(value)


class ConfigOption:
    _registered = False
    def __init__(self, name=None, namespace=None, default=None, env_var=None, help_text=None, mask=False, order=0, required=False, **kwargs):
        if name:
            name = name.upper()
            if not valid_name(name):
                raise ValueError("ConfigOption 'name' (%s) must start with a letter and only contain letters, numbers and underscores (_)" % name)
        self.name = name
        if namespace:
            namespace = namespace.upper()
            if not valid_name(namespace):
                raise ValueError("ConfigOption 'namespace' (%s) must start with a letter and only contain letters, numbers and underscores (_)" % namespace)
        self.namespace = namespace
        if required and default:
            raise ValueError("ConfigOption arguments 'required' (%s) and 'default' (%s) cannot both be set" % (repr(required), repr(default)))
        self.required = required
        self.default = default
        self._env_var = env_var
        self.help_text = help_text
        self.mask = mask
        self.order = order
        # Hit the registered property in case we have everything thats needed
        self.register()
        return
    
    def register(self):
        if self._registered:
            return True
        if self.namespace and self.name:
            Configuration.register_option(self)
            self._registered = True
            return True
        return False

    def update(self, option):
        option_attrs = vars(option)
        for attr_name, value in option_attrs.items():
            if value is not None:
                setattr(self, attr_name, value)

    @property
    def attr_name(self):
        if self.namespace == ENRICHR_NAMESPACE:
            return self.name
        return self.namespace + ATTR_DELIMETER + self.name

    @property
    def env_var(self):
        if self._env_var:
            return self._env_var
        return ENV_PREFIX + ATTR_DELIMETER + self.attr_name

    def __set_name__(self, obj, name):
        # If the namespace hasn't been defined, get the namespace from the object which is is defining the ConfigOption
        if not self.namespace:
            # If the object that is using the ConfigurationOption has a namespace attribute set, then use that as the namespace
            if hasattr(obj, 'namespace') and obj.namespace:
                self.namespace = obj.namespace.upper()
            # Otherwise, we will set the namespace to be the class name of the object defining the ConfigOption
            else:
                self.namespace = obj.__name__.upper()
        # If there isn't a name defined, get it from the name of the variable that ConfigObject is being set to
        if not self.name:
            self.name = name.upper()
        # Register the configuration option with the Configuration class if we haven't already
        self.register()

    def __get__(self, obj, objtype=None):
        # If we aren't working within an instance and it is a Configuration object, allow it to be worked with directly.
        if obj is None and objtype is Configuration:
            return self
        # Before we do anything, make sure the descriptor is registered
        if not self.register():
            raise AttributeError("Both the 'name' (%s) and 'namespace' (%s) are required in ConfigOption before using '__get__'" % (self.name, self.namespace))
        if hasattr(obj, '_config_values') and self.attr_name in obj._config_values:
            return obj._config_values[self.attr_name]
        # This is typically a plugin that has a .config attribute, we will verify there is a ._config_values in there and grab that if it exists.
        if hasattr(obj, 'config') and hasattr(obj.config, '_config_values') and self.attr_name in obj.config._config_values:
            return obj.config._config_values[self.attr_name]
        # If we have an environmental variable, then use that
        if self.env_var in os.environ:
            return os.environ[self.env_var]
        # If the option is required, we need to raise an exception
        if self.required:
            raise NotConfiguredError("A required configuration item has not been set for 'config.%s'" % self.attr_name)
        # Just return the default value
        return self.default

    def __set__(self, obj, value):
        # Before we do anything, make sure the descriptor is registered
        if not self.register():
            raise AttributeError("Both the 'name' (%s) and 'namespace' (%s) are required in ConfigOption before using '__set__'" % (self.name, self.namespace))
        # If the ConfigurationOption is supposed to be masked (for example in logs) use the Configuration.mask_values to add it to our global masks
        if self.mask:
            Configuration.mask_value(value)
        # We will always set the value to the objects obj._config_value.
        if not hasattr(obj, '_config_values'):
            obj._config_values = {}
        obj._config_values[self.attr_name] = value
        

