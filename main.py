import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("cred.json", scopes=scope)
client = gspread.authorize(creds)
google_sh = client.open_by_url("https://docs.google.com/spreadsheets/d/12pRWgjmc9BB7W86-uBwD4ibA-Uzn9HsmlfPI3Nlo02A/edit?usp=sharing")
import os
def getData():
 global name, address, regid,i
 print("Enter the data of ", i+1, " student")
 name.insert(i, (input("Enter Name : ")))
 address.insert(i, (input("Enter Address : ")))
 regid.insert(i, (input("Enter Registration Number : ")))
 i += 1
 os.system('cls||clear')

def main():
 os.system('cls||clear')
 print("Enter the number of students")
 n = int(input())
 for i in range(n):
     os.system('cls||clear')
     getData()
 print("uploading data")  
 i = 0
 for i in range(n):
     #serial Number
     j = i + 2
     serialNumber = str(j-1)
     rowId = str(j)
     cellId = str('A'+rowId)
     google_sh.worksheet("Sheet1").update_acell(cellId, serialNumber)
     #Name
     cellId = str('B'+rowId)
     google_sh.worksheet("Sheet1").update_acell(cellId, name[i])
     #Address
     cellId = str('C'+rowId)
     google_sh.worksheet("Sheet1").update_acell(cellId, address[i])
     #Registration Number
     cellId = str('D'+rowId)
     google_sh.worksheet("Sheet1").update_acell(cellId, regid[i])
     i = i + 1
print("Data Uploaded")
print("finished")
print("click here:  https://docs.google.com/spreadsheets/d/12pRWgjmc9BB7W86-uBwD4ibA-Uzn9HsmlfPI3Nlo02A/edit?usp=sharing")
name = []
address = []
regid = []
i= 0

main()
 