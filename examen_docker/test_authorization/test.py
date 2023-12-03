import os
import requests

# définition de l'adresse de l'API
api_address = 'datascientest_fastAPI'
# port de l'API
api_port = 8000



output = '''
============================
    Authorization test
============================

request done at "/permissions"
| username= {username}
| password= {password}
| sentence= {sentence}

expected result = {status_code_exp}
actual restult = {status_code}

==>  {test_status}

'''

def check_status_response(username,password,sentence,status_code_exp,num_version):
    print(username,password,status_code_exp)
    r = requests.get(
        url='http://{address}:{port}/v{num_version}/sentiment'.format(address=api_address, port=api_port,num_version=num_version),
        params= {
            'username': username,
            'password': password,
            "sentence" : sentence
        }
    )
    print() 
    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == status_code_exp:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output_formated = output.format(status_code=status_code, test_status=test_status,status_code_exp=status_code_exp,username =username ,password = password,sentence=sentence)
    print(output_formated)
    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('/home/logs/api_test.log', 'a') as file:
            print(output_formated,file=file)

data_test =[{"username":"alice","password":"wonderland","num_version":1,"status_code_exp":200,"sentence":"It's ok"},
            {"username":"alice","password":"wonderland","num_version":2,"status_code_exp":200,"sentence":"It's ok"},
            {"username":"bob","password":"builder","num_version":1,"status_code_exp":200,"sentence":"It's ok"},
            {"username":"bob","password":"builder","num_version":2,"status_code_exp":403,"sentence":"It's ok"},
            ]

for data in data_test:
    check_status_response(**data)

    
        
