from typing import Optional, Any


async def directions(
    self,
    origin: str,
    destination: str,
    waypoints: Optional[list[str]] = None,
    alternatives: Optional[bool] = None,
    steps: Optional[bool] = None,
):
    """
    Provides routable path between two or more points. Accepts coordinates in lat,long format.

    :param origin: Origin coordinates in lat,lng format
    :param destination: Destination coordinates in lat,lng format
    """

    assert len(origin), "Invalid origin coordinates provided"
    assert len(destination), "Invalid destination coordinates provided"

    params = {}

    params["origin"] = origin
    params["destination"] = destination
    if waypoints:
        params["waypoints"] = "|".join(waypoints)
    if alternatives:
        params["alternatives"] = str(alternatives).lower()
    if steps:
        params["steps"] = str(steps).lower()

    return await self._request(
        "POST",
        "/routing/v1/directions",
        params=params,
    )
