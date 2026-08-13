import asyncio
import time

# IO bound

async def make_db_call():
    await asyncio.sleep(1)


async def make_api_request():
    await asyncio.sleep(2)

# В Аснхронных же при использовании gather мы суммируем выполнение функций 
# в конкурентное выполнение асинх функций
async def main():
    start_time = time.perf_counter()

    await asyncio.gather(make_db_call(), make_api_request())
 
    finish_time = time.perf_counter()
    print(f"Времени прошло: {finish_time-start_time}")

if __name__ == '__main__':
    asyncio.run(main())