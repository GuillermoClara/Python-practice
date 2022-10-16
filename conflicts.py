class Action:
    
    def __init__(self, trans_number, letter, command):
        
        # number = Transaction number 
        # letter = field being affected
        # command = what is done to the field
        # Ex: R1(A)    Read(A) in Transaction 1
        
        self.number = trans_number
        self.letter = letter
        self.command = command
    
    # There is conflict if:
    # 1. We have ast least one Write
    # 2. Dont belong to the same transaction
    # 3. The letter inside the parentheses is the same
    def has_conflict(self, action2):
        if self.number == action2.number:
            return False
        
        if self.letter != action2.letter:
            return False
        
        if self.action == 'r' and action2.action == 'r':
            return False
        
        return True
    
    def stringify(self):
        return str(self.action+self.number+'('+self.letter+')')
    
# Parse user input
action_string = input('Enter commands divided by ;')
action_string = action_string.replace(' ', '')
actions = action_string.split(';')
actions_list = []

# Generate Action objects
# (R1(A) for example)
for action in actions:
    
    command = action[0]
    number = action[1]
    letter = action[3]
    action_object = Action(number, letter, command)
    actions_list.append(action_object)

# Iterate through all actions
for i in range(0, len(actions_list)):
    current_action = actions_list[i]
    print('Conflicts for '+current_action.stringify()+':')
    
    # If we reach the last action, ignore 
    if i == len(actions_list) -1:
        break
    
    # Compare current action to all actions succeding it
    # (i.e. We dont care about past actions)
    for j in range(i+1, len(actions_list)):
        
        compare_action = actions_list[j]
        
        if current_action.has_conflict(compare_action):
            
            print(current_action.stringify()+' -> '+ compare_action.stringify())
    
    print('')
