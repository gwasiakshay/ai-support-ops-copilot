def build_ticket_prompt(ticket_text: str) -> str:
    return f"""
Analyze the following customer support ticket and return ONLY valid JSON.

Ticket:
\"\"\"{ticket_text}\"\"\"

Return JSON with these fields:
- intent (billing | technical issue | feature request | complaint | general query)
- urgency (low | medium | high | critical)
- sentiment (positive | neutral | negative)
- escalation_required (true or false)
- churn_risk (low | medium | high)
- suggested_response (3-6 sentences)

Rules:
- Be concise
- Be business-focused
- Do not add explanations
- Output must be valid JSON
"""
