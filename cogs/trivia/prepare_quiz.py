import requests
import base64

def get_new_token():
        req = requests.get("https://opentdb.com/api_token.php?command=request")
        data = req.json()
        token = data['token']
        return token

def get_questions(token):
    request = requests.get("https://opentdb.com/api.php?&encode=base64&amount=10&token={}".format(token))
    response_data = request.json()
    return response_data
   

def new_game(token):

    question_bank = get_questions(token)

    if question_bank['response_code'] in [3, 4]:

        print("Requesting new token")
        token = get_new_token()
        question_bank = get_questions(token)


    for cat in question_bank['results']:
        print(str(base64.b64decode(cat['question']), "utf-8"))
    #print(question_bank['results'])