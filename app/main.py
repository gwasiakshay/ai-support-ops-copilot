from fastapi import FastAPI, UploadFile, File
import pandas as pd

from app.llm_client import call_llm
from app.prompts import build_ticket_prompt
from app.utils import safe_json_parse

app = FastAPI(title="AI Support Ops Copilot")


@app.post("/analyze-ticket")
def analyze_ticket(ticket: dict):
    prompt = build_ticket_prompt(ticket["message"])
    llm_output = call_llm(prompt)
    result = safe_json_parse(llm_output)

    return {"ticket_id": ticket["ticket_id"], "analysis": result}


@app.post("/analyze-batch")
def analyze_batch(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    results = []

    for _, row in df.iterrows():
        prompt = build_ticket_prompt(row["message"])
        llm_output = call_llm(prompt)
        analysis = safe_json_parse(llm_output)

        result = {"ticket_id": row["ticket_id"], **analysis}
        results.append(result)

    output_df = pd.DataFrame(results)
    output_path = "data/output_results.csv"
    output_df.to_csv(output_path, index=False)

    return {
        "message": "Batch analysis completed",
        "output_file": output_path,
        "total_tickets": len(output_df),
    }
