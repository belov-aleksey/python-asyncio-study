# Шпаргалка по asyncio
# asyncio - асинхронное выполнение; подходит для IO-bound задач. 
# Работает ровно 1 поток

# Плюсы:
# + скорость и экномия времени, вместо x + y + z -> max(x, y, z)


# 1) корутина работает как генератор
# 2) async - явный флаг, что данная функция является асинхронной (корутиной)
# 3) await - явный флаг, что в этом месте функция встает на паузу и дает работать другим, пока ждет свои данные
# 4) event loop - цикл событий. Механизм, который отвечает за планирование и запуск корутин.abs
#    Можно представить как список/очередь, из которого в вечном цикле достаются и запускаются корутины

# Часты ошибки:
# 1. не использование async внутри корутины
# 2. создание корутины, но использование ее как функции
# 2. использование внутри корутины синхронного (блокирующего кода)

import time
import asyncio

def task1():
    print("Run task1...")
    time.sleep(1)
    print("Stop task1!")

def task2():
    print("Run task2...")
    time.sleep(2)
    print("Stop task2!") 

def task3():
    print("Run task3...")
    time.sleep(3)
    print("Stop task3!")    

def run_synch_sleep():
    current_time = time.time()
    task1()
    task2()
    task3()
    print(f"{time.time()-current_time}")


async def async_task1():
    print("Run task1...")
    await asyncio.sleep(1)
    print("Stop task1!")

async def async_task2():
    print("Run task2...")
    await asyncio.sleep(2)
    print("Stop task2!") 

async def async_task3():
    print("Run task3...")
    await asyncio.sleep(3)
    print("Stop task3!")    

async def run_asynch_sleep():
    current_time = time.time()

    # Способ 1 создания event loop'а
    # asyncio.create_task(async_task1())
    # asyncio.create_task(async_task2())
    # await asyncio.create_task(async_task3())

    # Способ 2 создания event loop'а
    await asyncio.gather(
        async_task1(), 
        async_task2(), 
        async_task3()
    )

    print(f"{time.time() - current_time}")


if __name__ == "__main__":
    # run_synch_sleep()
    asyncio.run(run_asynch_sleep())