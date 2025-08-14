def kilometer_converters(kilometer):
    kilometer= float(input('enter kilometer:'))
    miles= kilometer_c * 0.621371
    print(f'{kilometer_converters} km = {miles:.2f} m')

def temperature_converter(temperature):
    temp_c=float(input('enter temp_c:'))
    temp_f=(temp_c * 9/5) +32
    print(f'{temp_c}C = {temp_f:.1f}F')
  
  
def calculate_discount() :
    cost=float(input('Enter the cost')) 
    if cost > 100:
        final= cost * 0.8
    elif cost >= 50:
        final= cost * 0.9
    else:
        final= cost 

    cost=float(input('enter cost'))
    print(f'discount cost: mk{final}')

def main():
    print('welcome to smart tool')
    print('1.kilometer to miles converter')
    print('2.temperature converter')
    print('3.shop discount calculator')

    choice = input('choose an option(1-3):')
    if choice== '1':
        kilometer_converters()
    elif choice== '2':
        temperature_converter()
    elif choice== '3':
        calculate_discount()
    else:
        print('please try again later')
main()