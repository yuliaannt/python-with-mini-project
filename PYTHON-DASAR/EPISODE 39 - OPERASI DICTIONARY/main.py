# operator dictionary

data_dict = {
    "cup": "ucup surucup",
    "tong": "surotong",
    "dung": "surudung",
    "mam": "mamamia",
}

# panjang dict
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")


# mengecek key exist atau tidak

KEY = "CUP"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data di dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("kiss", "key tidak ditemukan"))  # key dengan messege
print(data_dict.get("cup"))

# melakukan update data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["dung"] = "hudung si ganteng"
print(data_dict)

# update
data_dict.update({"dung": "surudung"})
print(data_dict)
# kalo gaada datanya bisa di .add()

# delete
del data_dict["dung"]
print(data_dict)
