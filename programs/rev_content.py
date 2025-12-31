

file_name ="content.txt"
with open(file_name , "r") as file :
    content = file.read()


reverse_content = content[::-1]

new_content = ",".join(reverse_content)

with open (file_name , "w") as file:
    file.write(new_content)




