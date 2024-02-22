import json
with open('sample-data.json') as f:
    data = json.load(f)

interface=data['imdata']
print("Interface Status")
print("=" *80)
print("DN                                                 Description           Speed    MTU  ")
print("-" *50, '-'*20, '-'*8, '-'*5)
for x in interface:
    dn = x['l1PhysIf']['attributes']['dn']
    speed = x['l1PhysIf']['attributes']['speed']
    mtu =x ['l1PhysIf']['attributes']['mtu']
    print(f"{dn:<72} inherit   {mtu:<6}")