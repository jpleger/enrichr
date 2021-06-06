#!/usr/bin/env python3
from enrichr import config
from enrichr.exceptions import DuplicatePluginName
import logging

dispatch_logger = logging.getLogger('enrichr.dispatch')


class Dispatcher:
    _plugins = {}
    _enrichments = {}
    _default_enrichments = {}


    def register_plugin(self, plugin):
        plugin_name = plugin.__name__
        dispatch_logger.debug('Attempting to register plugin: %s' % plugin)
        if plugin_name not in self._plugins or config.FORCE_PLUGIN_REGISTRATION:
            dispatch_logger.debug('New registration of plugin: %s' % plugin)
            self._plugins[plugin_name] = plugin
        elif plugin_name in self._plugins and plugin is not self._plugins[plugin_name]:
            raise DuplicatePluginName('Plugin name collision')
        return True

    def register_enrichment(self, func, datatype):
        dispatch_logger.debug('Attempting to register the enrichment: %s for %s' % (func, datatype))
        return True
    
    def get_enrichment_targets(self, datatype):
        if datatype in self._enrichments:
            return self._enrichments[datatype]
    
    def reset(self):
        self._plugins = {}
        self._enrichments = {}

