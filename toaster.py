from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Notificação", "Alerta", threaded=True, icon_path=None, duration=3)
import time 

while toaster.notification_active():
    time.sleep(0.1)