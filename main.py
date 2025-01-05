def main ():
    file_contents = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words():
    contents = main()
    return len(contents.split())

def sort_on(dict):
    return dict["num"]

def count_characters():
    array_char = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    contents = main()
    lowered_string = contents.lower()
    words = lowered_string.split()
    for word in words:
        for char in word:
            if char in array_char:
                array_char[char] += 1
    dictlist = []
    for key, value in array_char.items():
        temp = {'letter': key,'num': value}
        dictlist.append(temp)
    dictlist.sort(reverse=True, key=sort_on)
    return dictlist

main()
counted_word = count_words()
counted_char = count_characters()
print("--- Begin report of books/frankenstein.txt ---")
print(f"{counted_word} words found in the document")
print("")
for char in counted_char:
    print(f"The '{char['letter']}' character was found {char['num']} times")
print("--- End report ---")