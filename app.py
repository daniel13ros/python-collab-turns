# app.py
from utils import add_entry, read_entries

add_entry("A: refining update")
add_entry("Project initialized by B") 
for line in read_entries():
    print(line)