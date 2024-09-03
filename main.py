
def character_counter(text, character):
    count = 0
    for char in text.lower():
        if char == character:
            count += 1
    return count

with open("books/frankenstein.txt") as file:
    text = file.read()
    
# Lowercase alphabet
lowercase_alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'

counter = {}    
for char in lowercase_alphabet:
    counter[char] = character_counter(text, char)


for char_count in counter.items():
    print(f"The character '{char_count[0]}' appears {char_count[1]} times in the text.")
    
counter_list = []
for char_count in counter.items():
    character = {"name": char_count[0], "num": char_count[1]}
    counter_list.append(character)
    

counter_list.sort(key=lambda x: x["num"], reverse=True)

print("\nTop 5 characters:")
for i in range(5):
    print(f"{i+1}. {counter_list[i]['name']} - {counter_list[i]['num']} times")