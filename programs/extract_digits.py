

file_name = "input.txt"

with open(file_name , "r") as file:
    content = file.read()


words = content.split()

digit_words = [word for word in words if word.isdigit()]

print("words composed of digit only" , digit_words)