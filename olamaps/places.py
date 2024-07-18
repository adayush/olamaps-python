from typing import Optional, Tuple


def autocomplete(
    self,
    text: str,
    location: Optional[str] = None,
    radius: Optional[int] = None,
) -> list:
    """
    Provides Autocomplete suggestions for a given substring satisfying the given criteria

    :param text: The partial text to be matched
    :param location: The point around which to retrieve place information and from which to calculate straight-line distance to the destination. This must be specified as lat,lng.
    :param radius: The distance (in meters) within which to return place results.
    """

    assert len(text), "Text is required"

    params = {"input": text}

    if location:
        params["location"] = location
    if radius:
        params["radius"] = radius
    if location and radius:
        params["strictbounds"] = "true"

    response = self._request(
        "GET",
        "/places/v1/autocomplete",
        params=params,
    )

    return response["predictions"]


async def async_autocomplete(
    self,
    text: str,
    location: Optional[str] = None,
    radius: Optional[int] = None,
) -> list:
    """
    Provides Autocomplete suggestions for a given substring satisfying the given criteria

    :param text: The partial text to be matched
    :param location: The point around which to retrieve place information and from which to calculate straight-line distance to the destination. This must be specified as lat,lng.
    :param radius: The distance (in meters) within which to return place results.
    """

    assert len(text), "Text is required"

    params = {"input": text}

    if location:
        params["location"] = location
    if radius:
        params["radius"] = radius
    if location and radius:
        params["strictbounds"] = "true"

    response = await self._request(
        "GET",
        "/places/v1/autocomplete",
        params,
    )

    return response["predictions"]


def geocode(
    self, address: str, bounds: Optional[Tuple[str, str]] = None
) -> list:
    """
    Returns the geocoded address based on the provided parameters

    :param address: Address to be geocoded
    :param bounds: Tuple of two lat,lng pairs which will be treated as points of a bounding box.
    """

    assert len(address), "Address is required"

    params = {"address": address.replace(",", " ")}
    if bounds:
        params["bounds"] = f"{bounds[0]}|{bounds[1]}"

    response = self._request(
        "GET",
        "/places/v1/geocode",
        params,
    )

    return response["geocodingResults"]


async def async_geocode(
    self, address: str, bounds: Optional[Tuple[str, str]] = None
) -> list:
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


def reverse_geocode(self, lat: str, lng: str) -> list:
    """
    Provides information of a place based on the location provided satisfying the given criteria

    :param lat: Latitude of the location
    :param lng: Longitude of the location
    """

    assert len(lat) and len(lng), "Invalid latitude or longitude provided."

    response = self._request(
        "GET",
        "/places/v1/reverse-geocode",
        params={"latlng": f"{lat},{lng}"},
    )

    return response["results"]


async def async_reverse_geocode(self, lat: str, lng: str) -> list:
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
