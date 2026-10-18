from typing import Annotated

from fastapi import Body, Depends, Query, APIRouter
from src.schemas.hotels import Hotel, HotelPatch
from src.api.dependencies import PaginationDep

router = APIRouter(prefix="/hotels", tags=["Отели"])


hotels = [
    {"id": 1, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 2, "title": "Дубай", "name": "Отель в Дубай"},
    {"id": 3, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 4, "title": "Дубай", "name": "Отель в Дубай"},
    {"id": 5, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 6, "title": "Дубай", "name": "Отель в Дубай"},
    {"id": 7, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 8, "title": "Дубай", "name": "Отель в Дубай"},
    {"id": 9, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 10, "title": "Дубай", "name": "Отель в Дубай"},
    {"id": 11, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 12, "title": "Дубай", "name": "Отель в Дубай"},
    {"id": 13, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 14, "title": "Дубай", "name": "Отель в Дубай"},
]

# Примеры создания отелей
create_hotels_examples_={
    "1":{"summary":"Сочи", "value":{"title": "Сочи 5 звезд","name": "Sochi_5_stars"}},
    "2":{"summary":"Дубай", "value":{"title": "Дубай 5 звезд","name": "Dubai_5_stars"}}}

@router.get("/hotels",summary="Получение списка отеля из БД", description="С помощью этого ендпоинта можно получить список отелей с фильтрами")
def get_hotels(
   pagination: PaginationDep,
    id: int | None = Query(default =None, description="Айди отеля"),
    title: str | None = Query(default= None, description="Название отеля"),
 ):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] == id:
            hotels_.append(hotel)
        if title and hotel["title"] == title:
            hotels_.append(hotel)
        if not id and not title:
            offset = pagination.per_page * (pagination.page-1)
            return hotels[offset:offset+pagination.per_page]
            # return hotels[((pagination.page-1)*pagination.per_page):][:pagination.per_page]
    offset = pagination.per_page * (pagination.page-1)
    return hotels_[offset:offset+pagination.per_page]
    # return hotels_[((pagination.page-1)*pagination.per_page) : pagination.per_page*pagination.page]


@router.post("/hotels",summary="Добавление отеля в массив БД", description="С помощью ендпоинта можно добавить новый отель")
def create_hotel(
    hotel_data:Hotel = Body(openapi_examples=create_hotels_examples_) # type: ignore
):
    
    global hotels
    hotels.append({
        "id" : hotels[-1]["id"]+1,
        "title" : hotel_data.title,
        "name" : hotel_data.name
    })
    return {"status": "Ok"}


@router.put("/hotel/{id}",summary="Полное бновление данных об отелях",description="Тут мы обновляем данные об отеле!")
def edit_hotel(id:int,hotel_data:Hotel):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == id][0]

    hotel["title"] = hotel_data.title
    hotel["name"] = hotel_data.name

    return {"status": "Ok"}


@router.patch("/hotel/{id}",summary="Частичное бновление данных об отелях",description="Тут мы обновляем частитчно данные об отеле!")
def part_hotel(id:int, hotel_data:HotelPatch):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == id][0]

    if hotel["id"]==id:
        if hotel_data.title: hotel["title"] = hotel_data.title
        if hotel_data.name: hotel["name"] = hotel_data.name

    return {"status": "Ok"} 


@router.delete("/hotel/{id}",summary="Удаление отеля",description="Удаление отеля из массива!")
def delete_hotel(id: int): 
    global hotels
    hotels=[hotel for hotel in hotels if hotel["id"] != id]
    
    return {"status": "Ok"}

