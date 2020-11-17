from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
path = "/content/gdrive/My Drive/COLAB_RATMIR/HOMEWORK/insta_follower.csv"
with open(path, "r") as f:
    a = f.readlines()
names = []
for i in a[1:]:
    names.append(i)
names_set = set(names)
d = {name:names.count(name) for name in names_set}
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
names_set = set(names)
d = {name:names.count(name) for name in names_set}
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
names_set = set(names)
d = {name:names.count(name) for name in names_set}
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
names_set = set(names)
d = {name:names.count(name) for name in names_set}
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
del d[name]
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)
names_set = set(names)
d = {name:names.count(name) for name in names_set}
maxx = 0
name = ""
for i,j in d.items():
    if j > maxx:
        name = i
        maxx = j
print(name)