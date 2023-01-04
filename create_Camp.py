class create_Camp:
    def __init__(self):
        import pandas as pd
        tonext = True
        #start a new camp
        check1 = input("\nIs this the first camp for this disaster? (Y/N)")
        if check1.lower() == "y":
            check2 = input("\nThis will wipe any existing camp records! Are you sure? (Y/N)")
            if check2.lower() == "y":
                df=None
              
        else:
            df = pd.read_csv('Camp.csv')
            print("\nHere are the EXISTING CAMPS: \n")
            print(df)
            create_Camp.rtot(df)
        
        self.camp = input("\nNew Camp name? ")
        self.loc = input("Location? ")
        while True:
            self.nums = input("Num of refugees registered? ")
            if self.nums.isdigit():
                break
            else:
                print("Please type in a number.")
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
        df = pd.concat([df, dfNewCamp])
        df.to_csv('Camp.csv',index=False)
        print("\nUpdated CAMPS: \n")
        print(df)
        df = pd.read_csv('Camp.csv')
        create_Camp.rtot(df)
        
        while tonext:
            choice = input("\nWould you like to:\n\n[1] Edit details?\n [Q] Go back\n")
            #edit data
            if choice == '1':
                row=int(input("Type in the index of the row you want to edit: "))
                print()
                print(df.loc[row],"\n")
                field=input("Which of these would you like to edit? \n")
                new_val=input("Type in the new value: ")
                df.loc[row, field]=new_val
                df.to_csv('Camp.csv',index=False)
                print("\nUPDATED CAMPS: \n")
                print(df)
                df = pd.read_csv('Camp.csv')
                create_Camp.rtot(df)  
            elif choice.lower() == 'q':
                print('---------------------------------------')
                check = input("Are you sure to go back?\n [Y] Yes, please go back. [N] No, continue.\n")
                if check == "Y" or check == "y":
                    tonext=False
                if check != "Y" and check != "y":
                    pass
            else:
                df.to_csv('Camp.csv', index=False)
                tonext = True
    def rtot(df):
        #print()
        ref_count=0
        len_df=len(df.index)
        for row in range (0,len_df):
            ref_count=ref_count+int(df.loc[row, 'nums'])
        #print("Total refugees =",ref_count)
        print("\033[1;32;50m+"+"-"*56+"+")
        print("|\t\t\t\t\t\t\t |")
        print("|  \033[1;0;50m Total refugees:\033[1;31;50m",ref_count,"\033[1;32;50m "*(35-len(str(ref_count))),"|")
        print("\033[1;32;50m|\t\t\t\t\t\t\t |")
        print("+"+"-"*56+"+\033[1;0;50m")