class lybrary:
    def __init__(self,books):
          self.books=books

    def borrow_books(self,title):
        for i in self.books:
            if title.lower() == i.lower():
                return 'available'
            else:
                return 'this shit cant be in your collection'
books=['history','biology','social']
documents=lybrary(books)
documents.borrow_books('social')
print(documents.borrow_books('maths'))




class bank_account:
    def __init__(self,account_name):
        self.account_name = account_name
        self.balance= 0

    def depositing(self,money):
        self.balance += money
        return f'your balance is {self_balance}'
    def withdraw(self,money)
        if self.balance >= money:
            self.balance -=money
            return f'your balance is {self.balance}
        else:
            return f'chill you dont have money'


account_name=['john','joyce']
mpamba=bank_account('john')
deposit_amount=int(input('how much do u want to deposit'))
print(mpamba.depositing(amount))
withdraw_amount=int(input('how much do u want to withdraw'))
print(mpamba.withdraw(amount))