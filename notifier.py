
import pywhatkit
import datetime

def send_whatsapp_message(phone_number, message):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2

    # ✅ Fix overflow (e.g., 59 + 2 = 61 ❌)
    if minute >= 60:
        minute -= 60
        hour += 1
        if hour >= 24:
            hour = 0  # wrap around if over 23:59

    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time=10, tab_close=True)
        print(f"\n✅ WhatsApp message scheduled to {phone_number}.")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")