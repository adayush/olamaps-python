# OLA Maps Python Package (unofficial)

A Python wrapper for the OLA Maps API, providing easy-to-use abstractions for developers.

## Installation

Install the package using pip:

```
pip install olamaps
```

## Supported APIs

- Geocoding
- Reverse geocoding

## Future Plans

- Directions

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

# Geocode an address
results = client.geocode("MG Road, Bangalore")

# Reverse geocode a latitude-longitude pair
results = client.reverse_geocode(lat=12.9519408, lng=77.6381845)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not officially associated with or endorsed by OLA. Use of the OLA Maps API is subject to OLA's terms of service.
