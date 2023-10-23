import json
import requests.exceptions
import analysis
import requests
from bs4 import BeautifulSoup


def menu():
    print("Please Enter a test URL. If you want to exit type 1.")


def menu2():
    print("If you want you can add another test url and compare it against the first url test or:")
    print("1.- Analyze test.")
    print("2.- Exit.")


def get_option():
    o = input("Enter a Geekbench5 test url: ")
    return o


def get_url(url):
    t = url
    url = t + ".gb5"
    with requests.Session() as session:
        page = session.get("https://browser.geekbench.com/session/new")
        for cookie in page.cookies:
            print("cookie domain = " + cookie.domain)
            print("cookie domain = " + cookie.name)
            print("cookie domain = " + cookie.value)
            print("----------------------------------------")
            
        html = BeautifulSoup(page.content, "html.parser")
        csrf_token = html.find("input", {"name": "authenticity_token"})["value"]
        data_to_login = {'utf8': "✓",
                         "authenticity_token": csrf_token,
                         "user[username]": "tt7562905",
                         "user[password]": "testtest",
                         "commit": "Log in"
                         }
        r = session.post("https://browser.geekbench.com/session/create", data_to_login)
        for cookie in r.cookies:
            print("cookie domain r = " + cookie.domain)
            print("cookie domain r = " + cookie.name)
            print("cookie domain r = " + cookie.value)
            print("----------------------------------------")
        t = session.get(url)
        for cookie in t.cookies:
            print("cookie domain t = " + cookie.domain)
            print("cookie domain t = " + cookie.name)
            print("cookie domain t = " + cookie.value)
            print("----------------------------------------")
        dict = json.loads(t.text)

    return dict


print("")
print("-----------------------------------------------")
print(" ----- Welcome to the Geekbench5 test app ----- ")
print("-----------------------------------------------")
print("")
try:
    exit = False
    while not exit:
        menu()
        option = get_option()
        print("")
        if str(option) == str(1):
            print(" --- Good buy :), see you next time --- ")
            print("")
            exit = True
        elif type("") == type(option):
            try:
                print("Ok, processing data... ", end="")
                o = get_url(option)
                print("OK")
                exit2 = False
                while not exit2:
                    print("")
                    menu2()
                    option2 = get_option()
                    test_1 = analysis.tests(o)
                    print("")
                    if str(option2) == str(1):
                        print("")
                        test_1.print_important_analysis()
                        exit2 = True
                    elif str(option2) == str(2):
                        print("")
                        exit2 = True
                    elif type("") == type(option2):
                        try:
                            u = get_url(option2)
                            test_2 = analysis.tests(u)
                            test_1.print_compare(test_2)
                            exit2 = True
                        except requests.exceptions.MissingSchema:
                            print("Given url is not valid")
                            print("")
            except requests.exceptions.MissingSchema:
                print("Given url is not valid")
                print("")
        else:
            print(" -- The selected option is not available -- ")
            print("")
    input()
except KeyboardInterrupt:
    print("")
    print(" --- The user force the program exit --- ")
    print(" --- Good buy :), see you next time --- ")
    print("")
    input()
