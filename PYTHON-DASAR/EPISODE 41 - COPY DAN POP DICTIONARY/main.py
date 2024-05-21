# copy dictionary

teman_teman = {
    "ucup": "ucup surucup",
    "otong": "surotong",
    "dudung": "surudung",
    "sep": "si asep",
    "cuy": "ucuy",
}

friends = teman_teman.copy()

print(f"teman-teman = {teman_teman}")
print(f"friends = {friends}\n")

teman_teman["ucup"] = "ucup si keren"
print(f"teman-teman = {teman_teman}")
print(f"friends = {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")  # transfer data dari friens ke dataAsep jadi tidak muncul
print(f"data asep = {dataAsep}")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir ajah)
dataTerakhir = friends.popitem()
print(f"data terkahir = {dataTerakhir}")
print(f"friends = {friends}\n")
