def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
if __name__ == "__main__":
    main()

def wordcount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        split = file_contents.split()
        count = len(split)
        print(count)
wordcount()

def countLetters():
    lettercounter = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowercase = file_contents.lower()
        for i in lowercase:
            if i.isalpha():
                if i in lettercounter:
                    lettercounter[i] += 1
                else: 
                    lettercounter[i] = 1
countLetters()

def report():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = len(file_contents.split())
    print("--- Begin report of books/frankenstein ---")
    print(f"{count} words found in the document")
    lettercounter = {}
    lowercase = file_contents.lower()
    for i in lowercase:
            if i.isalpha():
                if i in lettercounter:
                    lettercounter[i] += 1
                else: 
                    lettercounter[i] = 1
    
    list_of_dictionaries = []
    for char, count in lettercounter.items():
         entry = {"char": char, "count": count}
         list_of_dictionaries.append(entry)

    list_of_dictionaries.sort(key=lambda x: x['count'], reverse=True)

    for i in list_of_dictionaries:
        print(f"The '{i['char']}' character was found {i['count']} times")
    
    
    print("\n --- End report ---")

report()