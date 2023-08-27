import string

created_tuple = ()

def isAnagram(w1_t, w2_t, w1, w2):
    global created_tuple
    if(sorted(w1_t)== sorted(w2_t)):
        if created_tuple == ():
            created_tuple = (w1, w2)
        else:
            created_tuple += (w2,)

list_of_tuples = []
first = True
characters = []
duplicate_removal_tuple = ()
text_file = open("output.txt", "w")
with open(r"words.txt", 'r') as fp:
    lines = fp.readlines()
    for word1 in lines:
        word1_trim = word1.translate({ord(c): None for c in string.whitespace})
        for word2 in lines:
            word2_trim = word2.translate({ord(c): None for c in string.whitespace})
            isAnagram(word1_trim, word2_trim, word1, word2)

        stripped_tuple = tuple(element.strip() for element in created_tuple)
        duplicate_removal_tuple = tuple(set(stripped_tuple))
        
        list_of_tuples.append(duplicate_removal_tuple)
        
        created_tuple = ()
 
    unique_list_of_tuples = []

    for t in list_of_tuples:
        if tuple(sorted(t)) not in unique_list_of_tuples:
            unique_list_of_tuples.append(tuple(sorted(t)))
                
    filtered_tuples = [tup for tup in unique_list_of_tuples if len(tup) > 1]

    for tuple in filtered_tuples:
        stripped_tuple = tuple[0].translate({ord(c): None for c in string.whitespace})
        for i in range(len(stripped_tuple)):
            characters.append(stripped_tuple[i].upper())

        final_output = f"{tuple}\n"

        total_count = len(sorted(characters))
        for char in sorted(characters):
            percental_value = round(((sorted(characters).count(char) / total_count) * 100), 2)
            absolute_value = sorted(characters).count(char)
            char_line = f"{char} - {absolute_value}, {percental_value}%\n"
            if char_line not in final_output:
                final_output += char_line
            
        print(final_output)
        text_file.write(final_output + ' \n')

        characters = []

    text_file.close()