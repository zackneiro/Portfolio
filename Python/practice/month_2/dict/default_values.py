def main() -> None:

    default_dict = {"a" : 0, "b" : 0, "c" : 0}
    input_dict = {"a" : 5, "b" : 10}
    
    print(merge_dict(default_dict, input_dict))

def merge_dict(dict_def : dict[str, int] , dict_inpt : dict[str, int]) -> dict[str, int]:

    """
    This function returns the merged dictionary
    """

    if not dict_def:
        return dict_inpt
    if not dict_inpt:
        return dict_def
    
    merged = dict_def.copy()

    for key, value in dict_inpt.items():
            merged[key] = value

    return merged
        

        


main()