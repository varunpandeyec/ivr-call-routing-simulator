## Ticket Lookup Flow

- Collect 6 digit ticket number
- Validate input (must be exactly 6 digits)
- Timeout: 6 seconds
- Retry: 3 attempts

Error Handling:
- Invalid input → Retry prompt
- After 3 failures → Disconnect

API Integration:
- Call external API to fetch:
  - Ticket ID
  - Description
  - Serial Number
  - Ticket Type

Routing:
- Finance → Finance Queue
- Admin → Admin Queue
- Sales → Sales Queue