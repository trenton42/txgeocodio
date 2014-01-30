===============================
txgeocodio
===============================
An extremely bland Twisted client for http://geocod.io. It's really bland because their api is SO EASY TO USE.

Usage
------
```
import txgeocodio

txgecodio.configure('YOURAPIKEYHERE')

# Geocode some address and get a list of results
d = txgecodio.geocode('123 Main ST, 91702')
# d is a deferred with a list of results

# Parse an address into parts (no geo lookup is made)
d = txgecodio.parse('42370 Bob Hope Dr, Rancho Mirage, CA')
# d is a deferred with the results in a dict that look something like:
{
    "address_components":
        {"number": "42370",
        "street": "Bob Hope",
        "suffix": "Dr",
        "city": "Rancho Mirage",
        "state": "CA"
    },
    "formatted_address": "42370 Bob Hope Dr, Rancho Mirage, CA"
}

```
