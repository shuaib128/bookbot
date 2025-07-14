def word_count(content):
     return(len(content.split()))
 
def count_characters(content):
    char_count = {}
    
    for char in content.lower():
        if char != ' ':  # optional: skip spaces
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def sort_characters(char_dict):
    sorted_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list
