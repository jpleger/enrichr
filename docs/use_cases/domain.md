# Domain Use Cases

```python
domain = Domain('enrichr.io')
fqdn = FQDN('the.enrichr.io')

fqdn.domain  # <Domain('enrichr.io')>
domain in fqdn  # True
```

## DNS Record Examples

```python
# thurr be dragons here.
question = FQDN('test4.enrichr.io')
fqdn = FQDN('test2.enrichr.io')
ip1  = IPv4Address('1.2.3.4')
ip2 = IPv4Address('2.3.4.5')
ip3 = IPv4Address('3.4.5.6')

a = DNSRecord(record_type='SOA', data='enrichr.io. dns.sheeple.us. 2 3600 600 604800 1800')
b = DNSARecord(ip1)
c = DNSCNAMERecord(fqdn)
d = DNSARecord(ip2)
response = DNSResponse(
    answer=[a,b,c],
    additional=[d],
    question=question,
    question_type='ANY',
    status='NOERR'
)

ip1 in response  # True
ip2 in response  # True -- from the additional
ip3 in response  # False

```
