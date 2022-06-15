from pydantic import BaseModel


class BaseSchema(BaseModel):
    """A base validation schema of the application."""

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1


class Message(BaseSchema):
    """Payload message of any kind of information or generic errors."""

    detail: str
