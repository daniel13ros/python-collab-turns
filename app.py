# app.py
from utils import add_entry, delete_last_entry, read_entries

add_entry("A: refining update")
add_entry("Project initialized by B") 

delete_last_entry()
add_entry("B: replaced deleted entry")

print("Executed by A")
print("Executed by B")
for line in read_entries():
    print(line)