class Transaction:
    def __init__(self, trans_number, letter, action):
        self.number = trans_number
        self.letter = letter
        self.action = action
        
    def has_conflict(self, transaction2):
        if self.number == transaction2.number:
            return False
        
        if self.letter != transaction2.letter:
            return False
        
        if self.action == 'r' and transaction2.action == 'r':
            return False
        
        return True
    
    def stringify(self):
        return str(self.action+self.number+'('+self.letter+')')
    

transaction_string = input('Enter transactions divided by ;')
transaction_string = transaction_string.replace(' ', '')
transactions = transaction_string.split(';')
transactions_list = []

for transaction in transactions:
    action = transaction[0]
    number = transaction[1]
    letter = transaction[3]
    trans_object = Transaction(number, letter, action)
    transactions_list.append(trans_object)


for i in range(0, len(transactions_list)):
    current_transaction = transactions_list[i]
    print('Conflicts for '+current_transaction.stringify()+':')
    
    if i == len(transactions_list) -1:
        break
    
    for j in range(i+1, len(transactions_list)):
        compare_transaction = transactions_list[j]
        if current_transaction.has_conflict(compare_transaction):
            print(current_transaction.stringify()+' -> '+ compare_transaction.stringify())
    
    print('')
