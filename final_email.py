from os import write
import random
import requests
import json
import re
from bs4 import BeautifulSoup as bs
import threading
import time

unverified_email = []

# ---------------------- RANDOM DATA GENERATE ----------------------
name_list = ["Sky", "Reyansh", "Mohammad", "Vivaan", 'Rhoda', 'Report', 'Augusta', 'Wind', 'Chris', 'Anthe', 'Claude', 'Strophobia', 'Anne', 'Gloindian', 'Dulcie', 'Veeta', 'Abby', 'Normal'
             "Ayaan", "Vihaan", "Atharv", "Sai", "Advik", "Arjun"'Patty', 'OFurniture', 'Paddy', 'OFurniture', 'Olive', 'Yew', 'Aida', 'Bugg', 'Maureen', 'Biologist', 'Teri', 'Dactyl', 'Peg', 'Legge', 'Allie', 'Grater', 'Liz', 'Erd', 'Mused',
             'Constance', 'Noring', 'Lois', 'Nominator', 'Minnie', 'Van', 'Ryder', 'Lynn', 'OLeeum', 'Ann', 'ORecital', 'Ray', 'OSun', 'Lee', 'Sun', 'Ray', 'Sin', 'Isabelle', 'Ringing', 'Eileen', 'Sideways', 'Rita', 'Book', 'Paige', 'Turner',
             'mum', 'Anne', 'Teak', 'Nice', 'Anita', 'Bath', 'Harriet', 'Upp', 'Tired', 'Missy', 'Ewe', 'Ivana', 'Withew', 'Anita', 'Letterback', 'Hope', 'Furaletter', 'Homesoon', 'Bea', 'Mine', 'Bess', 'Twishes', 'Yasoon', 'Audie', 'Yose',
             'End', 'Amanda', 'Hug', 'Ben', 'Dover', 'Eileen', 'Dover', 'Willie', 'Makit', 'Willie', 'Findit', 'Skye', 'Blue', 'Staum', 'Clowd', 'Addie', 'Minstra', 'Anne', 'Ortha', 'Dave', 'Allippa', 'Dee', 'Zynah', 'Hugh', 'Mannerizorsa',
             'Loco', 'Lyzayta', 'Manny', 'Jah', 'Mark', 'Ateer', 'Reeve', 'Ewer', 'Tex', 'Ryta', 'Theresa', 'Green', 'Barry', 'Kade', 'Stan', 'Dupp', 'Neil', 'Down', 'Con', 'Trariweis', 'Don', 'Messwidme', 'Annon', 'Anna', 'Domino', 'Clyde',
             'Stale', 'Anna', 'Logwatch', 'Anna', 'Littlical', 'Norma', 'Leigh', 'Absent', 'Sly', 'Meebuggah', 'Saul', 'Goodmate', 'Faye', 'Clether', 'Sarah', 'Moanees', 'Ayelloribbin', 'Hugo', 'First', 'Percy', 'Vere', 'Jack', 'Aranda', 'Olive',
             'Tree', 'Fran', 'Pani', 'John', 'Quil', 'Lasting', 'Anne', 'Thurium', 'Cherry', 'Blossom', 'Glad', 'Oli', 'Ginger', 'Plant', 'Del', 'Phineum', 'Rose', 'Bush', 'Perry', 'Scope', 'Frank', 'Stein', 'Roy', 'Commishun', 'Pat', 'Thettick',
             'Percy', 'Kewshun', 'Rod', 'Knee', 'Hank', 'Cheef', 'Bridget', 'Theriveaquai', 'Pat', 'Toffis', 'Karen', 'Onnabit', 'Col', 'Fays', 'Fay', 'Daway', 'Joe', 'Awl', 'Wes', 'Yabinlatelee', 'Colin', 'Sik', 'Greg', 'Arias', 'Toi', 'Story',
             'Gene', 'Eva', 'Convenshun', 'Jen', 'Tile', 'Simon', 'Sais', 'Peter', 'Owt', 'Hugh', 'Cry', 'Lee', 'Nonmi', 'Lynne', 'Gwafranca', 'Art', 'Decco', 'Lynne', 'Gwistic', 'Polly', 'Ester', 'Undawair', 'Oscar', 'Nommanee', 'Laura',
             'Biding', 'Laura', 'Norda', 'Des', 'Ignayshun', 'Mike', 'RoweSoft', 'Anne', 'Kwayted', 'Wayde', 'Thabalanz', 'Dee', 'Mandingboss', 'Sly', 'Meedentalfloss', 'Stanley', 'Knife', 'Wynn', 'Dozeaplikayshun', 'Mal', 'Ajusted', 'Penny',
             'Black', 'Mal', 'Nurrisht', 'Polly', 'Pipe', 'Polly', 'Wannakrakouer', 'Con', 'Staninterupshuns', 'Fran', 'Tick', 'Santi', 'Argo', 'Carmen', 'Goh', 'Carmen', 'Sayid', 'Norma', 'Stitts', 'Ester', 'Vista', 'Manuel', 'Labor', 'Ivan',
             'Itchinos', 'Ivan', 'Notheridiya', 'Mustafa', 'Leek', 'Emma', 'Grate', 'Annie', 'Versaree', 'Tim', 'Midsaylesman', 'Mary', 'Krismass', 'Tim', 'Buck', 'Too', 'Lana', 'Lynne', 'Creem', 'Wiley', 'Waites', 'Leeva', 'Cayshun', 'Anne', 'Dote'
             ]

domains = ["getnada.com", "abyssmail.com", "boximail.com", "clrmail.com", "dropjar.com",
           "getairmail.com", "givmail.com", "inboxbear.com", "tafmail.com", "zetmail.com", "vomoto.com"]


