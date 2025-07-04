
from admin_dashboard import authenticate, show_dashboard

if authenticate():
    show_dashboard()
else:
    print("Access denied.")
