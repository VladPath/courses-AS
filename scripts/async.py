import asyncio
import aiohttp
import threading

async def get_data(i:int,endpoint:str):
    print(f"Начал выполнение: {i}")
    url = f"http://127.0.0.1:8000/{endpoint}/{i}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(f"Закончил выполнение: {i}")


async def run():
    await get_data(1,"async")

    await asyncio.gather(
        *[get_data(i,"sync") for i in range(300)]
    )

    await asyncio.gather(
        *[get_data(i,"async") for i in range(300)]
)

