from fastapi import FastAPI, Query, Body, APIRouter
import time
import asyncio
import threading

router = APIRouter(prefix="/hotels", tags=["Отели"])


hotels = [
    {"id": 1, "title": "Сочи", "name": "Отель в Сочи"},
    {"id": 2, "title": "Дубай", "name": "Отель в Дубай"},
]



@router.get("/hotels",summary="Получение списка отеля из БД", description="С помощью этого ендпоинта можно получить список отелей с фильтрами")
def get_hotels(
    id: int | None = Query(default =None, description="Айди отеля"),
    title: str | None = Query(default= None, description="Название отеля")
 ):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] == id:
            hotels_.append(hotel)
        if title and hotel["title"] == title:
            hotels_.append(hotel)
        else:
            return hotels
    return hotels_

@router.post("/hotels",summary="Добавление отеля в массив БД", description="С помощью ендпоинта можно добавить новый отель")
def create_hotel(
    title:str = Body(embed=True)
):
    
    global hotels
    hotels.append({
        "id" : hotels[-1]["id"]+1,
        "title" : title
    })
    return {"status": "Ok"}



@router.put("/hotel/{id}",summary="Полное бновление данных об отелях",description="Тут мы обновляем данные об отеле!")
def edit_hotel(
    id:int,
    title: str =  Body(title="Название отеля"),
    name: str = Body(title="Описание отеля"),
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == id][0]

    hotel["title"] = title
    hotel["name"] = name

    return {"status": "Ok"}

@router.patch("/hotel/{id}",summary="Частичное бновление данных об отелях",description="Тут мы обновляем частитчно данные об отеле!")
def part_hotel(
    id:int,
    title:str|None = Body(None,title="Название отеля"),
    name: str|None = Body(None,title="Описание отеля"),
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == id][0]

    if hotel["id"]==id:
        if title: hotel["title"] = title
        if name: hotel["name"] = name

    return {"status": "Ok"} 


@router.delete("/hotel/{id}",summary="Удаление отеля",description="Удаление отеля из массива!")
def delete_hotel(id: int): 
    global hotels
    hotels=[hotel for hotel in hotels if hotel["id"] != id]
    
    return {"status": "Ok"}

@router.get("/sync/{id}")
def sync_func(id:int):
    print(f"sync. Потоков: {threading.active_count()}")
    print(f"sync. Начал {id}: {time.time():.2f}")
    time.sleep(3)
    print(f"sync. Закончил{id}: {time.time():.2f}")

@router.get("/async/{id}")
async def async_func(id:int):

    print(f"sync. Потоков: {threading.active_count()}")
    print(f"sync. Начал {id}: {time.time():.2f}")
    await asyncio.sleep(3)
    print(f"sync. Начал {id}: {time.time():.2f}")

