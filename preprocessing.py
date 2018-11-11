from pprint import pprint

countries = list()
with open("country_latlong.txt") as f:
    f.readline()  # header
    for line in f:
        things = line.strip().split(sep="\t")
        c = things[0]
        countries.append(c)

area_dict = dict()
with open("country_general.txt") as f:
    f.readline()  # header
    for line in f:
        things = line.strip().split(sep="\t")
        c = things[0].strip()
        area = int(things[3].strip())
        area_dict[c] = area

pprint(area_dict)

area_dict["Bosnia and Herzegovina"] = 51129
area_dict["Central African Republic"] = 622984
area_dict["Congo, Dem. Rep."] = 2345410
area_dict["Congo, Rep."] = 342000
area_dict["Gambia"] = 11300
area_dict["Hong Kong, China"] = 1092
area_dict["Korea, Dem. Rep."] = 120540
area_dict["Korea, Rep."] = 98480
area_dict["Montenegro"] = 13812
area_dict["Myanmar"] = 678500
area_dict["Sao Tome and Principe"] = 1001
area_dict["Slovak Republic"] = 48845
area_dict["Trinidad and Tobago"] = 5128
area_dict["West Bank and Gaza"] = 5860 + 360
area_dict["Yemen, Rep."] = 527970

with open("country_area.txt", mode="w") as f:
    f.write("country" + "\t" + "area" + "\n")
    for c in countries:
        area = area_dict.get(c, -1)
        f.write(c + "\t" + str(area) + "\n")