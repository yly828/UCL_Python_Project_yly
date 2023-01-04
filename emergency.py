import pandas as pd
import os
import datetime


class Emergency:
    if os.path.exists("emergencies.csv"):
        emergencies = pd.read_csv("emergencies.csv")
    else:
        emergencies = pd.DataFrame()

    def __init__(self, kind, desc, area):
        self.kind = kind.lower()
        self.description = desc.lower()
        self.area = area.lower()
        self.startDate = "{0:%d/%m/%Y}".format(datetime.date.today())
        self.endDate = ""
        self.active = True

        emergencyPlan = {
            'kind': self.kind,
            'description': self.description,
            'area': self.area,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'active': self.active
        }
        df = pd.DataFrame([emergencyPlan])
        Emergency.emergencies = pd.concat([Emergency.emergencies, df], ignore_index=True)
        Emergency.emergencies.to_csv("emergencies.csv", index=False)
        print("Record created.\n")
        print(df)

    @staticmethod
    def update_emergencyPlan():
        emergencies = pd.read_csv("emergencies.csv")
        pd.set_option('display.max_rows', None) #As we need to choose index based on display, for now remove row limit
        print(emergencies)
        try:
            update_index = int(input("Choose correct index correlating to correct emergency: "))
            if update_index < len(emergencies):
                print("Please specify what information you would like to edit\n"
                      "[1] kind\n"
                      "[2] description\n"
                      "[3] area\n"
                      "[4] startDate\n"
                      "[5] endDate\n"
                      "[6] active\n")
                choice = input("Please choose an option: ")
                if choice == '1':
                    info = 'kind'
                elif choice == '2':
                    info = 'description'
                elif choice == '3':
                    info = 'area'
                elif choice == '4':
                    info = 'startDate'
                elif choice == '5':
                    info = 'endDate'
                elif choice == '6':
                    info = 'active'
                else:
                    print("Invalid choice.Please try again.\n")
                    print("Please input an index again.\n")
                    Emergency.update_emergencyPlan()

                if choice != '4' and choice != '5':
                    new = input("Please choose what to update {} : ".format(info)).lower()
                    emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = new
                    emergencies.to_csv("emergencies.csv", index=False)
                    print(emergencies)
                elif choice == '4':
                    input_Date_again = True
                    while input_Date_again:
                        input_date = input("Please type the updated startDate(DD/MM/YYYY): ")
                        try:
                            new = datetime.datetime.strptime(input_date, '%d/%m/%Y').strftime('%d/%m/%Y')
                            emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = new
                            emergencies.to_csv("emergencies.csv", index=False)
                            print(emergencies)
                            input_Date_again = False
                        except:
                            print("Input Date is wrong format.Please input again")
                            input_Date_again = True
                else:
                    start_date = emergencies.iloc[update_index, emergencies.columns.get_loc('startDate')]
                    formatted_start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
                    input_Date_again = True
                    while input_Date_again:
                        input_date = input("Please type the updated endDate(DD/MM/YYYY): ")
                        try:
                            new_enddate = datetime.datetime.strptime(input_date, '%d/%m/%Y')
                            if formatted_start_date <= new_enddate:
                                str_new_enddate = new_enddate.strftime('%d/%m/%Y')
                                emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = str_new_enddate
                                emergencies.to_csv("emergencies.csv", index=False)
                                print(emergencies)
                                input_Date_again = False
                            else:
                                print("endDate should be greater than startDate.Please input again")
                                input_Date_again = True
                        except:
                            print("Input Date is wrong format.Please input again")
                            input_Date_again = True
            else:
                print("Invalid index.Please input a correct index again.\n")
                Emergency.update_emergencyPlan()
        except:
            print("Invalid index.Please input a correct index again.\n")
            Emergency.update_emergencyPlan()

    @staticmethod
    def display_emergencyPlan():
        pd.set_option('display.max_rows', None)
        emergencies = pd.read_csv("emergencies.csv")
        print(emergencies)
