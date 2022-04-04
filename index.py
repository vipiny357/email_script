from typing import Dict
import yagmail
import itertools
import pandas as pd
import os
import numpy as np
from pathlib import Path

path_of_excel=r"C:/Users/Vipin Kumar Yadav/Desktop/email script/list.xlsx"
df = pd.read_excel (path_of_excel)

df["Fname"] = df["Name"] +" "+ df["Lname"]

list1 = list(df['Name']) 
list2 = list(df['Lname'])
list3 = list(df['Fname'])
list4 = list(df['Email'])
print(list3)


for (i,j,k,l) in zip(list1,list2,list3,list4):
    # print('name is:'+i+" "+j+" ,email is "+l)


    receiver = l
    sub="Certificate of participation"
    body = "Mr./Ms."+' '+i+' '+j+',\n '+"Thanks for participating in SOlUTIONS 2k21. Hereby attached is your participation certificate.PFA."
    # filename = "C:/Users/MSI/Desktop/cert gen/tunhi/Alan Price.pdf"
   
    paths = Path('C:/Users/Vipin Kumar Yadav/Desktop/email script/tunhi/').glob("**/"+k+".pdf")
    
    for path in paths:
    # because path is object not string
        path_in_str = str(path)
        # Do thing with the path
        # print(('C:/Users/MSI/Desktop/cert gen/tunhi/'+i+'.pdf'))
        if path_in_str == str(Path('C:/Users/Vipin Kumar Yadav/Desktop/email script/tunhi/'+k+'.pdf')):
            print("done and sent for "+k)
            filename = 'C:/Users/Vipin Kumar Yadav/Desktop/email script/tunhi/'+k+'.pdf'
        # print(str(Path('C:/Users/MSI/Desktop/cert gen/tunhi/'+k+'.pdf')))


        yag = yagmail.SMTP('email','password')
        yag.send(
            to=receiver,
            subject=sub,
            contents=body, 
            attachments=filename,
        )
        # print(body)


