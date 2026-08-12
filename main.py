from threading import local
from typing import Optional
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

hotels = [{"id": 1, "title": "Сочи"},{"id": 2, "title": "Дубай"}]


@app.get("/hotels")
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

@app.delete("/hotel/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels=[hotel for hotel in hotels if hotel["id"] != hotel_id]
    
    return {"status": "Ok"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
