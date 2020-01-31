dict_history = [];

def binary_search(list, item):
    # array indices
    low = 0
    high = len(list) - 1
    global dict_history;
    
    def print_dic(dict):
        for val in dict:
            # print(val)  # prints dict at index    # {'item': 9, 'low': 0, 'high': 100, 'mid': 50, 'guess': 50}

            # prints in nicely formatted python2
            #     search val: 9    low: 0          high: 100        mid: 50          guess: 50
            print('search val: %s  \t low: %s  \t high: %s  \t  mid: %s  \t   guess: %s' % (val['item'], val['low'], val['high'], val['mid'], val['guess']))
                # this will print out val
            for k, v in val.items(): # we can use any variable for key, value positions
                # print(f'\t Key: {k} \t Value: {v}')   # python 3
                print("\t Key: %s \t Value: %i " % (k, v))

    while low <= high:  
        # print(f'search val: {item}   low: {low} high: {high} mid: {mid}')
        mid = (low + high) // 2    # gives floor, rounded down val
        guess = list[mid]     # check the middle val
            # python3 syntax
        # print(f'search val: {item}  \t low: {low}  \t high: {high}  \t  mid: {mid}  \t   guess: {guess}')
            # python2 syntax
        # print('search val: %s  \t low: %s  \t high: %s  \t  mid: %s  \t   guess: %s' % (item, low, high, mid, guess))
        # dict_history.append({item: item, low: low ,high: high, mid: mid,  guess: guess})   # saves k &v as same e.g.     { 9: 9, 50: 50, ...}
        dict_history.append({'item': item, 'low': low, 'high': high, 'mid': mid, 'guess': guess})
        if guess == item:
            #  return mid     # middle is actual item    --> use with # print(binary_search(test_list, find))
            # python 3 syntax
            #return print(f' item located: {guess}')
                # python 2 syntax
            print("item located {} after {} iterations".format(guess, len(dict_history)) )    
            print_dic(dict_history)
            return None
        elif guess > item:  
            high = mid - 1  # look in lower half
        else:               
            low = mid + 1   # look in upper half        
    return None


test_list =  list(range(0,101))   # generate list 1 to 100 
find = 9

# print(binary_search(test_list, find))
binary_search(test_list, find)