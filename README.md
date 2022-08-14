# [Asari.gay](https://asari.gay) tempmail wrapper

## Example
```python
import time
import asari.api as asari

client = asari.Api(email='email_name')
while True:
    print(client.wait_for_email(_from="noreply@discord.com"))
    time.sleep(1)
```

## Known domains
  - goon.bar
  - guilded.lol
  - selfbot.cc
  
## Add your own domain
- Contact `dropoutuwu` on telegram todo so.
