#Task1/Görev1#
x = 8
print(type(x))

y = 3.2
print(type(y))

z = 8j + 18
print(type(z))

a = "Hello World"
print(type(a))

b = True
print(type(b))

c = 23 < 22
print(type(c))

l = [1, 2, 3, 4]
print(type(l))

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
print(type(d))

t = ("Machine Learning", "Data Science")
print(type(t))

s = {"Python", "Machine Learning", "Data Science"}
print(type(s))

#Task2/Görev2#
def new_sntnc(string):
    string = string.upper()
    string = string.replace(',', ' ')
    string = string.replace('.', ' ')
    words = string.split()
    return words

text = "The goal is to turn data into information, and information into insight."
print(new_sntnc(text))


#Task3/Görev3#

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

print(len(lst))

first_indx = lst[0]
print(first_indx)

ninth_indx = lst[9]
print(ninth_indx)

new_list = lst[0:4]
print(new_list)

delete = lst.pop(8)
print(lst)

add = lst.append("A")
print(lst)

again = lst.insert(8,"N")
print(lst)

#Task4/Görev4#

dict = {'Christian' : ["America", 18],
        'Daisy' : ["England", 12],
        'Antonio' : ["Spain", 22],
        'Dante' : ["Italy", 25]}

keys = dict.keys()
print("Keys:")
for key in keys:
    print(key)

values = dict.values()
print("Values:")
for value in values:
    print(value)

dict['Daisy'][1]=13
print(values)

dict['Ahmet'] = ["Turkey", 24]
print(dict)

del dict['Antonio']
print(dict)

#Task5/Görev5#

l = [2,13,18,93,22]
def func(lst):
    even_list = []
    odd_list = []
    for number in lst:
        if number % 2 == 0 :
          even_list.append(number)
        else :
          odd_list.append(number)
    return even_list, odd_list

even_list, odd_list = func(l)

print("Even list:", even_list)
print("Odd list:", odd_list)

#Task6/Görev6#

ogrenciler = ["Ali", "Veli", "Ayşe","Talat", "Zeynep", "Ece"]

muh_ogr = ogrenciler[:3]
tip_ogr = ogrenciler[3:]

for i, ogrenci in enumerate(muh_ogr,start=1):
    print(f"Mühendislik Fakültesi: {i}. öğrenci {ogrenci}")

for i, ogrenci in enumerate(tip_ogr,start=1):
    print(f"Tıp Fakültesi: {i}. öğrenci {ogrenci}")

#Task7/Görev7#

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi=[3,4,2,4]
kontenjan = [30,75,150,25]

for kod,krd,kntnjn in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi %s olan %s kodlu dersin kontenjanı %s kişidir." % (kod, krd, kntnjn))

#Task8/Görev8#

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
      common_elements = kume1.intersection(kume2)
      print(common_elements)
else:
      difference_elements = kume2.difference(kume1)
      print(difference_elements)






















