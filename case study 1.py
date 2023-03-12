#Q1
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
l = [1,2,3,4]
print(type(l))
d = {"Name" : "Jake",
     "Age" : 27,
     "Adress": "Downtown"}
print(type(d))
t = ("Machine Learning", "Data Science")
print(type(t))
s = {"Python","Machine Learning","Data Science"}
print(type(s))

#Q2
def func(string):
    new = ""
    for i in string:
        if "a"<= i <= "z" or "A"<= i <= "Z":
            new += i.upper()
        elif i == " " or i == "," or i == ".":
            new += ","
        else:
            continue
    print(new)   

func("The goal is to turn data into information, and information into insaight")                  
            
#Q3
lst = ["D","A","T","A","S","C","I","E","N","C","E"]
print(len(lst))
print(lst[0],lst[10])
new = []
for i in range(len(lst)):
    if i < 4 :
        new += lst[i]
    else:
        continue   
print(new)
lst.pop(8)
print(lst)
lst.append("*")
print(lst)
lst.insert(8,"N")
print(lst)

#Q4
dict = {'Christian': ["America",18],
        'Daisy' : ["England",12],
        'Antonio' : ["Spain",22],
        'Dante' : ["Italy",25]}
print(dict.keys())
print(dict.values())
print(dict['Daisy'])
dict.update({'Ahmet' : ["Turkey",24]})
print(dict)
dict.pop('Antonio')
print(dict)

#Q5
l = [2,13,18,93,22]

def func(list):
 odd = []
 even = []  
 for i in range(len(list)):
        if list[i] % 2 == 0:
            even.append(list[i])
        else:
            odd.append(list[i])
 print(list,even,odd)               
 return even , odd       

func(l)

#Q6
Muhendislik_Fakultesi = []
Tip = []
students = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index, student in enumerate(students):
    if index % 2 == 0:
        Muhendislik_Fakultesi .append(student)
    else:
        Tip.append(student)    

for index,student in enumerate(Muhendislik_Fakultesi,1):
    print("Mühendislik Fakültesi",index,". öğrenci", student)  
for index,student in enumerate(Tip,1):
    print("Tıp",index,". öğrenci", student)       

#Q7
ders_kod = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
m = list(zip(kredi,ders_kod,kontenjan))
for i in range(len(m)):
    print("Kredisi",m[i][0],"olan",m[i][1],"kodlu dersin kontenjanı",m[i][2],"kişidir")

#Q8
set1 = set(["data","python"])
set2 = set(["data","functions","qcut","lamba","python","miuul"])
if set1.issuperset(set2) :
    print(set1.intersection(set2))
else:
    print(set2.difference(set1))        
    
    