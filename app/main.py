import time

BLACKLIST = {"+919999999999", "+918888888888"}

def is_blacklisted(ani):
    return ani in BLACKLIST

def get_ticket(ticket_id):
    return {
        "123456": {"type": "Finance", "description": "Payment issue"},
        "654321": {"type": "Admin", "description": "Account setup"},
    }.get(ticket_id)

def route(ticket_type):
    mapping = {
        "Finance": "Finance Queue",
        "Admin": "Admin Queue",
        "Sales": "Sales Queue",
        "Tech": "Tech Support Queue"
    }
    return mapping.get(ticket_type, "General Queue")

def collect_input(prompt, length, attempts=3, timeout=6):
    for _ in range(attempts):
        print(prompt)
        start = time.time()
        user = input("> ")
        if time.time() - start > timeout:
            print("Timeout. Try again.")
            continue
        if len(user) == length and user.isdigit():
            return user
        print("Invalid input. Try again.")
    return None

def main():
    ani = input("Enter ANI (caller number): ")

    if is_blacklisted(ani):
        print("Call disconnected (blacklisted).")
        return

    print("Welcome to Varun.com")
    print("Calls may be recorded for quality and training.")

    choice = input("Enter ticket (6 digits) or press 1 to create: ")

    if choice == "1":
        serial = collect_input("Enter 10-digit serial:", 10)
        if not serial:
            print("Failed. Disconnecting.")
            return
        ttype = input("Press 1 Admin, 2 Tech: ")
        ttype = "Admin" if ttype == "1" else "Tech"
        print(f"Ticket created. Routing to {route(ttype)}")

    else:
        ticket = collect_input("Enter 6-digit ticket:", 6)
        if not ticket:
            print("Failed. Disconnecting.")
            return
        data = get_ticket(ticket)
        if not data:
            print("Ticket not found.")
            return
        print(f"Routing to {route(data['type'])}")

if __name__ == "__main__":
    main()
