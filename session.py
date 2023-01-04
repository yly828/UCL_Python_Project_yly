import pandas
from admin import Admin
from volunteer import Volunteer
from create_Camp import create_Camp
from Update_Camp import Update_Camp
import logo_art
from message import Message
import datetime
from emergency import Emergency
import os
import sys
import time


class Session:
    def __init__(self):
        self.mode = None
        self.username = None
        self.active = None

    @staticmethod
    def print_logo():
        """Print the introduction of the system.
                   """
        print('******************************************************************************')
        print(logo_art.logo)
        print('******************************************************************************')

    def start(self):
        try:
            print('------------------------------------------------------------------------------')
            choice = input(
                "             Welcome to Emergy, your emergency management system.\n\n                        Please select your action:\n                                  [1] Login\n                             [CTRL+C] "
                "Quit Program\n\n")
            if choice not in ('1'):  # ,"Q","q"):
                print("Invalid choice. Please try again.")
                self.start()
            elif choice == '1':
                self.verify_user()
                loading = "\n                     =====█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀=====                     \n                     =====█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█=====                     "
                bar = "                     ████████████████████████████████████"

                print(loading)
                for c in bar:
                    time.sleep(0.03)
                    print(c, end="", flush=True)
                    #sys.stdout.write(c)
                    #sys.stdout.flush()
                print("\n\n")
                self.menu_options()
            # elif choice == "Q" or choice =='q':
            # quit()
        except KeyboardInterrupt:
            print("\n############################################################################")
            quit()

    def verify_user(self):
        try:
            if os.path.exists("admin.csv") and os.path.exists("volunteers.csv"):
                ad_data = pandas.read_csv("admin.csv")
                vol_data = pandas.read_csv("volunteers.csv")
                df1 = pandas.DataFrame(ad_data)
                df2 = pandas.DataFrame(vol_data)
                df2['login'] = False
                df2.to_csv("volunteers.csv", index=False)

                print(
                    "\n============================𝖤𝖭𝖳𝖤𝖱 𝖸𝖮𝖴𝖱 𝖫𝖮𝖦𝖨𝖭 𝖣𝖤𝖳𝖠𝖨𝖫𝖲==========================")
                username = input("                            Username: ")

                password = input("                            Password: ")

                if len(df1[(df1.username == username) & (df1.password == password)]) > 0:
                    d2 = df1[(df1.username == username) & (df1.password == password)]
                    self.mode = d2['status'].values[0]
                    self.username = d2['username'].values[0]

                elif len(df2[(df2.username == username) & (df2.password == password)]) > 0:
                    d2 = df2[(df2.username == username) & (df2.password == password)]
                    self.mode = d2['status'].values[0]
                    self.active = d2['active'].values[0]
                    self.username = d2['username'].values[0]
                    Volunteer.edit_info(self.username, "login", True)

                else:
                    print('\nInvalid username and/or password. Please try again or press 𝗖𝗧𝗥𝗟 + 𝗖 to exit: \n')
                    self.verify_user()
            else:
                ad_data = pandas.read_csv("admin.csv")
                df1 = pandas.DataFrame(ad_data)

                username = input("Username: ")
                # if username == "q" or username == "Q":
                # exit()

                password = input("Password: ")

                if len(df1[(df1.username == username) & (df1.password == password)]) > 0:
                    d2 = df1[(df1.username == username) & (df1.password == password)]
                    self.mode = d2['status'].values[0]
                    self.username = d2['username'].values[0]

                else:
                    print('\nInvalid username and/or password. Please try again or press 𝗖𝗧𝗥𝗟 + 𝗖 to exit: \n')
                    self.verify_user()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            self.start()

    def menu_options(self):
        if self.mode == "admin":
            self.display_admin_menu()
        elif self.mode == "volunteer":
            self.display_volunteer_menu()
        else:
            print("\n==============================YOU ARE LOGGED OUT===============================")

    def display_admin_menu(self):  # tested
        try:
            print(
                "\n=================█░█ █▀▀ █░░ █░░ █▀█ ░   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█==================\n=================█▀█ ██▄ █▄▄ █▄▄ █▄█ █   █▀█ █▄▀ █░▀░█ █ █░▀█==================")
            print("\n=====================================𝖬𝖤𝖭𝖴=====================================")
            print("[1] Create or update emergency plan\n"
                  "[2] Close emergency plan\n"
                  "[3] Display emergency\n"
                  "[4] Register volunteer\n"
                  "[5] Deactivate volunteer\n"
                  "[6] Activate volunteer\n"
                  "[7] Delete volunteer\n"
                  "[8] Create/update camps\n"
                  "[9] Message board\n"
                  "[10] Log out\n")
            # "[Q] Exit\n")
            Session.check_volunteer_endDate()
            choice = input("Please choose an option: ")
            if choice == '1':
                self.admin_create_emergency()
                self.menupage()
            elif choice == '2':  # to be tested
                if os.path.exists("emergencies.csv"):
                    self.admin_close_emergency()
                    self.menupage()
                else:
                    print("No records available.")
                    self.menupage()
            elif choice == '3':
                if os.path.exists("emergencies.csv"):
                    self.admin_display_emergency()
                    self.menupage()
                else:
                    print("No records available.")
                    self.menupage()
            elif choice == '4':
                self.admin_register_volunteer()
                self.menupage()
            
            elif choice == '5':
                if os.path.exists("volunteers.csv"):
                    self.admin_deactivate_volunteer()
                    self.menupage()
                else:
                    print("No volunteers are currently registered.")
                    self.menupage()
            elif choice == '6':
                self.admin_activate_volunteer()
                self.menupage()
            elif choice == "7":
                self.admin_delete_volunteer()
                self.menupage()
            elif choice == '8':
                try:
                    print(
                        "\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
                    create_Camp()
                    self.display_admin_menu()
                except KeyboardInterrupt:
                    print("\n############################################################################")
                    session = Session()
                    session.mode = 'admin'
                    session.username = 'admin'
                    session.display_admin_menu()
            elif choice == "9":
                self.admin_message_board()  ####################
                self.menupage()
            elif choice == '10':
                confirm = input("Are you sure you want to log out? (Y/N)\n")
                if confirm == 'Y' or confirm == 'y':
                    self.logout()
                else:
                    self.display_admin_menu()
            # elif choice == 'q' or choice == "Q":
            # exit()
            else:
                print("Invalid choice. Please try again\n")
                self.display_admin_menu()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def display_volunteer_menu(self):  # tested
        try:
            if not self.active:
                print("Your account has been deactivated. Please contact the administrator.")
                self.verify_user()
            else:
                print(
                    "\n=======================█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀========================\n=======================▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄========================")
                print("\n====================================𝖬𝖤𝖭𝖴=====================================")
                print("[1] Update your information\n"
                      "[2] Add refugees\n"
                      "[3] Update camp details\n"
                      "[4] Message board\n"
                      "[5] Log out\n")
                # "[Q] Exit\n")
                choice = input("Please choose an option: ")
                if choice == '1':
                    self.volunteer_edit_info()
                    self.menupage()
                elif choice == '2':
                    self.volunteer_create_profile()
                    self.menupage()
                elif choice == '3':
                    try:
                        print(
                            "\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
                        Update_Camp()
                        self.display_volunteer_menu()
                    except:
                        print("\n############################################################################")
                        session = Session()
                        session.resetSession()
                        session.display_volunteer_menu()
                elif choice == "4":
                    self.vol_message_board()
                    self.menupage()
                elif choice == '5':
                    confirm = input("Are you sure you want to log out? (Y/N)\n")
                    if confirm == 'Y' or confirm == 'y':
                        self.logout()
                    else:
                        self.display_volunteer_menu()
                # elif choice == 'q' or choice == "Q":
                # exit()
                else:
                    print("Invalid choice.\n")
                    self.display_volunteer_menu()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.resetSession()
            session.display_volunteer_menu()

    @staticmethod
    def admin_create_emergency():  # tested
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            print("Please specify what function you would like\n"
                  "[1] create emergency\n"
                  "[2] update emergency\n")
            choice = input("Please choose an option: ")
            if choice == '1':
                try:
                    print(
                        "\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
                    kind = input("Enter the type of the emergency: ")
                    desc = input("Enter description: ")
                    area = input("Enter the affected area: ")
                    Admin.create_emergency(kind, desc, area)
                except KeyboardInterrupt:
                    print("\n############################################################################")
                    session = Session()
                    session.admin_create_emergency()

            elif choice == '2':
                try:
                    Emergency.update_emergencyPlan()
                except KeyboardInterrupt:
                    print("\n############################################################################")
                    session = Session()
                    session.admin_create_emergency()
            else:
                print("Please input the correct number.\n")
                Session.admin_create_emergency()

        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    @staticmethod
    def admin_register_volunteer():  # tested
        ## make sure username is unique before entering other information (session.py)
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            username_exist = True
            while username_exist:
                username = input("Enter username of the new volunteer: ")
                if not Volunteer.volunteers.empty:
                    usernames = Volunteer.volunteers['username']
                    for l in usernames:
                        if l == username:
                            print('The username already exists')
                            username_exist = True
                            break
                    else:
                        username_exist = False
                        print("The username is available, continue entering necessary information")
                        password = input("Enter their password: ")
                        first_name = input("First name: ")
                        last_name = input("Last name: ")
                        while True:  # Loop continuously
                            phone = input("Phone number: ")
                            if phone.isdigit():
                                break
                            else:
                                print("Incorrect phone type.Please try again")
                        camp_data = pandas.read_csv("Camp.csv")
                        df1 = pandas.DataFrame(camp_data)
                        while True:  # Loop continuously
                            camp = input("Camp: ")
                            if (df1['camp'] == camp).any():
                                break
                            else:
                                print("Camp not recognized.Please try again")
                        avail_startDate = "{0:%d/%m/%Y}".format(datetime.date.today())
                        input_endDate_again = True
                        while input_endDate_again:
                            input_endDate = input("End Date(DD/MM/YYYY):")
                            try:
                                avail_endDate = datetime.datetime.strptime(input_endDate, '%d/%m/%Y').strftime(
                                    '%d/%m/%Y')
                                if datetime.datetime.strptime(avail_startDate, '%d/%m/%Y') > datetime.datetime.strptime(
                                        avail_endDate, '%d/%m/%Y'):
                                    print('"End Date" is not correct.Please Input "End Date" again.')
                                    input_endDate_again = True
                                else:
                                    print('\n \033[1m' + 'Volunteer created' + '\033[0m')
                                    Admin.register_volunteer(username, password, first_name, last_name, phone, camp,
                                                             avail_startDate, avail_endDate)
                                    input_endDate_again = False
                            except:
                                print("Input Date is wrong format.Please input 'End Date' again")
                                input_endDate_again = True

                else:
                    username_exist = False
                    password = input("Enter their password: ")
                    first_name = input("First name: ")
                    last_name = input("Last name: ")
                    phone = input("Phone number: ")
                    camp = input("Camp: ")
                    if camp != "Linda":
                        print("Please choose a correct camp")
                    avail_startDate = "{0:%d/%m/%Y}".format(datetime.date.today())
                    input_endDate_again = True
                    while input_endDate_again:
                        input_endDate = input("End Date(day/month/year):")
                        try:
                            avail_endDate = datetime.datetime.strptime(input_endDate, '%d/%m/%Y').strftime('%d/%m/%Y')

                            if datetime.datetime.strptime(avail_startDate, '%d/%m/%Y') > datetime.datetime.strptime(
                                    avail_endDate, '%d/%m/%Y'):
                                print('"End Date" is not correct.Please Input "End Date" again.')
                                input_endDate_again = True
                            else:
                                print('\n \033[1m' + 'Volunteer created' + '\033[0m')
                                Admin.register_volunteer(username, password, first_name, last_name, phone, camp,
                                                         avail_startDate, avail_endDate)
                                input_endDate_again = False
                        except:
                            print("Input Date is wrong format.Please input 'End Date' again")
                            input_endDate_again = True
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def admin_display_emergency(self):  # tested
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            print("Would you like to:\n"
                  "[1] Display all emergencies\n"
                  "[2] Display chosen emergencies\n")
            choice = input("Please choose an option: ")
            if choice == "1":
                data = pandas.read_csv("emergencies.csv")
                df = pandas.DataFrame(data)
                print(df.to_string())

            elif choice == "2":
                kind = input("Enter a type of the emergency: ").lower()
                area = input("Enter the affected area: ").lower()
                data = pandas.read_csv("emergencies.csv")
                df = pandas.DataFrame(data)
                res = df[df['kind'].str.contains('.*' + kind + '.*')]
                results = res[res['area'].str.contains('.*' + area + '.*')]
                if results.empty:
                    print("No such record found.")
                else:
                    print(results.to_string())
            else:
                print("Invalid choice. Please try again\n")
                self.admin_display_emergency()

        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def admin_close_emergency(self):
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            data = pandas.read_csv("emergencies.csv")
            df = pandas.DataFrame(data)
            answer = input("Do you know the ID number of the record you want to close? Y/N: ")
            if answer == "y" or answer == "Y":
                try:
                    index = int(input("Enter the ID number: "))
                    set_endDate = input("Enter the closing date: ")
                    data.iloc[index, data.columns.get_loc('endDate')] = set_endDate
                    data.to_csv("emergencies.csv", index=False)
                    print("Record updated")
                except ValueError:
                    print("Invalid value entered. Try again\n")
                    self.admin_close_emergency()
            elif answer == "n" or answer == "N":
                kind = input("Enter the kind of the emergency: ").lower()
                area = input("Enter the area affected: ").lower()
                res = df[df['kind'].str.contains('.*' + kind + '.*')]
                results = res[res['area'].str.contains('.*' + area + '.*')]
                # if results is not empty, proceed, otherwise inform and cease
                if results.empty:
                    print("No such records found.")
                else:
                    print(results.to_string())

                    try:
                        index = int(input("Choose ID number from the records listed above: "))
                        # check that index given belongs in results
                        if index in results.index:
                            result = df.iloc[[index]]
                            print(result)
                            set_endDate = input("Enter the closing date: ")
                            Admin.close_emergency(index, set_endDate)  # all good
                            print("Record updated")
                        else:
                            print("Data given does not fit any records.")
                    except ValueError:
                        print("Invalid ID number.")
                        self.admin_close_emergency()
            else:
                print("Invalid answer.\n")
                self.admin_close_emergency()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def admin_deactivate_volunteer(self):  # tested
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            user = input("Enter the username of the volunteer: ")
            if Admin.deactivate_volunteer(user):
                print("Account was deactivated.")
            else:
                print("User not found. Try again\n")
                self.admin_deactivate_volunteer()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def admin_activate_volunteer(self):  # tested
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            user = input("Enter the username of the volunteer: ")
            if Admin.activate_volunteer(user):
                print("Account was activated.")
            else:
                print("User not found. Try again\n")
                self.admin_activate_volunteer()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def volunteer_edit_info(self):  # tested
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            user = self.username
            vol_data = pandas.read_csv("volunteers.csv")
            df = pandas.DataFrame(vol_data)

            print("Please specify what information you would like to edit: \n"
                  "[1] First name\n"
                  "[2] Last name\n"
                  "[3] Password\n"
                  "[4] Phone number\n"
                  "[5] Availability(Start Date)\n"
                  "[6] Availability(End Date)\n")
            choice = input("Enter your choice: ")

            if choice == '1':
                column = 'firstname'
            elif choice == '2':
                column = 'lastname'
            elif choice == '3':
                column = 'password'
            elif choice == '4':
                column = 'phone'
            elif choice == "5":
                column = 'avail_startDate'
                period = "start"
            elif choice == "6":
                column = 'avail_endDate'
                period = "end"
            else:
                print("Invalid choice.\n")
                self.volunteer_edit_info()

            if choice != '5' and choice != '6':
                new = input("Please type the updated information: ")
                Volunteer.edit_info(user, column, new)  # warning here
                print("Your information has been updated.")
            else:
                input_Date_again = True
                while input_Date_again:
                    input_date = input("Please type the updated date(date/month/year): ")
                    try:
                        inputdate_is_valid = Volunteer.date_is_valid(user, period, input_date)
                        if inputdate_is_valid:
                            print("is valid")
                            new = datetime.datetime.strptime(input_date, '%d/%m/%Y').strftime('%d/%m/%Y')
                            Volunteer.edit_info(user, column, new)  # warning here
                            print("Your information has been updated.")
                            input_Date_again = False
                        else:
                            if choice == '5':
                                print("The start date you have input is greater than end date!!")
                            elif choice == "6":
                                print("The end date you have input is smaller than start date!!")

                    except:
                        print("Input Date is wrong format.Please input again")
                        input_Date_again = True
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.resetSession()
            session.display_volunteer_menu()

    def volunteer_create_profile(self):  # tested
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            print("Please enter the refugee details:\n")
            firstName = input("First name of the refugee family leader: ")
            lastName = input("Last name of the family leader: ")

            data = pandas.read_csv("volunteers.csv")
            camp = data.loc[data['username'] == self.username, 'camp'].values[0]
            print("Camp:", camp)

            condition = input("Please outline any health concerns: ")
            try:
                dependants = int(input("Number of dependants, including the family leader: "))
                data2 = pandas.read_csv("Camp.csv")
                num = data2.loc[data2['camp'] == camp, 'nums'].values[0]
                num = num + dependants
                print("New numbers at camp:", camp, ":", num)
                data2.loc[data2['camp'] == camp, 'nums'] = num
                data2.to_csv('Camp.csv', index=False)

                Volunteer.create_profile(firstName, lastName, camp, condition, dependants)
                ans = input("Your new record has been created. Do you want to view the refugee table?")
                if ans == "Y" or ans == "y":
                    refugees = pandas.read_csv("refugees.csv")
                    print(refugees)
            except ValueError:
                print("Invalid data. Please try again\n")
                self.volunteer_create_profile()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.resetSession()
            session.display_volunteer_menu()

    def logout(self):
        if self.mode == "volunteer":
            Volunteer.edit_info(self.username, "login", False)
        self.mode = None
        self.username = None
        self.active = None
        Session.print_logo()
        self.start()

    def resetSession(self):
        vol_data = pandas.read_csv("volunteers.csv")
        df = pandas.DataFrame(vol_data)
        d2 = df.loc[df.login == True]
        self.mode = 'volunteer'
        self.username = d2['username'].values[0]
        self.active = d2['active'].values[0]

    def menupage(self):
        print("\n=======================================")
        cont = input("\nPress any key and 'Enter' to return to menu.")
        while cont:
            if self.mode == "admin":
                self.display_admin_menu()
            else:
                self.display_volunteer_menu()

    def admin_message_board(self):
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            if not os.path.exists("messages.csv"):
                messages = pandas.DataFrame(columns=["author", "time", "to", "subject", "text", "private"])
                messages.to_csv("messages.csv")

            df = pandas.read_csv("messages.csv")

            df['time'] = pandas.to_datetime(df['time'], format='%d/%m/%Y %H:%M')

            if df.empty:
                print("No messages.")
            else:
                # Get public messages from the last week
                today = datetime.datetime.today()
                week_ago = today - datetime.timedelta(days=7)
                new_messages = df[(df['time'] > week_ago) & (df['private'] == False)]
                if new_messages.empty:
                    print("There are no new messages.")
                else:
                    for index, row in new_messages.iterrows():
                        author = row["author"]
                        time = row["time"].strftime("%d/%m/%Y %H:%M")
                        text = row["text"]
                        print(f"{author} ({time}): {text}")

            choice = input(
                "[1] Leave a public board message\n[2] See your private messages\n[3] Send a private message\n"
                )  # "[4] Back to main menu\n")
            try:
                if choice == "1":
                    new_mess = input("Enter the message: ")
                    Message(self.username, new_mess)
                elif choice == "2":
                    private = df[(df['to'] == self.username) & (df['private'] == True)]
                    if private.empty:
                        print("You have no messages.")
                    else:
                        for index, row in private.iterrows():
                            author = row["author"]
                            time = row["time"].strftime("%d/%m/%Y %H:%M")
                            subject = row['subject']
                            text = row["text"]
                            print(f"From: {author}\nOn: {time}\nSubject line: {subject}\n{text}")
                elif choice == "3":
                    if not os.path.exists("volunteers.csv"):
                        print("No volunteers are currently registered.")
                    else:

                        receiver = input("Username of the addressee: ")
                        # checking if receiver exists in volunteers.csv
                        vdf = pandas.read_csv("volunteers.csv")
                        adf = pandas.read_csv("admin.csv")
                        if receiver not in vdf['username'].values and receiver not in adf['username'].values:
                            print("No such person in the contact book.")
                            self.admin_message_board()
                        else:
                            subject = input("Subject line: ")
                            text = input("Message: ")
                            Message(self.username, text, to=receiver, subject=subject, private=True)
                # elif choice == "4":
                # self.menu_options()
                else:
                    print("Invalid choice.")
            except KeyboardInterrupt:
                print("\n############################################################################")
                session = Session()
                session.mode = 'admin'
                session.username = 'admin'
                session.admin_message_board()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.mode = 'admin'
            session.username = 'admin'
            session.display_admin_menu()

    def vol_message_board(self):
        try:
            print("\n===========================𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 𝗘𝗫𝗜𝗧============================")
            if not os.path.exists("messages.csv"):
                messages = pandas.DataFrame(columns=["author", "time", "to", "subject", "text", "private"])
                messages.to_csv("messages.csv")

            df = pandas.read_csv("messages.csv")

            df['time'] = pandas.to_datetime(df['time'], format='%d/%m/%Y %H:%M')

            if df.empty:
                print("No messages.")
            else:
                # Get public messages from the last week
                today = datetime.datetime.today()
                week_ago = today - datetime.timedelta(days=7)
                new_messages = df[(df['time'] > week_ago) & (df['private'] == False)]
                if new_messages.empty:
                    print("There are no new messages.")
                else:
                    for index, row in new_messages.iterrows():
                        author = row["author"]
                        time = row["time"].strftime("%d/%m/%Y %H:%M")
                        text = row["text"]
                        print(f"{author} ({time}): {text}")

            choice = input(
                "[1] Leave a public board message\n[2] See your private messages\n[3] Send a private message\n"
                )  # "[4] Back to main menu\n")
            try:
                if choice == "1":
                    new_mess = input("Enter the message: ")
                    Message(self.username, new_mess)
                elif choice == "2":
                    private = df[(df['to'] == self.username) & (df['private'] == True)]
                    if private.empty:
                        print("You have no messages.")
                    else:
                        for index, row in private.iterrows():
                            author = row["author"]
                            time = row["time"].strftime("%d/%m/%Y %H:%M")
                            subject = row['subject']
                            text = row["text"]
                            print(f"From: {author}\nOn: {time}\nSubject line: {subject}\n{text}")
                elif choice == "3":
                    if not os.path.exists("volunteers.csv"):
                        print("No volunteers are currently registered.")
                    else:

                        receiver = input("Username of the addressee: ")
                        # checking if receiver exists in volunteers.csv
                        vdf = pandas.read_csv("volunteers.csv")
                        adf = pandas.read_csv("admin.csv")
                        if receiver not in vdf['username'].values and receiver not in adf['username'].values:
                            print("No such person in the contact book.")
                            self.vol_message_board()
                        else:
                            subject = input("Subject line: ")
                            text = input("Message: ")
                            Message(self.username, text, to=receiver, subject=subject, private=True)
                # elif choice == "4":
                # self.menu_options()
                else:
                    print("Invalid choice.")
            except KeyboardInterrupt:
                print("\n############################################################################")
                session = Session()
                session.resetSession()
                session.vol_message_board()
        except KeyboardInterrupt:
            print("\n############################################################################")
            session = Session()
            session.resetSession()
            session.display_volunteer_menu()

    @staticmethod
    def check_volunteer_endDate():
        current_Date = datetime.datetime.today()
        data = pandas.read_csv("volunteers.csv")
        df = pandas.DataFrame(data)
        list_of_endDate = list(set(df['avail_endDate']))
        if len(list_of_endDate) != 0:
            alertmsg=""
            for i in list_of_endDate:
                if datetime.datetime.strptime(i, '%d/%m/%Y') < current_Date:
                    query = df[(df['avail_endDate'] == i) & (df['active'] == True)]
                    for incorrect_status_username in list(set(query['username'])):
                            alertmsg+=f"\033[1;34;50m Please note that volunteer {incorrect_status_username} is no longer available. You may wish to confirm/deactivate. \033[1;0;50m \n"
            if len(alertmsg)!=0:
                alertmsg="\033[1;34;50m ALERT: \n \033[1;0;50m \n"+alertmsg 
                print(alertmsg)

        camps_data = pandas.read_csv("Camp.csv")
        cdf = pandas.DataFrame(camps_data)
        messages = []
        for index, row in cdf.iterrows():
            camp = row['camp']
            subset = cdf.iloc[[index]].to_string()
            if "poor" in subset.lower() or "needed" in subset.lower() or "few" in subset.lower() or "none" in subset.lower():
                messages.append(f"\033[1;34;50m Camp {camp} is in need of additional resources. \033[1;0;50m")
            
        if len(messages) > 0:
            print(f"\033[1;34;50m URGENT:\033[1;0;50m \n")
            for mess in messages:
                print(mess)
    @staticmethod
    def admin_delete_volunteer():
        vol_username = input("Enter the username of volunteer:")
        data = pandas.read_csv("volunteers.csv")
        df = pandas.DataFrame(data)
        res = df[df.username != vol_username]
        res.to_csv("volunteers.csv")

        




        
