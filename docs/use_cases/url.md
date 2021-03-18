# URL Use Case

```python

url = URL('https://the.enrichr.io/spiffy/malware.exe?passcode=abc123')
url.scheme == 'https'  # True
url.domain  # <Domain('enrichr.io')>
url.fqdn  #  <FQDN('the.enrichr.io')>
url.directory  # <Directory('/spiffy')>
url.filename  # <Filename('malware.exe')>
url.path # <Path('/spiffy/malware.exe')>

# Advanced Use Cases
Filename('malware.exe') in url  # True
```
