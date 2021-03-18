# IP Address Use Case

```python
ip = IPAddress('1.2.3.4')
ip.valid  # Check for validity, returns True
ip.defang  # Obfuscate the IP, Returns 1[.]2[.]3[.]4
ip.regex  # Returns RE for finding this data type
ip.enrich()

# Basic use cases
ip.enrich(disable_plugins=['PassiveTotal'])  # Disable certain plugins
ip.enrich(extra_plugins=['SpiffyPlugin'])  # Add a non-default plugins
ip.enrich(only_plugins=['PluginName'])  # Only run a specific plugins
ip.enrich(remote_plugins=False)  # Don't run any plugins that require network access
int(ip)  #  16909060

# Advanced use cases:

# run an enrichment with PassiveTotal and SpiffyPlugin, passing optional arguments to each plugin.
ip.enrich(
    only_plugins=['PassiveTotal', 'SpiffyPlugin'],
    passivetotal_extended_results=True,
    spiffyplugin_extra_option='Everything!'
)
# PassiveTotalPlugin().enrich_ip(IPAddress('1.2.3.4'), extended_results=True)
# SpiffyPlugin().enrich_ip(IPAddress('1.2.3.4'), extra_option=True)


# check to see if the ip is in a network block
network = IPv4Network('1.0.0.0/8')
ip in network  # Returns True
```

IP Address Example (this also has v6) using ipaddress.

```python
import ipaddress
ip = ipaddress.IPv4Address('1.2.3.4')
ip2 = ipaddress.IPv4Address('2.3.4.5')
ipnet = ipaddress.IPv4Network('1.0.0.0/8')
ip in ipnet    # True
ip2 in ipnet  # False
```
