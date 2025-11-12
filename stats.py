def get_num_words(file_content):
    return len(file_content.split())

def count_characters(file_content):
    counts = {}
    for char in file_content.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

def get_sorted_list(file_dict):
    return_list = []
    for char, count in file_dict.items():
        return_list.append({
            "char": char,
            "num": count
        })
    return sorted(return_list, reverse=True, key=get_num_from_dict)
    
def get_num_from_dict(items):
    return items["num"]