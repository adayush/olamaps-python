from typing import Union, Optional, Tuple


async def geocode(self, address: str, bounds: Optional[Tuple[str, str]] = None) -> list:
    """
    Returns the geocoded address based on the provided parameters

    :param address: Address to be geocoded
    :param bounds: Tuple of two lat,lng pairs which will be treated as points of a bounding box.
    """

    assert len(address), "Address is required"

    params = {
        "address": address.replace(",", " "),
    }
    if bounds:
        params["bounds"] = f"{bounds[0]}|{bounds[1]}"

    response = await self._request(
        "GET",
        "/places/v1/geocode",
        params=params,
    )

    return response["geocodingResults"]


async def reverse_geocode(self, lat: str, lng: str) -> list:
    """
    Provides information of a place based on the location provided satisfying the given criteria

    :param lat: Latitude of the location
    :param lng: Longitude of the location
    """

    assert len(lat) and len(lng), "Invalid latitude or longitude provided."

    response = await self._request(
        "GET",
        "/places/v1/reverse-geocode",
        params={"latlng": f"{lat},{lng}"},
    )

    return response["results"]
