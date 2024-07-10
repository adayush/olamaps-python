from typing import Union, Optional


async def geocode(self, address: str, bounds: Optional[str] = None):
    """Returns the geocoded address based on the provided parameters"""

    assert len(address), "Address is required"

    address = address.replace(",", " ")

    return await self._request(
        "GET",
        "/places/v1/geocode",
        params={"address": address},
    )


async def reverse_geocode(
    self, lat: Union[str, int, float], lng: Union[str, int, float]
):
    """Provides information of a place based on the location provided satisfying the given criteria"""

    lat = float(lat)
    lng = float(lng)

    assert -90 <= lat <= 90, "Invalid latitude"
    assert -180 <= lng <= 180, "Invalid longitude"

    return await self._request(
        "GET",
        "/places/v1/reverse-geocode",
        params={"latlng": f"{lat},{lng}"},
    )
