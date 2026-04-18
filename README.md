IVR Call Routing Simulator

Overview

This project simulates a real-world IVR (Interactive Voice Response) system inspired by enterprise platforms like Genesys Cloud Architect.

It demonstrates intelligent call routing, API integration, retry handling, and customer experience optimization.

⸻

Features

1. ANI Blacklist Check

* Incoming caller number (ANI) is validated against a data table
* If number is blacklisted → Call is disconnected immediately

⸻

2. Welcome & Compliance Prompts

* Premium welcome prompt
* Call recording disclaimer

⸻

3. Ticket Lookup Flow

* User enters 6-digit ticket number
* Input validation (exactly 6 digits)
* Timeout handling (6 seconds)
* Retry logic (3 attempts)

API Integration

* Fetch ticket metadata:
    * Ticket ID
    * Description
    * Serial Number
    * Ticket Type

Routing Logic

* Finance → Finance Queue
* Administration → Admin Queue
* Sales → Sales Queue

⸻

4. Ticket Creation Flow

* User presses 1 to create ticket
* Collect 10-digit serial number
* Retry logic (3 attempts)

Ticket Type Selection

* Press 1 → Admin
* Press 2 → Tech Support

API Integration

* Create ticket using backend API (Salesforce simulation)
* Retrieve ticket metadata

Routing

* Dynamic routing based on ticket type

⸻

Tech Stack

* IVR Design (Genesys Cloud concepts)
* REST APIs
* Data Tables
* Call Routing Logic
* Error Handling & Retry Mechanism

⸻

Project Structure

ivr-call-routing-simulator/
│
├── call-flows/
├── api/
├── data/


Key Highlights

* Simulates enterprise-grade IVR system
* Implements retry + timeout handling
* Demonstrates backend API integration
* Designed for scalability and reliability

⸻

Future Enhancements

* NLU integration (Dialogflow)
* Multi-language support
* Real-time analytics dashboard
