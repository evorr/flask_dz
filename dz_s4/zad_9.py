# Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
# файле, название которого соответствует названию изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и
# асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через
# аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.


import asyncio
import aiohttp
import time
import aiofiles
from sys import argv


urls_im = ['https://st.tsum.com/static/verstkaio/50000632-desktop/97d0cd25835c9d6254e0179623c50710.jpg',
        'https://st.tsum.com/static/verstkaio/50000627-desktop/6b46a218b3e1d179f068733adcdd0915_small.jpg',
        'https://www.kit.edu/img/Forschen/CDM-Header-Bild-neu-zugeschnitten_rdax_1634x603s.jpg',
        'https://www.kit.edu/img/Forschen/windrad-004_05.jpg',
        'https://www.kit.edu/img/Forschen/fahrzeug-20190510-CN-20-024.jpg',
        'https://www.kit.edu/img/Forschen/klima-umwelt-20190923-CN-01-001.jpg',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            start_l = time.time()
            if response.status == 200:
                content = await response.read()
                filename = url.split('/')[-1]
                async with aiofiles.open(filename, 'wb') as f:
                    await f.write(content)
                    print(f"Downloaded {filename} in  {time.time() - start_l} seconds")



async def main(urls):
    start_prog = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Program end in  {time.time() - start_prog} seconds")


if __name__ == '__main__':
    #asyncio.run(main(urls_im))
    res = argv
    no, *urls = res
    asyncio.run(main(urls))
# в терминале:
# python zad_9.py https://www.tretyakovgallery.ru/upload/iblock/f2b/x97hpj8ydmqembq3ihtaw9kpvi4fefmj.jpg https://www.tretyakovgallery.ru/upload/iblock/720/44hcp5lmiujrdmg99nz7upr12kqvzbwq.jpg https://www.tretyakovgallery.ru/upload/iblock/ef1/cm3zgwi767sqpknbrtcn6ajor3qsketn.jpg
