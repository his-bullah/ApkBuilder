from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text='Service Status: Stopped')
        
        start_btn = Button(text='Start Service')
        stop_btn = Button(text='Stop Service')
        
        start_btn.bind(on_press=self.start_service)
        stop_btn.bind(on_press=self.stop_service)
        
        layout.add_widget(self.label)
        layout.add_widget(start_btn)
        layout.add_widget(stop_btn)
        
        return layout
    
    def start_service(self, *args):
        from android import AndroidService
        self.service = AndroidService('My Service', 'Running in background')
        self.service.start('hello')
        self.label.text = 'Service Status: Running'
    
    def stop_service(self, *args):
        self.service.stop()
        self.label.text = 'Service Status: Stopped'

if __name__ == '__main__':
    MainApp().run()