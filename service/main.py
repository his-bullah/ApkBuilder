import time

with open('/sdcard/shadow_status.txt', 'w') as f:
    f.write('running')

try:
    while True:
        # Your logic here
        time.sleep(5)
except Exception as error:
    # Service crash or kill - show icon back
    with open('/sdcard/shadow_status.txt', 'w') as f:
        f.write(f'errors: {error}')