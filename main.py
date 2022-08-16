import aiohttp
import asyncio
import time
import coordinates_generator as cg

start_time = time.time()

point = cg.polygon_random_points(cg.poly, 2000)


async def main():
    for number in range(len(point)-1):
        async with aiohttp.ClientSession() as session:
            headers = {'Content-Type': 'application/json'}
            valhalla = "http://192.168.59.104:31222/route"

            payload = {
                "locations": [
                    {
                        "lat": point[number].x,
                        "lon": point[number].y,
                        "street": "222"
                    },
                    {
                        "lat": point[number + 1].x,
                        "lon": point[number + 1].y,
                        "street": "Veguita"
                    }
                ],
                "costing": "auto",
                "costing_options": {"auto": {"country_crossing_penalty": 2000}},
                "units": "miles",
                "id": "my_work_route"
            }

            async with session.get(url=valhalla, json=payload, headers=headers) as resp:
                response = await resp.json()
                print(response)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
