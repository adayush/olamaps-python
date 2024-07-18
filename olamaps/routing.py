from typing import Optional, Literal


def directions(
    self,
    origin: str,
    destination: str,
    waypoints: Optional[list[str]] = None,
    alternatives: Optional[bool] = None,
    steps: Optional[bool] = None,
    overview: Optional[Literal['full', 'simplified', 'false']] = 'full'
) -> list:
    """
    Provides routable path between two or more points. Accepts coordinates in lat,long format.

    :param origin: Origin coordinates in lat,lng format
    :param destination: Destination coordinates in lat,lng format
    :param waypoints: List of coordinates in lat,lng format
    :param alternatives: Whether or not to provide multiple routes
    :param steps: Whether or not to provide steps for the route
    :param overview: Overview geometry either full, simplified or false
    """

    assert len(origin), "Invalid origin coordinates provided."
    assert len(destination), "Invalid destination coordinates provided."

    params = {}

    params["origin"] = origin
    params["destination"] = destination
    if waypoints:
        params["waypoints"] = "|".join(waypoints)
    if alternatives:
        params["alternatives"] = str(alternatives).lower()
    if steps:
        params["steps"] = str(steps).lower()
    if overview:
        params["overview"] = overview
        

    response = self._request(
        "POST",
        "/routing/v1/directions",
        params=params,
    )

    return response["routes"]


async def async_directions(
    self,
    origin: str,
    destination: str,
    waypoints: Optional[list[str]] = None,
    alternatives: Optional[bool] = None,
    steps: Optional[bool] = None,
    overview: Optional[Literal['full', 'simplified', 'false']] = 'full'
) -> list:
    """
    Provides routable path between two or more points. Accepts coordinates in lat,long format.

    :param origin: Origin coordinates in lat,lng format
    :param destination: Destination coordinates in lat,lng format
    :param waypoints: List of coordinates in lat,lng format
    :param alternatives: Whether or not to provide multiple routes
    :param steps: Whether or not to provide steps for the route
    :param overview: Overview geometry either full, simplified or false
    """

    assert len(origin), "Invalid origin coordinates provided."
    assert len(destination), "Invalid destination coordinates provided."

    params = {}

    params["origin"] = origin
    params["destination"] = destination
    if waypoints:
        params["waypoints"] = "|".join(waypoints)
    if alternatives:
        params["alternatives"] = str(alternatives).lower()
    if steps:
        params["steps"] = str(steps).lower()
    if overview:
        params["overview"] = overview

    response = await self._request(
        "POST",
        "/routing/v1/directions",
        params=params,
    )

    return response["routes"]
