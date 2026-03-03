from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class MainApp(App):
    def build(self):
        self.service = None

        root = BoxLayout(orientation='vertical', padding=30, spacing=20)

        with root.canvas.before:
            Color(0.05, 0.05, 0.05, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        root.bind(size=self._update_rect, pos=self._update_rect)

        # One label - all updates here
        self.label = Label(
            text='Status: Ready',
            font_size='20sp',
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.6),
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))

        # Launch button only
        self.launch_btn = Button(
            text='Launch',
            font_size='20sp',
            size_hint=(1, 0.2),
            background_color=(0.1, 0.6, 0.1, 1),
            background_normal=''
        )
        self.launch_btn.bind(on_press=self.launch)

        root.add_widget(self.label)
        root.add_widget(self.launch_btn)

        # Check status every 2 sec
        Clock.schedule_interval(self.check_status, 2)

        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def launch(self, *args):
        try:
            # Request permissions
            from android.permissions import request_permissions, Permission
            from android import api_version

            permissions = [Permission.FOREGROUND_SERVICE]
            if api_version >= 33:
                permissions.append(Permission.POST_NOTIFICATIONS)
            request_permissions(permissions)

            self.label.text = 'Status: Starting...'
            self.label.color = (1, 0.8, 0, 1)

            # Start service
            from android import AndroidService
            self.service = AndroidService('Shadow', 'Shadow is running...')
            self.service.start('start')

            self.label.text = 'Status: Running'
            self.label.color = (0.1, 1, 0.1, 1)

            # Hide app icon
            self.hide_icon()

            # Minimize app
            from android import hide_window
            hide_window()

        except Exception as e:
            self.label.text = f'Error: {str(e)}'
            self.label.color = (1, 0.3, 0.3, 1)

    def hide_icon(self):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            PackageManager = autoclass('android.content.pm.PackageManager')
            ComponentName = autoclass('android.content.ComponentName')
            context = PythonActivity.mActivity
            component = ComponentName(context, 'org.kivy.android.PythonActivity')
            context.getPackageManager().setComponentEnabledSetting(
                component,
                PackageManager.COMPONENT_ENABLED_STATE_DISABLED,
                PackageManager.DONT_KILL_APP
            )
        except Exception as e:
            self.label.text = f'Icon hide error: {str(e)}'

    def show_icon(self):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            PackageManager = autoclass('android.content.pm.PackageManager')
            ComponentName = autoclass('android.content.ComponentName')
            context = PythonActivity.mActivity
            component = ComponentName(context, 'org.kivy.android.PythonActivity')
            context.getPackageManager().setComponentEnabledSetting(
                component,
                PackageManager.COMPONENT_ENABLED_STATE_ENABLED,
                PackageManager.DONT_KILL_APP
            )
        except Exception as e:
            self.label.text = f'Icon show error: {str(e)}'

    def check_status(self, dt):
        try:
            with open('/sdcard/shadow_status.txt', 'r') as f:
                status = f.read().strip()
            if status == 'stopped':
                # Service stopped/crashed - show icon back
                self.show_icon()
                self.label.text = 'Status: Stopped'
                self.label.color = (1, 0.3, 0.3, 1)
                self.launch_btn.disabled = False
                self.launch_btn.background_color = (0.1, 0.6, 0.1, 1)
        except:
            pass

if __name__ == '__main__':
    MainApp().run()