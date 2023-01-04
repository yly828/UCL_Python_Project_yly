class Update_Camp:
    def __init__(self):
        import pandas as pd
        tonext = True   
        df = pd.read_csv('Camp.csv')
        print("\nHere are the EXISTING CAMPS: \n")
        print(df)
        while tonext:
            choice = input("\nWould you like to:\n\n[1] Edit details?\n[Q] Go back\n")
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