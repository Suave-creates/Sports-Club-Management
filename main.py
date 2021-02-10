import pandas as pd
from matplotlib import pyplot as plt
from datetime import date

print("-------------------------WELCOME TO ACE SPORTS CLUB-------------------------")


def add_new_supplement():
    supplement_id = int(input("Enter a supplement id :"))
    supplement_name = input("Enter supplement name :")
    cost = int(input("Enter cost of supplement :"))
    category = input("Enter category of supplement:")
    bdf = pd.read_csv("Supplements.csv")
    n = bdf["supplement_id"].count()
    bdf.at[n] = [supplement_id, supplement_name, cost, category]
    bdf.to_csv("Supplements.csv", index=False)
    print("Supplement Added Successfully :)")
    print(bdf)


def search_supplement():
    supplement_name = input("Enter a Supplement name:")
    bdf = pd.read_csv(r"Supplements.csv")
    df = bdf.loc[bdf["supplement_name"] == supplement_name]
    if df.empty:
        print("No supplement found with given code  :(")
    else:
        print("Supplement details are:")
        print(df)


def delete_supplement():
    supplement_id = float(input("Enter supplement_id:"))
    bdf = pd.read_csv(r"Supplements.csv")
    bdf = bdf.drop(bdf[bdf["supplement_id"] == supplement_id].index)
    bdf.to_csv(r"Supplements.csv", index=False)
    print("Supplement Deleted Successfully ;) ")
    print(bdf)


def show_supplement():
    bdf = pd.read_csv(r"Supplements.csv")
    print(bdf)


def add_new_player():
    player_id = input("Enter Player id :")
    name = input("Enter player name :")
    stage = input("Enter players level:")
    year_of_joining = input("Enter joining Year:")
    bdf = pd.read_csv(r"player.csv")
    n = bdf["player_id"].count()
    bdf.at[n] = [player_id, name, stage, year_of_joining]
    bdf.to_csv(r"player.csv", index=False)
    print("Player added successfully")
    print(bdf)


def search_player():
    name = input("Enter player Name:")
    bdf = pd.read_csv(r"player.csv")
    df = bdf.loc[bdf["player_name"] == name]
    if df.empty:
        print("No player Found")
    else:
        print("Player Details are:")
        print(df)


def delete_player():
    player_id = float(input("Enter Player_id:"))
    bdf = pd.read_csv(r"player.csv")
    bdf = bdf.drop(bdf[bdf["player_id"] == player_id].index)
    bdf.to_csv(r"player.csv", index=False)
    print("Player Deleted Successfully")
    print(bdf)


def show_player():
    bdf = pd.read_csv(r"player.csv")
    print(bdf)


def issue_supplements():
    supplement_name = input("Enter supplement name:")
    bdf = pd.read_csv(r"Supplements.csv")
    bdf = bdf.loc[bdf["supplement_name"] == supplement_name]
    if bdf.empty:
        print("No Supplement found:(")
        return

    p_name = input("Enter player name :")
    mdf = pd.read_csv(r"player.csv")
    mdf = mdf.loc[mdf["player_name"] == p_name]
    if mdf.empty:
        print("No Such Member found:(")
        return

    # delete_of_issue = input("Enter Date of issue:")
    number_of_supplements_issued = int(input("enter  number of supplements issued:"))
    bdf = pd.read_csv(r"issue.csv")
    n = bdf["supplement_name"].count()
    bdf.at[n] = [supplement_name, p_name,
                 date.today(), number_of_supplements_issued, ""]
    bdf.to_csv(r"issue.csv", index=False)
    print("Supplement issued successfully")
    print(bdf)


