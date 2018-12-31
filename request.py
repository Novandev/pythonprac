import requests

r = requests.get('https://api.myjson.com/bins/m6wsyFASDFAFDADFADEFADAS')


response_dict = r.json()


def return_response():
    if not r.json()['name']:
        print('API ERROR')
    else:
         print(r.json())
    # for key, value in response_dict.items():
    #     print('key is : {} value is: {} \n'.format(key,value))

if __name__ == "__main__":
    return_response()