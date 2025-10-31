class SahaRobotikAPIError(Exception):
    """
    Base class for general API errors.
    All custom error classes should inherit from this class.
    """

    def __init__(
        self,
        message: str,
        status_code: int = None,
        response=None,
        url: str = None,
        method: str = None
    ):
        if not message and response is not None:
            try:
                message = response.json().get("error", {}).get("message", "")
            except Exception:
                message = response.text if hasattr(response, "text") else "Invalid Error"

        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response
        self.url = url
        self.method = method

    def __str__(self) -> str:
        parts = [f"[API Error] {self.message}"]
        if self.status_code:
            parts.append(f"(Status Code: {self.status_code})")
        if self.method and self.url:
            parts.append(f"--> {self.method.upper()} {self.url}")
        return " ".join(parts)

    def __repr__(self) -> str:
        return (
            f"<SahaRobotikAPIError status_code={self.status_code} "
            f"method={self.method} url={self.url} message='{self.message}'>"
        )

class BadRequestError(SahaRobotikAPIError):
    """400 Bad Request – The request was invalid or malformed."""
    pass

class UnauthorizedError(SahaRobotikAPIError):
    """401 Unauthorized – Authentication failed or API key is missing."""
    pass

class ForbiddenError(SahaRobotikAPIError):
    """403 Forbidden – The API key does not have access to this resource."""
    pass

class NotFoundError(SahaRobotikAPIError):
    """404 Not Found – The requested resource could not be found."""
    pass

class InternalServerError(SahaRobotikAPIError):
    """500 Internal Server Error – An unexpected error occurred on the server."""
    pass

class CreatedSuccess(SahaRobotikAPIError):
    """201 Created – Resource successfully created. (Usually not raised; informational)"""
    pass

class ServerError(SahaRobotikAPIError):
    """Server error"""
    pass