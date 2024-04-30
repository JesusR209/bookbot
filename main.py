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
                
                
    print(lettercounter)
countLetters()