#wapp to write the no.of letters and digits in the given string in a file object

str = input("Enter the string: ")

letter_count = 0
digit_count = 0 

for char in str:
    if char.isalpha():
        letter_count +=1
    elif char.isdigit() : 
        digit_count+=1

#storing counts to a file

file_path = 'letter_counts.txt'
file = open(file_path , 'w')    
file.write(f"Number of letters in the string: {letter_count}\n")  
file.write(f"Number of digits in the string: {digit_count}\n")  
file.close()
