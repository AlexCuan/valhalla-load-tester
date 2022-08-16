# valhalla-load-tester
Simple script that uses random coordinates within a specific polygon on a map and performs a large number of requests.

## How to use
Install depeendencies.

Go to http://apps.headwallphotonics.com/ and choose a set of coordinates that encloses your desired work area.
![imagen](https://user-images.githubusercontent.com/77734898/185000579-32a37e12-1492-40e4-8291-4d1fcd0469ac.png)

Enter a set of coordinates on the **coordinates_generator.py** file as you can see below: 
```
poly = Polygon([(23.109168639786912, -82.38050743782621), (23.08137764519128, -82.38977715218168),
                (23.0954317643179, -82.34600350105863), (23.112326343560625, -82.35750481331449)])
```

Change the number of asynchronous requests you want to perform (2000 in my case):
```
point = cg.polygon_random_points(cg.poly, 2000)
```

Change Valhalla's server endpoint you want to test:
```
valhalla = "http://192.168.59.104:31222/route"
```

### Articles used to make this script
- https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
- https://medium.com/the-data-journal/a-quick-trick-to-create-random-lat-long-coordinates-in-python-within-a-defined-polygon-e8997f05123a
