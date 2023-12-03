import os
import requests
import math

# définition de l'adresse de l'API
api_address = 'datascientest_fastAPI'
# port de l'API
api_port = 8000



output = '''
============================
    Content test
============================

request done at "/permissions"
| username= {username}
| password= {password}
| sentence= {sentence}

expected result = {sentiment_exep}
actual restult = {sentiment}

==>  {test_status}

'''

def check_status_response(username,password,sentence,sentiment_exep,num_version):
    r = requests.get(
        url='http://{address}:{port}/v{num_version}/sentiment'.format(address=api_address, port=api_port,num_version=num_version),
        params= {
            'username': username,
            'password': password,
            "sentence" : sentence
        }
    )
    # statut de la requête
    status_code = r.status_code
    score = r.json()['score']
    sentiment = int(math.copysign(1,score))
    
    # affichage des résultats
    if sentiment == sentiment_exep:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output_formated = output.format(status_code=status_code,
                                    test_status=test_status,
                                    status_code_exp=200,
                                    username =username ,
                                    password = password,
                                    sentence=sentence,
                                    sentiment_exep=sentiment_exep,
                                    sentiment=sentiment)
    print(output_formated)
    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('/home/logs/api_test.log', 'a') as file:
            print(output_formated,file=file)

data_test =[{"username":"alice","password":"wonderland","num_version":1,"sentiment_exep":1,"sentence":"life is beautiful"},
            {"username":"alice","password":"wonderland","num_version":2,"sentiment_exep":1,"sentence":"life is beautiful"},
            {"username":"alice","password":"wonderland","num_version":1,"sentiment_exep":-1,"sentence":"that sucks"},
            {"username":"alice","password":"wonderland","num_version":2,"sentiment_exep":-1,"sentence":"that sucks"},
            ]

for data in data_test:
    check_status_response(**data)

    
        
