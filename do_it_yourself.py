import re
device_broken = set()
device_good = set()


log = open('app_2.log').readlines()
matches = list(filter(lambda line: re.search(r'(BIG).*(02)', line), log))
matches_2 = list(filter(lambda line: re.search(r'(BIG).*(DD)', line), log))


for i in matches_2:
    device_broken.add(i.split(';')[2])


for a in matches:
    device_current = a.split(';')[2]
    if device_current not in device_broken:
        device_good.add(device_current)

print("Справних пристроїв:", len(device_good))
print("Бракованих пристроїв:", len(device_broken))