from datetime import datetime

def detect_login(username, success):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if success:
        print(f"[{timestamp}] SUCCESSFUL LOGIN: {username}")
    else:
        print(f"[{timestamp}] FAILED LOGIN: {username}")

if __name__ == "__main__":
    detect_login("test_user", True)
    detect_login("unknown_user", False)