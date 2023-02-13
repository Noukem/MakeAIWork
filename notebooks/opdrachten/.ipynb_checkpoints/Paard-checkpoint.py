# Loop langs elke letter in het woord “paard”​ 
# en check of dit een klinker is. 

# Define the string “paard”
word = "paard"

#Define counter
counter = 0

# Loop over each letter in string:
for char in word:
	
	# Check if character is vowel:
    if char == "a"or char == "e" or char ==  "i" or char == "o"or char == "u":
	# If so then increment counter
    
        counter = counter + 1

# Print result
print(f"paard contains {counter} vowels")