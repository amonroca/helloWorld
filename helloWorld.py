from datetime import datetime

# Hello World sample code in Python
def presentation():
    now = datetime.now()
    hour = now.hour
    greeting = "Good morning!" if hour < 12 else "Good afternoon!" if hour < 18 else "Good evening!"
    
    print(greeting)

    print(f"Current date and time: {now.strftime('%m/%d/%Y at %I:%M %p')}")

def main():
    print(r"""
  _   _      _ _        __        __         _     _ 
 | | | | ___| | | ___   \ \      / /__  _ __| | __| |
 | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` |
 |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |
 |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_|
    """)
    presentation()

if __name__ == "__main__":
    main()