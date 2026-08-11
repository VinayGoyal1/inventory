import json
import logging

data = "new_file.json"

logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

def loading():
    try:
        with open(data,"r") as x:
            return json.load(x)
    except FileNotFoundError:
        logging.info("Inventory file was not found")
        return []
    except json.JSONDecodeError:
        logging.error("Json.JSONDecodeError")
        return []

def dumping(loading):
    with open(data,"w") as f:
        name= input("Enter the name: ")
        try:
            price = int(input("Enter the price: "))
        except ValueError:
            logging.error("Input was wrong")
            print("Invalid Input Type")
            return
        category = input("Enter the category of it: ")
        inventory = {
            "name": name,
            "price": price, 
            "category": category
              }
        loading.append(inventory)
        logging.info("Item added %s",name)
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
        logging.info("Item found %s",json.dumps(loading[save]["name"]))

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
        logging.info("Item was deleted: %s",del_item)
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
    if change=="name":
        new_item= input("Enter the new item name: ")
    elif change=="category":
        new_item= input("Enter the new category")
    elif change=="price":
        try:
            new_item= int(input("Enter the price of item"))
        except ValueError:
            logging.error("Input was wrong")
            print("invalid Input Type")
            return
    else:
        print("Somethings wrong")
        return 
    flag = 0 
    for i in range(len(loading)):
        if old_item in loading[i][change]:
            flag+=1
            save=i
    if flag==0:
        print("somethings wrong")
    else:
        loading[save][change]=new_item
        logging.info("%s was changed to %s",old_item,new_item)
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
        logging.info("The user took exit")
        return False
    else:
        print("Input is invalid!")

while True:
    result = main_menu()
    if result is False:
        break
