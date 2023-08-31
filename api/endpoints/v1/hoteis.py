from fastapi import Depends, HTTPException, FastAPI, Response, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Sequence

from api.core.database import get_db_session
from api.models import hotel_model as models
from api.schemas import hotel_schema as db_models

app = FastAPI()


@app.post('/hotel', status_code=status.HTTP_201_CREATED, response_model=models.Hotel)
async def create_hotel(
        data: models.HotelPayload,
        session: AsyncSession = Depends(get_db_session)
) -> models.Hotel:
    new_hotel = db_models.Hotel(**data.model_dump())
    session.add(new_hotel)
    await session.commit()
    await session.refresh(new_hotel)

    return models.Hotel(id=new_hotel.id, name=new_hotel.name, phone=new_hotel.phone, stars=new_hotel.stars)


@app.get('/hotel', status_code=status.HTTP_200_OK, response_model=Sequence[models.Hotel])
async def get_all_hotel(
        session: AsyncSession = Depends(get_db_session)
) -> Sequence[models.Hotel]:
    db_hotel = await session.execute(select(db_models.Hotel))
    all_hotel: Sequence[models.Hotel] = db_hotel.scalars().all()
    return all_hotel


@app.get('/hotel/{hotel_id}', status_code=status.HTTP_200_OK, response_model=models.Hotel)
async def get_hotel_by_id(
        hotel_id: int,
        session: AsyncSession = Depends(get_db_session)
) -> models.Hotel:
    hotel = await session.get(db_models.Hotel, hotel_id)

    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not Found")

    return models.Hotel(
        id=hotel.id, name=hotel.name, phone=hotel.phone, stars=hotel.stars
    )


@app.get('/hotel/{name}', status_code=status.HTTP_200_OK, response_model=Sequence[models.Hotel])
async def get_hotel_by_name(
        name: str,
        session: AsyncSession = Depends(get_db_session)
) -> Sequence[models.Hotel]:
    query = select(db_models.Hotel).filter(db_models.Hotel.name.like(f'%{name}%'))
    result = await session.execute(query)
    hotel: Sequence[models.Hotel] = result.scalars().all()

    if hotel:
        return hotel
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no hotel with that name found")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("hoteis:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
