###This method formats list of items into 3 rows into a table-like structure
def vformat_list(int_list):
    return_str = ""
    num_of_columns = 3
    cols_used = 0
    str_row = ""
    for item in int_list:
        #f"{item:36}" adds 36 pixels of padding after the item
        str_row = str_row + f"{item:36}"
        cols_used = cols_used + 1
        if cols_used == num_of_columns:
            return_str = return_str + str_row + "\n"
            cols_used = 0
            str_row = ""
    if(len(str_row)>0):
        return_str = return_str + str_row + "\n"
    return return_str
