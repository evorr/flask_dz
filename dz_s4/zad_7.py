# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000_000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import threading
import multiprocessing
import asyncio
import time

arr = [randint(1, 100) for _ in range(1000000)]


# многопоточность
counter = 0

def another(arr):
    global counter
    for num in arr:
        counter += num


# многопроцессорность
counter_2 = multiprocessing.Value('i', 0)

def increment(cnt, arr):
    for num in arr:
        with cnt.get_lock():
            cnt.value += num


# асинхронность
counter_a = 0

async def sum_num(arr):
    global counter_a
    for num in arr:
        global counter_a
        counter_a += num
    return counter_a

async def main():
    start_3 = time.time()
    await asyncio.gather(sum_num(arr[:50001]), sum_num(arr[50001:]))
    print(f"Async res: {counter_a:_} - {time.time() - start_3}")


if __name__ == '__main__':
    # запуск многопоточного
    threads = []
    for half in [arr[:50001], arr[50001:]]:
        #start_1 = datetime.utcnow()
        start_1 = time.time()
        t = threading.Thread(target=another, args=[half])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Threads res: {counter:_}  - {time.time() - start_1}")
    # запуск многопроцессорного
    processes = []
    for half in [arr[:50001], arr[50001:]]:
        start_2 = time.time()
        p = multiprocessing.Process(target=increment, args=(counter_2, half))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f"Proc res: {counter_2.value:_} - {time.time() - start_2}")
    # запуск асинхронность
    asyncio.run(main())