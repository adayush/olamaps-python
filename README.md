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

## Usage

- [Installation](#installation)
- [Authentication](#authentication)
- [Client](#client)
- [AsyncClient](#asyncclient)

### Installation

Install the package using pip:

```
pip install olamaps
```

### Authentication

There are two ways to authenticate:

1. Using API key

   ```python
   os.environ["OLAMAPS_API_KEY"] = "your_api_key"

   # OR
   client = Client(api_key="your_api_key")
   ```

2. Or using `client_id` and `client_secret`

   ```python
   os.environ["OLAMAPS_CLIENT_ID"] = "your_client_id"
   os.environ["OLAMAPS_CLIENT_SECRET"] = "your_client_secret"

   # OR
   client = Client(client_id="your_client_id", client_secret="your_client_secret")
   ```

Follow the same steps for AsyncClient as well.

### Client

```python
from olamaps import Client

# Initialize the client
client = Client()

# Autocomplete a query
results = client.autocomplete("Kempe")

# Geocode an address
results = client.geocode("MG Road, Bangalore")

# Reverse geocode a latitude-longitude pair
results = client.reverse_geocode(lat="12.9519408", lng="77.6381845")

# Get directions from one place to another
results = client.directions(
    origin="12.993103152916301,77.54332622119354",
    destination="12.972006793201695,77.5800850011884",
)

# close the client
client.close()
```

Or you can use the context manager, in which case you don't need to close the client manually:

```python
with Client() as client:
    results = client.autocomplete("Kempe")
```

### AsyncClient

Usage is very similar to Client, except that all methods are coroutines:

```python
# use await for all methods
results = await client.autocomplete("Kempe")

# use await for closing the client
await client.close()
```

Also the context manager is async:

```python
async with AsyncClient() as client:
    results = await client.autocomplete("Kempe")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not officially associated with or endorsed by OLA. Use of the OLA Maps API is subject to OLA's terms of service.
