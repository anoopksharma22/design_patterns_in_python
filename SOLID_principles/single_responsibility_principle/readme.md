## Single Responsibility Principle
Also known as **Seperation of Concerns**, it states that: A class should have only one primary responsibilty and should not have any other responsibilty or area of concern.\
We should always do separation of concerns.

### Example
Let's say we need to implement a program to manage Journals:

### Class
We can create a class which Journal to represent a journal and add functionaly to add journals and save Journals.

```python
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.entries.append(text)
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)
    
    def save(self):
        with open("journal.txt","w") as fh:
            fh.write('\n'.join(self.entries))


if __name__ == "__main__":
    j = Journal()
    print("Adding entries")
    j.add_entry("Learn python")
    j.add_entry("Learn solid principles")
    j.add_entry("Learn design patterns")
    j.add_entry("dummy")
    print(f"Journal after adding entries{j}")

    print("Removing entry")
    j.remove_entry(3)
    print(f"Journal after removin entry{j}")

    print("Saving journal to a file")
    j.save()
```

### Issue with above implementation:
Journal class has two area of concerns:
- Creating and adding entries.
- Saving / Persistance of entries.

Now issue is if we have many such classes eg: Quotes, Poems etc in our systeam and each have their own function to save then if we want to modify the storage form let's say file to some DB, then we need to change all the classes.

### Solution
We can do separatiop of concerns
- Creation / addition should be handled by Journal class.
- For persistance we can create a persistasnce manager class, which would take any class like journal and file name to persist data.

```python
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.entries.append(text)
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    #### Moved to separate Persistanve class    
    # def save(self):
    #     with open("journal.txt","w") as fh:
    #         fh.write('\n'.join(self.entries))

class PersistanceManager:

    @staticmethod
    def save(file_name, entries):
        with open(file_name,"w") as fh:
            fh.write('\n'.join(entries))

if __name__ == "__main__":
    j = Journal()
    print("Adding entries")
    j.add_entry("Learn python")
    j.add_entry("Learn solid principles")
    j.add_entry("Learn design patterns")
    j.add_entry("dummy")
    print(f"Journal after adding entries{j}")

    print("Removing entry")
    j.remove_entry(3)
    print(f"Journal after removin entry{j}")

    print("Saving journal to a file")
    file_name = "journal.txt"
    PersistanceManager.save(file_name, j.entries)

```