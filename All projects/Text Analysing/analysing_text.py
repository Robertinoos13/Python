text = str(input("Enter you text here to work with it: \n"))
current_index = 0
commas = 0
dots = 0
words = 1
started_counting_words = False
letters = "qwertyuiopasdfghjklzxcvbnmăîâșțQWERTYUIOPASDFGHJKLZXCVBNMÎÂȘȚ"
letters_num = 0
numbers = "1234567890"
numbers_single_num = 0
paranthese = "({[<>]})"
paranthese_num = 0
nth = "{}"

for i in text:
    if not started_counting_words and i in letters:
        started_counting_words = True
    try:
        if i == " " and started_counting_words and text[current_index + 1] in letters or i in paranthese and text[current_index + 1] in letters:
            words += 1
    except IndexError:
        if i == " " and started_counting_words and text[current_index + 1] in letters or i in paranthese and i in letters:
            words += 1
    if i == ",":
        commas += 1
    elif i == ".":
        dots += 1
    elif i in paranthese:
        paranthese_num += 1
    elif i in numbers:
        numbers_single_num += 1
    
    current_index += 1

print("\nI analized your text:")
print(f'"{text}" \n')
print("-----------")
print(f"Commas: {commas}")
print(f"Dots: {dots}")
print(f"Words: {words}")
print(f"(),{nth},[] or <>: {paranthese_num} ({int(paranthese_num / 2)} pairs)")
print(f"Total numbers (single): {numbers_single_num}")
print("-----------")