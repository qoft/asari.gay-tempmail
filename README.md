# [Asari.gay](https://asari.gay) mail wrapper

## Example
```python
import time
import asari.api as asari

client = asari.Api(email='esex')
while True:
    print(client.wait_for_email(_from="bot@fbi.ac"))
    time.sleep(1)
```