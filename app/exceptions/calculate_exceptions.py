from typing import Optional
from fastapi import HTTPException, status


class BadRequestError(HTTPException):
    def __init__(
        self,
        detail: any = None,
        headers: Optional[dict[str, any]] = None,
    ):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            headers=headers,
        )
