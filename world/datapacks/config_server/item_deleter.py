import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))

item_list_file = os.path.join(current_dir, "data", "rk", "tags", "items", "deleted.json")
delete_item_file = os.path.join(current_dir, "data", "rk", "functions", "delete", "tick_item_entity.mcfunction")

try:
    with open(item_list_file) as j:
        d = json.load(j)
        
        with open(delete_item_file, "w", encoding="utf-8") as f:
            print("\n==========================================================" \
                  "\nItem List:")
            count = 0
            for value in d["values"]:
                count+=1
                f.write("execute as @e[nbt={Item:{id:\""+value+"\"}}] run kill @s\n")
                print(f" - {value}")

            print(f"\n{count} item(s) loaded")
except FileNotFoundError:
    print("\nSomething failed...")

print("==========================================================\n")