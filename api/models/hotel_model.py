from pydantic import BaseModel, Field


class Hotel(BaseModel):
    """hotel class model"""

    id: int
    name: str
    phone: int
    stars: int

    class Config:
        from_attributes: True
        validate_all: True


class HotelPayload(BaseModel):
    """hotel model payload"""

    name: str = Field(min_length=5, max_length=127)
    phone: int = Field()
    stars: int = Field()
