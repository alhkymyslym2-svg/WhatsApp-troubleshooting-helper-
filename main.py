from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
import webbrowser

class WhatsAppCleanerApp(App):
    def build(self):
        self.title = "مساعد حل مشاكل واتساب"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        lbl = Label(
            text="مساعد حل مشاكل واتساب\n(تواصل مباشر مع الشركة)", 
            font_size='20sp', 
            halign='center',
            color=get_color_from_hex('#25D366')
        )
        
        btn_support = Button(
            text="إرسال طلب فك حظر للشركة", 
            size_hint=(1, 0.2), 
            background_color=get_color_from_hex('#075E54')
        )
        btn_support.bind(on_press=self.send_support_email)
        
        layout.add_widget(lbl)
        layout.add_widget(btn_support)
        return layout

    def send_support_email(self, instance):
        recipient = "support@whatsapp.com"
        subject = "Question about my WhatsApp account"
        body = "Hello,\nMy account has been banned by mistake. Please review it and activate it again.\nMy Phone number: "
        url = f"mailto:{recipient}?subject={subject}&body={body}"
        webbrowser.open(url)

if __name__ == '__main__':
    WhatsAppCleanerApp().run()
