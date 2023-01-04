import pandas as pd
next = True
class create_Camp:
   def __init__(self):
      self.camp = input("\nCamp name? ")
      self.loc = input("Location? ")
      self.nums = input("Num of refugees registered? ")
      self.food = input("Food/water? ")
      self.shelter = input("Shelters? ")
      self.blankets = input("Blanlets? ")
      self.comms = input("Communications? ")
      self.access = input("Access? ")
      self.toilets = input("Toilet facilities? ")
   
      newCamp={
            'camp':[self.camp],
            'loc': [self.loc],
            'nums': [self.nums],
            'food': [self.food],
            'shelter': [self.shelter],
            'blankets': [self.blankets],
            'comms': [self.comms],
            'access': [self.access],
            'toilets': [self.toilets]
        }
      dfNewCamp = pd.DataFrame(newCamp)
      dfNewCamp.to_csv('NewCamp.csv', index=False)

#start a new camp
check1 = input("\nIs this the first camp for this disaster? (Y/N)")
if check1.lower() == "y":
    check2 = input("\nThis will wipe any existing camp records! Are you sure? (Y/N)")
    if check2.lower() == "y":
        clearPanda = {'camp': ['o'],'loc': ['o'],'nums': ['o'],'food': ['o'],'shelter': ['o'],'blankets': ['o'],'comms': ['o'],'access': ['o'],'toilets': ['o']}
        df = pd.DataFrame(clearPanda)
        Rec=df
        df.to_csv('Camp.csv', index=False)

df = pd.read_csv('Camp.csv')
print("\nHere are the EXISTING CAMPS: \n")
print(df)
while next:
    choice = input("\nWould you like to:\n\n[1] Add another camp?\n[2] Edit details?\n[Q] Quit the Program\n")
    # add to existing camps
    if choice.lower() == "1":
        next = True
        create_Camp()
        dfNewCamp = pd.read_csv('NewCamp.csv')
        df = pd.concat([df, dfNewCamp])
        print("\nEXISTING CAMPS: \n")
        print(df)
    #edit data
    if choice == '2':
        row=int(input("Type in the index of the row you want to edit: "))
        print()
        print(df.loc[row],"\n")
        field=input("Which of these would you like to edit? \n")
        new_val=input("Type in the new value: ")
        df.loc[row, field]=new_val
        df.to_csv('Camp.csv')
        print("\nUPDATED CAMPS: \n")
        print(df)
        
    elif choice == 'Q':
        print('---------------------------------------')
        check = input("Are you sure to quit the program?\n [Y] Yes, please quit. [N] No, take me back.\n")
        if check == "Y" or check == "y":
            quit()
        if check != "Y" and check != "y":
            pass
    else:
        df.to_csv('Camp.csv', index=False)
        next = False
