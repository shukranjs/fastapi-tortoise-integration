from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    """
    Enum representing the possible statuses for MyModel.

    Attributes:
        ACTIVE (str): Represents an active status.
        INACTIVE (str): Represents an inactive status.
        PENDING (str): Represents a pending status.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"


class MyModelIn(BaseModel):
    """
    Pydantic model for MyModel input schema.

    Attributes:
        status (Status): The status of the model.
    """

    status: Status


class MyModelOut(BaseModel):
    """
    Pydantic model for MyModel output schema.

    Attributes:
        id (int): The primary key of the model.
        status (Status): The status of the model.
    """

    id: int
    status: Status

    class Config:
        orm_mode = True
