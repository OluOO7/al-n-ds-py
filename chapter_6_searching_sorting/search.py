def sequential_search(a_list, item):
    item_pos = 0
    while item_pos < len(a_list):
        print(a_list[item_pos])
        if(a_list[item_pos] == item):
            return True
        else:
            item_pos += 1
    return False

print(sequential_search([1, 2, 4, 3], 8))