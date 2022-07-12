# WIN10TOAST
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast(title="Naab0",
                   msg="This notification is in it's own thread!",
                   icon_path="C:\\NAABO\\Codes\\z.Official_test\\microsoft_store.ico",
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active():
    time.sleep(0.1)


# WINOTIFY
from winotify import Notification, audio

toast = Notification(
    app_id="Naabo",
    title="New",
    msg="This notification is in it's own thread!",
    duration="short",
    icon="C:\\NAABO\\Codes\\z.Official_test\\microsoft_store.ico"
)

toast.set_audio(audio.Default, loop=False)
toast.add_actions(
    label="Click Me",
    launch="https://todo.naabo.repl.co/"
)
toast.show()
