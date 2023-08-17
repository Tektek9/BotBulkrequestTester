import pandas as pd
import requests

print('''\n=BULK===================
==   REQUEST TESTER   ==
=======by=kulionline11==\n''')

a = 0
data = pd.read_csv('Audit_dnscluster.csv')
diulang = data.shape[0]
for i in range(diulang):
    print("Bulk Audit DNS Cluster ke ",i+1)
    alamat = data.iloc[i]['target']
    if pd.notnull(alamat):
        url_list = alamat.split(',')
        for url in url_list:
            url = url.strip()
            url2 = "http://" + url + ":2087/"
            url3 = "https://" + url + ":2087/"
            url4 = "http://" + url + "/whm"
            url5 = "https://" + url + "/whm"
            subdomain = url.split('.')[0].upper()
            
            try:
                sc = requests.get(url2)
                if sc.status_code == 200 :
                    url6 = url2
                    print(f"\n{subdomain}")
                    print("Koneksi OK\n")
                else:
                    cek2 = url3
                    sc = requests.get(cek2)
                    if sc.status_code == 200 :
                        url6 = url3
                        print(f"\n{subdomain}")
                        print("Koneksi OK\n")
                    else:
                        cek3 = url4
                        sc = requests.get(cek3)
                        if sc.status_code == 200 :
                            url6 = url4
                            print(f"\n{subdomain}")
                            print("Koneksi OK\n")
                        else:
                            cek4 = url5
                            sc = requests.get(cek4)
                            if sc.status_code == 200 :
                                url6 = url5
                                print(f"\n{subdomain}")
                                print("Koneksi OK\n")
            except requests.exceptions.ConnectionError:
                print(f"\n{subdomain}")
                print("SERVER NONAKTIF\n")
    continue