stock_in_store={'fanta':8,
'bread':4,
'shooter':9,
'ice':5,
'apple':12,
'sweet':7,
'books':4,
'pens':6,
'soap':0,
'nails':0,
'plane':4,
'atom':3,
'bottles':14,
'firewood':3,
'computers':9,}
stock_in_store['wire']=3
# update an exsting stock
stock_in_store['apple']=19
stock_in_store.pop('sweet')
print(stock_in_store)

# stock_quantity > 5
print('stock which is > 5 in store')
for stock, quantity in stock_in_store,items():
    if quantity > 5:
        print(stock)

# removing
new_quantity={}
for stock,quantity in stock_in_store.items():
    if quantity > 0:
        new_quantity[stock]=quantity
print(new_quantity)

total= sum(new_quantity.values())
print(total)