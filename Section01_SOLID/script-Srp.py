from Section01_SOLID.SingleResponsivePrinciple.Journal import Journal
from Section01_SOLID.SingleResponsivePrinciple.PersistenceManager import PersistenceManager

j: Journal = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p: PersistenceManager = PersistenceManager()
file: str = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
