#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("../../Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    j = file.readlines()
    kl =[]
    for i in j:
        hi = i.strip()
        kl.append(hi)

with open("../../Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as letter:
    u = letter.read()
    for i in kl:
        h = u.replace("[name]", i)
        y = open (f"C:/Users/yaswa/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{i}.txt", mode="w+")
        y.write(h)


