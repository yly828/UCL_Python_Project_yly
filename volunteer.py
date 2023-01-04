import pandas
import os
from refugee import Refugee
import datetime


class Volunteer:
    if os.path.exists("volunteers.csv"):
        volunteers = pandas.read_csv("volunteers.csv")
    else:
        volunteers = pandas.DataFrame()

    # figure out how to represent and store availability dates
    def __init__(self, username, password, firstName, lastName, phone, camp, avail_startDate, avail_endDate):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.camp = camp
        self.avail_startDate = avail_startDate
        self.avail_endDate = avail_endDate
        self.active = True
        self.status = "volunteer"
        self.login = False
        #self.loginname_exist = False

        #make sure username created by using volunteer class directly is unique
        if Volunteer.volunteers.empty or not any(Volunteer.volunteers['username'] == self.username):
            # adding the volunteer to the volunteers df by turning it into separate df and concatenating the two
            volunteer = {"username": self.username, "password": self.password, "firstname": self.firstName,
                         "lastname": self.lastName, "phone": self.phone, "camp": self.camp,
                         "avail_startDate": self.avail_startDate,
                         "avail_endDate": self.avail_endDate,"status": self.status, "active": self.active, "login": self.login}
            df = pandas.DataFrame([volunteer])
            Volunteer.volunteers = pandas.concat([Volunteer.volunteers, df], ignore_index=True)
            # save df to csv file
            Volunteer.volunteers.to_csv('volunteers.csv', index=False)
        else:
            print('The username already exists')

    @staticmethod
    def create_profile(firstname, lastname, camp, condition, dependants):
        return Refugee(firstname, lastname, camp, condition, dependants)

    @staticmethod
    def edit_info(username, key, value):
        df = pandas.read_csv("volunteers.csv")
        df.loc[df.username == username, key] = value
        df.to_csv("volunteers.csv", index=False)

    @staticmethod
    def date_is_valid(user, period, cur_date):
        if period == "start":
            date_column = "avail_endDate"
        elif period == "end":
            date_column = "avail_startDate"
        df = pandas.read_csv("volunteers.csv")
        original_date = df.loc[df.username == user, date_column].values.item()
        cur_date =  datetime.datetime.strptime(cur_date, '%d/%m/%Y')
        original_date = datetime.datetime.strptime(original_date, '%d/%m/%Y')
        if period == "start":
            if cur_date < original_date:
                return True
        if period == "end":
            if cur_date > original_date:
                return True
        return False


