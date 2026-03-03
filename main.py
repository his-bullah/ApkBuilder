from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20)
        self.label = Label(text='Starting...')
        root.add_widget(self.label)
        Clock.schedule_once(self.get_permission, 1)
        return root

    def get_permission(self, dt):
        try:
            from android.permissions import request_permissions, Permission
            from android import api_version
            permissions = [Permission.FOREGROUND_SERVICE]
            if api_version >= 33:
                permissions.append(Permission.POST_NOTIFICATIONS)
            request_permissions(permissions, self.permission_callback)
            self.label.text = 'Requesting permission...'
        except Exception as e:
            self.label.text = f'Error: {str(e)}'

    def permission_callback(self, permissions, results):
        if all(results):
            self.label.text = 'Permission granted'
            Clock.schedule_once(self.launch, 1)
        else:
            self.label.text = 'Permission denied'

    def launch(self, dt):
        try:
            from android import AndroidService
            self.service = AndroidService('Shadow', 'Shadow is running...')
            self.service.start('start')
            self.label.text = 'Service Running'
        except Exception as e:
            self.label.text = f'Error: {str(e)}'

if __name__ == '__main__':
    MainApp().run()