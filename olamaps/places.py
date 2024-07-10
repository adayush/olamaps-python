from typing import Union, Optional, Tuple


async def geocode(self, address: str, bounds: Optional[Tuple[str, str]] = None):
    """Returns the geocoded address based on the provided parameters"""

    assert len(address), "Address is required"

    params = {
        "address": address.replace(",", " "),
    }
    if bounds:
        params["bounds"] = f"{bounds[0]}|{bounds[1]}"

    return await self._request(
        "GET",
        "/places/v1/geocode",
        params=params,
    )


async def reverse_geocode(self, lat: str, lng: str):
    """Provides information of a place based on the location provided satisfying the given criteria"""

    assert len(lat) and len(lng), "Invalid latitude or longitude provided"

    return await self._request(
        "GET",
        "/places/v1/reverse-geocode",
        params={"latlng": f"{lat},{lng}"},
    )