def random_name(): return random.choice(name_list)
def random_domain(): return random.choice(domains)
def random_no(): return random.randint(0, 1000)


def random_email():
    return f"{random_name().lower()}{random_no()}@{random_domain()}"


def random_password():
    return "".join(re.findall(r"[a-z0-9#$@]+", string="".join([chr(random.randint(
        35, 122)) for _ in range(10)]), flags=re.IGNORECASE))+"".join([chr(random.randint(65, 97)) for _ in range(5)])

# -------------------------------------------------- RANDOM GENERATE END ----------------------------------------------------


def account_generator(name, email, password):
    data_dict = {}
    s = requests.session()
    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyBkg818dO-7AeiVqDFIqcyF2FSrBV4-vlE'
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": "true"
    }
    key_s = {
        "key": "AIzaSyBkg818dO-7AeiVqDFIqcyF2FSrBV4-vlE"}

    response = s.post(url=url, json=data, params=key_s)
    store = response.json()

    new_data = {"idToken": store['idToken'],
                "displayName": name, "returnSecureToken": "true"}

    sign_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/setAccountInfo?key=AIzaSyBkg818dO-7AeiVqDFIqcyF2FSrBV4-vlE'

    responce2 = s.post(url=sign_url, json=new_data)
    if responce2.status_code == 200:
        temp = {
            "name": name,
            "email": email,
            "pass": password
        }
        login_veri(name, email, password, responce2.json()["localId"])
        global unverified_email
        unverified_email.append(email)

        print(f"success : {name} {email} {password}")
        return temp
    else:
        print('fail')
        return None


def get_nada_verify(email):
    time.sleep(1)
    url = f"https://getnada.com/api/v1/inboxes/{email}"
    uuid = requests.get(url=url).json()["msgs"][0]["uid"]
    html_url = f"https://getnada.com/api/v1/messages/html/{uuid}"
    responce = requests.get(url=html_url)
    soup_url = bs(responce.content, "lxml").find("a")["href"]
    print(soup_urln, "\n")
    #data = link_para(link=soup_url)
    #requests.get(url=soup_url, params=data)


def login_veri(name, email, password, userid):
    temp_data = {"SocialName": "Email",
                 "UserUID": userid,
                 "ExternalSocialId": email,
                 "FullName": name,
                 "Email": email,
                 "UserName": name,
                 "ProfilePicURL": "null",
                 "IsEmailVerified": "false",
                 "AdditionalOrganizationURLToBePartOf": "lidoma-gaming"}
    new_s = requests.session()
    login_url = "https://platform.gogamers.tech/api/User/SignUpOrLogIn"
    new_s.post(url=login_url, json=temp_data)
    url = "https://platform.gogamers.tech/api/Communication/GetEmailConfiguration/lidoma-gaming"
    res_url_204 = "https://us-central1-go-gamers-tech.cloudfunctions.net/resendEmailVerificationCallable"
    new_s.get(url=url)
    new_s.options(url=res_url_204)
    ver_data = {"data": {"host": {"email": "info@gogamers.tech", "host": "smtp.office365.com", "port": "587", "name": "Lidoma Gaming", "password": "U2FsdGVkX1/37IyLeLTL3made7+hsZaIt5DA37ouQbo=", "appId": "62655ef2-79eb-46b2-ad1f-0e225f4a1855"}, "displayName": name, "email": email, "redirect": "https://platform.gogamers.tech/", "resendUsingGGIfFail": "true",
                         "theme": {"name": "Lidoma Gaming", "accentColor": "#9d6ec8", "accentTextColor": "#ffffff", "primaryColor": "#000000", "primaryTextColor": "#ffffff", "logo": "https://firebasestorage.googleapis.com/v0/b/go-gamers-tech.appspot.com/o/theme%2F1617298753007?alt=media&token=9db45b16-39e4-4bdd-bca6-6bd56408b87c", "backgroundColor": "#131416", "textColor": "#ffffff"}}}
    new_s.post(url=res_url_204, json=ver_data)


def do_work(T=10):
    final_data = {}
    for i in range(T):
        data = account_generator(
            name=random_name(), email=random_email(), password=random_password())

    # -------- Uncomment below if you want to save to file
        # if data != None:
        #    final_data[f"id_{i}"] = data
    # with open("text.json","w") as f:
    #   f.write(str(data))


def link_para(link=""):
    link = "https://go-gamers-tech.firebaseapp.com/__/auth/action?apiKey=AIzaSyBkg818dO-7AeiVqDFIqcyF2FSrBV4-vlE&mode=verifyEmail&oobCode=DR8X5y-txnMAp_byk1jfcw9jNTJWlgmJGmjaeHwZFTYAAAF5ifLPvA&continueUrl=https://platform.gogamers.tech/&lang=en"
    linklist = link.split("?")[1]
    return linklist


if __name__ == "__main__":
    # uncomment below if user dont want to use threading
    #do_work(T=int(input("Enter total no. of acc. : ")))

    # ----- Threading if user want to fasten the process
    total_threads = 10
    threads = []
    for i in range(total_threads):
        t = threading.Thread(target=do_work)
        t.daemon = True
        threads.append(t)
    for i in range(total_threads):
        threads[i].start()
    for i in range(total_threads):
        threads[i].join()

    # ----- VERIFICATION LINK
    print("\nWAITING 30sec before getting links\n-----------------------------------\n")
    time.sleep(30)
    for email in unverified_email:
        try:
            get_nada_verify(email)
        except Exception:
            print(f"fail to get link of : {email}\n")