def return_supplement():
    p_name = input("Enter a player name : ")
    supplement_name = input("Enter supplement Name :")
    idf = pd.read_csv(r"issue.csv")
    idf = idf.loc[idf["supplement_name"] == supplement_name]
    if idf.empty:
        print("The supplement is not issued in the Arsenal")
    else:
        idf = idf.loc[idf["name"] == p_name]
        if idf.empty:
            print("Supplement is not issued to the member:")
        else:
            print("Supplement can be Returned ;)")
            ans = input("Are you sure you want to return the supplement ")
            if ans.lower() == "yes":
                idf = pd.read_csv(r"issue.csv")
                idf = idf.drop(idf[idf["supplement_name"]
                                   == supplement_name].index)
                idf.to_csv(r"issue.csv", index=False)
                print("Supplement Received successfully :)")
            else:
                print("Return operation Unsuccessful")


def show_issued_supplements():
    idf = pd.read_csv(r"issue.csv")
    print(idf)


def delete_issued_supplement():
    supplement_name = input("Enter Supplement Name : ")
    bdf = pd.read_csv(r"issue.csv")
    bdf = bdf.drop(bdf[bdf["supplement_name"] == supplement_name].index)
    bdf.to_csv(r"issue.csv", index=False)
    print("Deleted issued Supplement successfully :) ")
    print(bdf)


def show_charts():
    print("Press 1 - Supplement and their Cost")
    print("Press 2 - Number of Supplements issued by members ")
    char = int(input("Enter you choice: "))
    if char == 1:
        df = pd.read_csv(r"Supplements.csv")
        df = df[["supplement_name", "cost"]]
        df.plot("supplement_name", "cost", kind='bar')
        plt.xlabel('supplement_name---->')
        plt.ylabel('cost---->')
        plt.show()

    if char == 2:
        df = pd.read_csv("issue.csv")
        df = df["number_of_supplements"]
        df.plot(kind='bar', color='red')
        plt.show()


def login():
    uname = input("Enter your name : ")
    pwd = input("Enter your password : ")
    df = pd.read_csv(r"user.csv")
    df = df.loc[df["uname"] == uname]
    if df.empty:
        print("Invalid User Name given :( ")
        return False
    else:
        df = df.loc[df["pwd"] == pwd]
        if df.empty:
            print("Invalid password :(")
            return False
        else:
            print("Username & Password matched Successfully")
            return True
    # if uname in df.uname and pwd in df.pwd:
    #     print("Access Granted")
    # else:
    #     print("Access Denied")


def show_menu():
    print("-----------------------------------------------------------")
    print("                   ACE SPORTS CLUB")
    print("-----------------------------------------------------------")
    print("Press 1  - Add a new Supplement")
    print("Press 2  - Search for a Supplement ")
    print("Press 3  - Delete a Supplement")
    print("Press 4  - Show all Supplement")
    print("Press 5  - Add a New Player")
    print("Press 6  - Search for a Player")
    print("Press 7  - Delete a Player")
    print("Press 8  - Show all Player")
    print("Press 9  - Issue Supplement")
    print("Press 10 - Return Supplement")
    print("Press 11 - Show all Issued Supplements")
    print("Press 12 - Delete a Issued Supplement")
    print("Press 13 - To view Charts")
    print("Press 14 - To exit")
    choice = int(input("Enter your choice:"))
    return choice


if login():
    while True:
        ch = show_menu()
        if ch == 1:
            add_new_supplement()
        elif ch == 2:
            search_supplement()
        elif ch == 3:
            delete_issued_supplement()
        elif ch == 4:
            show_supplement()
        elif ch == 5:
            add_new_player()
        elif ch == 6:
            search_player()
        elif ch == 7:
            delete_player()
        elif ch == 8:
            show_player()
        elif ch == 9:
            issue_supplements()
        elif ch == 10:
            return_supplement()
        elif ch == 11:
            show_issued_supplements()
        elif ch == 12:
            delete_issued_supplement()
        elif ch == 13:
            show_charts()
        elif ch == 14:
            break
        else:
            print("Invalid Option selected :( ")

print("*****THANK YOU FOR VISITING ACE SPORTS CLUB*****")
print(f"Don't forget to give a star on GitHub https://github.com/Suave-creates/Sports-Club-Management/")
