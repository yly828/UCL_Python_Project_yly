import pandas
import os
from volunteer import Volunteer
from emergency import Emergency
import datetime


class Admin:
    if os.path.exists("admin.csv"):
        admins = pandas.read_csv("admin.csv")
    else:
        admins = pandas.DataFrame()

    def __init__(self, login, password):
        self.username = login
        self.password = password
        self.status = "admin"

        admin = {"username": self.username, "password": self.password, "status": self.status}
        df = pandas.DataFrame([admin])
        Admin.admins = pandas.concat([Admin.admins, df], ignore_index=True)
        # save df to csv file
        Admin.admins.to_csv('admin.csv', index=False)

    @staticmethod
    def register_volunteer(username, password, firstName, lastName, phone, camp, avail_startDate, avail_endDate):
        return Volunteer(username, password, firstName, lastName, phone, camp, avail_startDate, avail_endDate)

    @staticmethod
    def deactivate_volunteer(username):  # tested
        data = pandas.read_csv("volunteers.csv")
        df = pandas.DataFrame(data)
        if username in df.username.values:
            df.loc[df.username == username, 'active'] = False
            df.to_csv("volunteers.csv", index=False)
            return True
        else:
            return False  


    @staticmethod
    def activate_volunteer(username):  # tested
        df = pandas.read_csv("volunteers.csv")
        if username in df.username.values:
            obtained = df.loc[df.username == username, 'active']
            if obtained.item() == False:

                while True:
                    if Admin.update_renew_enddate(username, df):
                        break
                return True
      
                            
        else:
            return False

    @staticmethod
    def update_renew_enddate(username,df):
        renew_Enddate = input('Enter a new end date (mm/dd/yyyy): ')
        print("New end date I have entered:", renew_Enddate)
        try:
            renew_Enddate = datetime.datetime.strptime(renew_Enddate, '%m/%d/%Y')            
            renew_Enddate = renew_Enddate.strftime("%m/%d/%Y")
            df.loc[df.username == username, 'avail_endDate'] = renew_Enddate
            df.loc[df.username == username, 'active'] = True
            df.to_csv("volunteers.csv", index=False)
    
        except Exception as e:
            print('Invalid date!', e)
        else:
            return True



    @staticmethod
    def create_emergency(kind, desc, area):
        return Emergency(kind.lower(), desc.lower(), area.lower())

    @staticmethod
    def close_emergency(index, date):
        data = pandas.read_csv("emergencies.csv")
        df = pandas.DataFrame(data)
        df.loc[index, "endDate"] = date
        df.loc[index, "active"] = False
        df.to_csv("emergencies.csv", index=False)
