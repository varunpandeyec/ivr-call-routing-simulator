## Ticket Creation Flow

- User presses 1 to create ticket
- Collect 10 digit serial number
- Validate input (must be exactly 10 digits)
- Timeout: 6 seconds
- Retry: 3 attempts

Error Handling:
- Invalid input → Retry prompt
- After 3 failures → Disconnect

Ticket Type Selection:
- Press 1 → Admin
- Press 2 → Tech Support
- Retry: 3 attempts

API Integration:
- Send serial number + ticket type to backend (Salesforce)
- Create ticket and retrieve metadata

Routing:
- Finance → Finance Queue
- Admin → Admin Queue
- Sales → Sales Queue