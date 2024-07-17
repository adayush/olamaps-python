# OLA Maps Python Package

A Python wrapper for the OLA Maps API, providing easy-to-use abstractions for developers.

[![Stable Version](https://img.shields.io/pypi/v/olamaps?label=stable)](https://pypi.org/project/olamaps/)
![Python Versions](https://img.shields.io/pypi/pyversions/olamaps)
[![Download Stats](https://img.shields.io/pypi/dm/olamaps)](https://pypistats.org/packages/olamaps)

## Supported APIs

- Autocomplete
- Geocoding
- Reverse geocoding
- Directions

## Installation

Install the package using pip:

```
pip install olamaps
```

## Authentication

There are two ways to authenticate:

1. Using API key

   ```python
   os.environ["OLAMAPS_API_KEY"] = "your_api_key"

   # OR
   client = Client(api_key="your_api_key_here")
   ```

2. Or using `client_id` and `client_secret`

   ```python
   os.environ["OLAMAPS_CLIENT_ID"] = "your_client_id"
   os.environ["OLAMAPS_CLIENT_SECRET"] = "your_client_secret"

   # OR
   client = Client(client_id="your_client_id", client_secret="your_client_secret")
   ```

## Usage

```python
import os
from olamaps import Client

# Initialize the client
client = Client()

# Autocomplete a query
results = await client.autocomplete("Kempe")

# Geocode an address
results = await client.geocode("MG Road, Bangalore")

# Reverse geocode a latitude-longitude pair
results = await client.reverse_geocode(lat="12.9519408", lng="77.6381845")

# Get directions from one place to another
results = await client.directions(
    origin="12.993103152916301,77.54332622119354",
    destination="12.972006793201695,77.5800850011884",
)

# close the client
await client.close()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not officially associated with or endorsed by OLA. Use of the OLA Maps API is subject to OLA's terms of service.
