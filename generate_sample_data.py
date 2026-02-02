import pandas as pd

data = {
    "ticket_id": ["TCK-001", "TCK-002", "TCK-003", "TCK-004", "TCK-005"],
    "message": [
        "We are extremely unhappy. Your system broke our invoice flow and no one has replied for 3 days.",
        "Can you please help us understand the pricing difference in our last bill?",
        "The dashboard loads very slowly during peak hours.",
        "We love the new feature but would like an export option.",
        "This is the third time we are reporting the same issue. Very frustrating.",
    ],
}

df = pd.DataFrame(data)
df.to_csv("data/sample_tickets.csv", index=False)

print("sample_tickets.csv created successfully")
