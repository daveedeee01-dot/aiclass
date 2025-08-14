# creating dictionary
contact_book= {'dave':'123456789','huncho':'987654321','digga':'222111333'}

contact_book['santana']='90872635'
contact_book['p prime']='65465233'

# accessing dict
print(contact_book['santana'])
print(contact_book.get('p prime'))

#updating dict
contact_book['santana']= '885446545'
#removing item in dict
remove_number=contact_book.pop('digga')
del contact_book['huncho']

print(contact_book)



# menu
menu_book={'pizza':'12.99','salad':'6.99','fish':'10.99'}
del menu_book['salad']
print(menu_book)

#looping through a dictionary
#loop through keys
for item in contact_book.keys():
    print(item)
# loop through values
for phone_num in contact_book.values():
    print(phone_num)

# loop through key values
for item,phone_num in contact_book.items():
    print(f'{item}: {phone_num}')