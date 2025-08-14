def calculate_discount(cost):
    if cost > 100:
        return cost * 0.8
    elif cost >= 50:
        return cost * 0.9
    else:
        return cost 


cost=float(input('enter the cost'))
print(calculate_discount(cost))