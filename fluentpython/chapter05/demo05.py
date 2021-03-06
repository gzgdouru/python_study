'''
operator模块
'''
from operator import mul, itemgetter, attrgetter, methodcaller
from functools import reduce
from collections import namedtuple


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


if __name__ == "__main__":
    # print(fact(5))
    # print(reduce(mul, range(1, 6)))

    metro_data = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delgi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833))
    ]

    # for city in sorted(metro_data, key=itemgetter(1)):
    #     print(city)

    # cc_name = itemgetter(1, 0)
    # for city in metro_data:
    #     print(cc_name(city))

    # LatLong = namedtuple("LatLong", "lat long")
    # Metropolis = namedtuple("Metropolis", "name cc pop coord")
    # metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    # print(metro_areas[0].coord.lat)
    # name_lat = attrgetter("name", "coord.lat")
    # for city in sorted(metro_areas, key=attrgetter("coord.lat")):
    #     print(name_lat(city))

    s = "The time has come"
    upcase = methodcaller("upper")
    print(upcase(s))
    hiphenate = methodcaller("replace", " ", "-")
    print(hiphenate(s))
