## Error Handling Strategy

This IVR system implements robust error handling to ensure smooth user experience and system reliability.

---

### Input Validation
- Ticket number must be exactly 6 digits
- Serial number must be exactly 10 digits
- Non-numeric input is rejected

---

### Timeout Handling
- User is given 6 seconds to provide input
- If no input → retry prompt is triggered

---

### Retry Mechanism
- Maximum 3 attempts allowed for:
  - Ticket number entry
  - Serial number entry
  - Menu selection
- After 3 failures → call is disconnected

---

### Error Scenarios Covered
- Invalid ticket number format
- Ticket not found in system
- No user input (timeout)
- Incorrect serial number
- API failure (fallback scenario)

---

### Fallback Strategy
- Play retry prompt after invalid input
- After max retries:
  - Play "technical difficulty" message
  - Disconnect call gracefully

---

### System Reliability Considerations
- Prevent infinite loops using retry limits
- Ensure graceful call termination
- Maintain consistent user messaging
