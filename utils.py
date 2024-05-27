def det_list_type(list):
    for item in list:
        if item:
            try:
                int(item)
                return "int"
            except ValueError:
                try:
                    
                    float(item)
                    return "float"
                except ValueError:
                    return "str"

def are_there_duplicates(list):
    return len(list) != len(set(list))