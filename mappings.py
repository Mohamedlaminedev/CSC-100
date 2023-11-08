def all_mappings(input_dict):
    result = []
    
    for key, value_list in input_dict.items():
        for element in value_list:
            result.append((key, element))
    
    return result
