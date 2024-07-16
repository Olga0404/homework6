print("Работа со словарями:")
my_dict = {'Анна': 1985, "Петр":2003, "Николай":1996, "Илья":2001}
print('Dict:',my_dict)
print("Existing value:", my_dict["Петр"])
print("Not existing value:", my_dict.get("Ольга","Такое имя отсутствует")) #Выведите на экран одно значение по существующему ключу,
# одно по отсутствующему из словаря
my_dict["Ольга"]=2010
my_dict2={"Нонна":2004, "Артем":2007}
my_dict.update(my_dict2)
n=my_dict.pop("Николай")
print("Deleted value:", n)
print("Modified dictionary:", my_dict)

print("Работа с множествами:")
my_set={56,"Ponchik", 1, True, 33,1,1,2,33,56,"Ponchik", "ponchik",1,False,0,0}
print("Set:", my_set)
my_set.update([48,15])
my_set.add("и еще один элемент")
my_set.remove("ponchik")
print("Modified set:", my_set)