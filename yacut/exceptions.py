from http import HTTPStatus
from typing import Dict


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, msg, status_code=None) -> None:
        super().__init__()
        self.msg = msg
        if status_code is not None:
            self.status_code = status_code

    def to_representation(self) -> Dict[str, str]:
        return dict(message=self.msg)