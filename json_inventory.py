import json
import logging
import sqlite3

data = "new_file.json"

def loading():
    with open(data,"r") as x:
        return json.load(x)

def dumping(loading):
    with open(data,"w") as f:
        name= input("Enter the name: ")
        price = int(input("Enter the price: "))
        category = input("Enter the category of it: ")
        inventory = {
            "name": name,
            "price": price, 
            "category": category
              }
        loading.append(inventory)
        json.dump(loading,f , indent=4)


def searching(loading):
    search_item = input("Enter the item for searching: ")
    flag = 0
    for i in range(len(loading)):
        if search_item in loading[i]["name"]:
            save=i
            flag += 1
    if flag == 0:
        print("not found")
    else:
        print("found at index",save)
        print(f"the item",json.dumps(loading[save],indent=4))

def delete(loading):
    del_item = input("Enter the item for deleting: ")
    flag=0
    for i in range(len(loading)):
        if del_item in loading[i]["name"]:
            flag+=1
            save=i
    if flag ==0:
        print("item doesn't exists")
    else:
        loading.pop(save)
        print(f"The item is successfully deleted from the file")
        with open(data,"w") as updating:
            json.dump(loading, updating, indent=4)

def updating_item(loading):
    print("|name or 1 for updating name|\n|cat or 2 for updating category|\n|price or 3 for updating price|")
    key = input("Enter the key:")
    old_item=input("Enter the old item:")
    if key in ("1", "name"):
        change="name"
    elif key in ("2","cat"):
        change="category"
    elif key in ("3","price"):
        change="price"
    else:
        print("Invalid input!")
        return
    new_item= input("Enter the new item: ")
    flag = 0 
    for i in range(len(loading)):
        if old_item in loading[i][change]:
            flag+=1
            save=i
    if flag==0:
        print("somethings wrong")
    else:
        loading[save][change]=new_item

    with open(data, "w") as upd:
        json.dump(loading, upd, indent=4)



def main_menu():
    print("1 and add for adding new item to the file.\n" \
    "2 and search for searching an item in the file.\n" \
    "3 or del for deleting an item from the file.\n" \
    "4 or upd for updating new item in dictionary")
    task = input("Enter the task to perform: ")
    if task in ("1", "add"):
        dumping(loading())
    elif task in ("2", "search"):
        searching(loading())
    elif task in ("3", "del"):
        delete(loading())
    elif task in ("4","upd"):
        updating_item(loading())
    elif task in ("0", "exit"):
        return False
    else:
        print("Input is invalid!")

while True:
    result = main_menu()
    if result is False:
        break
