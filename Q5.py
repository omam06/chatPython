def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if item not in stock:       #2 for 2nd order, goes back to check original stock(5) again instead of remaining stock(2)
            raise ValueError('Unknown Item: NOT in stock') #so it accepted 6 in total out of 5 available 
    
        elif quantity > remaining[item]:
            raise ValueError('Insufficient stock')       #unknown item check must come 1st
    
        elif quantity <= 0:
            raise ValueError('CANNOT take negative or zero order quantities')
    
        remaining[item] = remaining[item] - quantity    #stock[item] uses original stock everytime and keyerror if item dont exist
    return remaining         #1 after 1st order, remaining becomes 2


#successful repeated items
stock = {'pen': 5, 'book': 10} 
order = [('pen', 3), ('pen', 1), ('book', 4)]

#repeated order exceed stock
# stock = {'pen': 5}
# order = [('pen', 3), ('pen', 3)]

#unknown item
# stock = {'pen': 5}
# order = [('pencil', 2)]     

#for 0 order qnty
# stock = {'pen': 5}
# order = [('pen', 0)]

#for -ve order qnty
# stock = {'pen': 5}
# order = [('pen', -3)]
print(reserve_stock(stock, order))

assert reserve_stock({'pen': 5, 'book': 10}, [('pen', 3), ('pen', 1), ('book', 4)]) == {'pen': 1, 'book': 6}, 'Successful repeated items did not pass'
# assert reserve_stock({'pen': 5}, [('pen', 3), ('pen', 3)]) == ValueError('Insufficient stock')   X. use try/except to assert ValueError
try:
    reserve_stock({'pen': 5}, [('pen', 3), ('pen', 3)])
    assert False
except ValueError:
    assert stock['pen'] == 5

try:
    reserve_stock({'pen': 5}, [('pencil', 2)])
    assert False
except ValueError:
    pass

try:
    reserve_stock({'pen': 5}, [('pen', 0)])
    assert False
except ValueError:
    pass

#edit local copy protects original wen exception happens halfway through the order