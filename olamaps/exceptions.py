class AuthError(Exception):
    """Raised when the user is not authorized to access a resource"""

    def __init__(self, message=None):
        self.message = message or "Check your credentials or billing"
        super().__init__(self.message)


class ClientError(Exception):
    """Raised when there's some problem initialising the client"""


class InvalidRequestError(Exception):
    """Raised when an invalid request is sent"""


class MapsServiceError(Exception):
    """Raised when the server returns an error"""
