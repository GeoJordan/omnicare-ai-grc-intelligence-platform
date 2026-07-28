import os
import json
import logging
import sqlite3
from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("CyberGRC")

load_dotenv()

# Initialize Gemini Client
try:
    client = genai.Client()
except Exception as e:
    logger.error(f"Failed to initialize Gemini Client: {e}")
    client = None

app = FastAPI(
    title="CyberGRC Coprocessor API",
    description="Database-backed GRC API infrastructure caching multi-framework compliance blueprints.",
    version="1.1.0"
)

DB_FILE = "risks.db"

# --- Database Initialization ---

def init_db():
    """Initializes the local SQLite database and establishes the risk ledger schema."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS risk_ledger (
            risk_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            matrix_key TEXT NOT NULL,
            framework_mappings TEXT NOT NULL,
            technical_remediation TEXT NOT NULL,
            audit_evidence TEXT NOT NULL,
            operational_procedure TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Local SQLite database initialized and verified.")

# Run database setup on server spin-up
init_db()

# --- Data Schemas ---

class RiskIntakePayload(BaseModel):
    risk_id: str = Field(..., examples=["RSK-2026-001"])
    title: str = Field(..., examples=["Unencrypted S3 Buckets"])
    description: str = Field(..., examples=["Production storage lacks encryption at rest."])
    matrix_key: str = Field(..., examples=["UNENCRYPTED_S3_BUCKET"])

class ComplianceBlueprint(BaseModel):
    technical_remediation: str = Field(description="Precise technical steps to mitigate the risk in cloud environments.")
    audit_evidence: str = Field(description="Exact evidence logs, artifacts, or configurations requested by auditors.")
    operational_procedure: str = Field(description="Ongoing operational review cadence or governance workflows required.")

# --- Core Logic Workhorse with Database Cache ---

def execute_compliance_mapping(risk_data: dict) -> dict:
    risk_id = risk_data.get("risk_id")
    lookup_key = risk_data.get("matrix_key")

    # 1. Check Local SQLite Database Cache First
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, framework_mappings, technical_remediation, audit_evidence, operational_procedure 
        FROM risk_ledger WHERE risk_id = ?
    """, (risk_id,))
    cached_record = cursor.fetchone()

    if cached_record:
        logger.info(f"🎯 Cache Hit! Pulling historical data for {risk_id} directly from local SQLite storage.")
        conn.close()
        return {
            "risk_id": risk_id,
            "title": cached_record[0],
            "framework_mappings": json.loads(cached_record[1]),
            "compliance_remediation_blueprint": {
                "technical_remediation": cached_record[2],
                "audit_evidence": cached_record[3],
                "operational_procedure": cached_record[4]
            },
            "source": "Local SQLite Database"
        }

    # 2. Cache Miss - Fallback to Local Configuration Matrix
    matrix_path = "mapping_matrix.json"
    if not os.path.exists(matrix_path):
        conn.close()
        return {"error": "Internal configuration error: Mapping database unavailable."}

    with open(matrix_path, "r") as f:
        mapping_matrix = json.load(f)

    framework_citations = mapping_matrix.get(lookup_key)
    if not framework_citations:
        conn.close()
        return {"error": f"Target framework key '{lookup_key}' is invalid or unregistered."}

    if not client:
        conn.close()
        return {"error": "AI Coprocessor offline. Backend API client initialization failed."}

    logger.info(f"🔄 Cache Miss. Invoking Gemini Engine to map controls for {risk_id} via key: {lookup_key}")

    system_instruction = (
        "You are an expert CyberGRC Co-Processor specialized in healthcare compliance audits. "
        "Your responses must be strictly technical, practical, and tailored directly to cloud infrastructure teams."
    )
    
    user_prompt = f"""
    Analyze the following security finding and generate an engineering mitigation and audit evidence blueprint.

    RISK DETAIL:
    - ID: {risk_id}
    - Title: {risk_data.get('title')}
    - Vulnerability/Threat Context: {risk_data.get('description')}

    DETERMINISTIC REGULATORY MAPPINGS:
    - HIPAA Security Rule: {framework_citations.get('hipaa')}
    - NIST SP 800-53 Rev 5: {framework_citations.get('nist_800_53')}
    - SOC 2 TSC: {framework_citations.get('soc2')}
    - HITRUST CSF v11: {framework_citations.get('hitrust')}
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.15,
                response_mime_type="application/json",
                response_schema=ComplianceBlueprint,
            )
        )
        structured_output = json.loads(response.text)
    except Exception as api_err:
        logger.error(f"Gemini API generation failure: {api_err}")
        conn.close()
        return {"error": "Upstream intelligence processing error. Please try again."}

    # 3. Save the Newly Generated Blueprint to the SQLite Database
    try:
        cursor.execute("""
            INSERT INTO risk_ledger 
            (risk_id, title, description, matrix_key, framework_mappings, technical_remediation, audit_evidence, operational_procedure)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            risk_id,
            risk_data.get("title"),
            risk_data.get("description"),
            lookup_key,
            json.dumps(framework_citations),
            structured_output.get("technical_remediation"),
            structured_output.get("audit_evidence"),
            structured_output.get("operational_procedure")
        ))
        conn.commit()
        logger.info(f"💾 Successful data persistence: Saved {risk_id} to risk_ledger table.")
    except Exception as db_err:
        logger.error(f"Failed to persist record to database: {db_err}")
    finally:
        conn.close()

    return {
        "risk_id": risk_id,
        "title": risk_data.get("title"),
        "framework_mappings": framework_citations,
        "compliance_remediation_blueprint": structured_output,
        "source": "Gemini AI Engine Generation"
    }

# --- API Endpoints ---

@app.post("/analyze-risk", response_model=dict)
async def analyze_risk_endpoint(payload: RiskIntakePayload):
    result = execute_compliance_mapping(payload.model_dump())
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.get("/historical-risks", response_model=list)
async def get_historical_risks():
    """Queries the local SQLite database to return all saved historical tracking items."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT risk_id, title, matrix_key, created_at FROM risk_ledger ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    history_list = [
        {"risk_id": row[0], "title": row[1], "matrix_key": row[2], "created_at": row[3]}
        for row in rows
    ]
    return history_list


@app.delete("/clear-database")
async def clear_database_endpoint():
    """Admin utility endpoint to purge all rows from the local risk tracking table."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM risk_ledger")
        conn.commit()
        conn.close()
        logger.info("Admin Action executed: Purged risk_ledger data rows.")
        return {"status": "success", "message": "All historical records have been successfully purged from the database ledger."}
    except Exception as e:
        logger.error(f"Database clear failure: {e}")
        raise HTTPException(status_code=500, detail="Internal SQL database purge operation failed.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ai_coprocessor:app", host="127.0.0.1", port=8000, reload=True)