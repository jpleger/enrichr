import ipaddress
import logging
from enrichr import dispatcher
datatype_logger = logging.getLogger('enrichr.config')


class BaseDataType:
    _raw = None
    _parsed = None
    regex = None
    defanged_regex = None
    stix_type = None
    metadata = {}
    common_name = None
    
    def __init__(self, data, defanged=False, *args, **kwargs):
        self._raw = data
        self._parsed = data
    
    @property
    def defang(self):
        return str(self._parsed)
    
    def parse(self):
        pass

    def refang(self):
        raise NotImplementedError('Refanging is not implemented for this data type')

    @property
    def is_valid(self):
        return True
    
    def enrich(self, *args, **kwargs):
        datatype_logger.debug(self)
        targets = dispatcher.get_enrichment_targets(self)
        datatype_logger.debug('would target the following enrichments: %s' % targets)

class IPv4Address(BaseDataType):
    regex = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    common_name = 'ip'

    def __init__(self, ip_address):
        self._raw = ip_address
        self.ipv4_address = ipaddress.IPv4Address(ip_address)

    @property
    def defang(self):
        str(self.ipv4_address).replace('.','[.]')

