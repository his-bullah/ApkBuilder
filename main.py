from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass
from android import mActivity


class MyApp(App):

    def start_service(self, instance):

        PythonService = autoclass('org.kivy.android.PythonService')

        service = PythonService.mService
        if service is None:
            PythonService.start(mActivity, "Foreground Service Running")

        print("Service started")

    def build(self):
        btn = Button(text="Start Foreground Service")
        btn.bind(on_press=self.start_service)
        return btn


MyApp().run()