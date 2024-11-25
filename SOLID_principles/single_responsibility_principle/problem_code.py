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
