places=[(3,4),(9,0),(10,6)]

me={"NAME":"John Wiech",
    "HEIGHT":(5,11),
    "WEIGHT":160,
    "COLOR":"Green"}

x=input("What would you like to know about me?: ")
if x in me:
    info=me[x]
    print(info)
else:
    print("not found")

music={"musician1":["song1","song2","song3"],
       "musician2":["song3","song4"],
       "musician3":["song6","song7"]}
