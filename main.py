import MySQL_connector
import CSV_reader
import JSON_generator
import PATH_controll
import json
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print('\033[2J'+Fore.YELLOW+Back.RED+"\t\tWelcome to "+Fore.WHITE+Back.RED+"CC_LOGISTICS"+Fore.YELLOW+Back.RED+" csv converter \t\t")

#Convert .csv to json format
datas = json.loads(CSV_reader.csv2json(PATH_controll.csvpath))

#Check shipper information
shipper_id = MySQL_connector.check(datas[0])
if shipper_id:
    print(f"\t\t\t\t...shipper_id[{shipper_id}] already exist!")
else:
    print("\t\t\t\t...shipper_id not exist!")
    shipper_id = MySQL_connector.create_shipper(datas[0])

print("\n"+Fore.YELLOW+Back.RED+"\t\t    Data insert process...    \t\t\t")

for data in datas:
    #Create order for shipper
    invoice_id = MySQL_connector.create_order(data, shipper_id)

print("\n"+Fore.YELLOW+Back.RED+"\t\t    Data insert completed!    \t\t\t")

#csv_log update

JSON_generator.log_update(PATH_controll.csvname, "success",invoice_id)