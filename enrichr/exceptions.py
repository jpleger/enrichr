#!/usr/bin/env python3

class NotConfiguredError(Exception):
    """The requested configuration item has not yet been configured"""
    pass
    
class DuplicatePluginName(Exception):
    """Plugin name isn't unique"""
    pass
