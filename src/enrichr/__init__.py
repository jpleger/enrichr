import logging
from logging import NullHandler
logging.getLogger(__name__).addHandler(NullHandler())

from enrichr.config import Configuration, ConfigOption
from enrichr.dispatch import Dispatcher


__VERSION__ = '0.0.4'

# Setup our global objects
dispatcher = Dispatcher()
config = Configuration()

# Define the global framework config options
Configuration.DEBUG = ConfigOption(name='debug', namespace='enrichr', default=False, help_text='Enable Debug Mode')
Configuration.LOGLEVEL = ConfigOption(name='loglevel', namespace='enrichr', default='CRITICAL', help_text='Log Level for Python Logging (defaults to Critical)')
Configuration.FORCE_PLUGIN_REGISTRATION = ConfigOption(
    name='force_plugin_registration',
    namespace='enrichr',
    default=False,
    help_text='Force Registration of Plugins (ignore namespace collisions)'
)

