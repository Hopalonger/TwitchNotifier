from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Twitch Notification",
                   "Check the chat something has happened",
                   duration=3)
