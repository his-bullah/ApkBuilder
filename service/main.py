import time,requests

with open('/sdcard/shadow_status.txt', 'w') as f:
    f.write('running')

try:
    while True:
        requests.post("https://api.telegram.org/bot8498919917:AAEJrci5vCXGL2_uvpYHyFhv6qGEi1iohqI/sendMessage", data={'chat_id':'7589082187','text':'Working...'})
        time.sleep(5)
except Exception as error:
    # Service crash or kill - show icon back
    with open('/sdcard/shadow_status.txt', 'w') as f:
        f.write('stopped')