import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="CyberGRC Coprocessor", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")
BACKEND_URL = "http://127.0.0.1:8000"

# --- Sidebar Controls Panel ---
st.sidebar.title("🧭 Navigation Control")
app_mode = st.sidebar.radio("Select Workspace Panel:", ["🔬 Coprocessor Analysis Console", "📜 Historical Risk Ledger"])
st.sidebar.markdown("---")
st.sidebar.subheader("🛠️ Admin Master Utilities")

# The Live Purge Button Action
if st.sidebar.button("🚨 Purge Local SQL Database", use_container_width=True, type="secondary"):
    try:
        purge_res = requests.delete(f"{BACKEND_URL}/clear-database")
        if purge_res.status_code == 200:
            st.sidebar.success("Database wiped successfully!")
            st.toast("Database cleared!", icon="🗑️")
        else:
            st.sidebar.error("Failed to clear database.")
    except Exception as err:
        st.sidebar.error(f"Error calling clear endpoint: {err}")

st.sidebar.markdown("---")
st.sidebar.caption("🤖 **Engine Version:** v1.2.0")

# =========================================================
# PANEL 1: ANALYTICS RUNNER
# =========================================================
if app_mode == "🔬 Coprocessor Analysis Console":
    st.title("🛡️ CyberGRC Coprocessor Intelligence Workbench")
    st.markdown("Automate technical remediation blueprints and evidence parameters natively across multiple healthcare standards.")
    st.write("---")

    input_panel, display_panel = st.columns([1, 2], gap="large")

    with input_panel:
        st.subheader("📋 Risk Metric Intake Form")
        risk_id = st.text_input("Risk Tracking ID", value="RSK-2026-004")
        risk_title = st.text_input("Vulnerability Title", value="Missing MFA for Domain Administration")
        risk_description = st.text_area("Risk Context / Impact Statement", value="Privileged domain accounts allow single-factor login.")
        
        # Pull newly expanded matrix values
        target_matrix_key = st.selectbox(
            "Control Framework Pivot Key",
            options=["OVER_PRIVILEGED_IAM", "UNENCRYPTED_S3_BUCKET", "MISSING_MFA_DOMAIN_ADMIN", "UNLOGGED_DATABASE_QUERIES", "EXPOSED_SSH_PORTS"]
        )
        execute_analysis = st.button("Generate Compliance Blueprint", type="primary", use_container_width=True)

    with display_panel:
        st.subheader("⚡ Structured Compliance Engineering Output")
        if execute_analysis:
            request_payload = {"risk_id": risk_id, "title": risk_title, "description": risk_description, "matrix_key": target_matrix_key}
            with st.spinner("Processing framework data..."):
                try:
                    api_response = requests.post(f"{BACKEND_URL}/analyze-risk", json=request_payload, timeout=30)
                    if api_response.status_code == 200:
                        processed_data = api_response.json()
                        blueprint = processed_data.get("compliance_remediation_blueprint", {})
                        citations = processed_data.get("framework_mappings", {})
                        data_source = processed_data.get("source", "Unknown")
                        
                        if "Cache Hit" in data_source:
                            st.success(f"🎯 Loaded from Local Storage ({data_source})")
                        else:
                            st.success(f"🎉 Generated Fresh ({data_source})")
                        
                        st.markdown("### 🗺️ Mapped Control Infrastructure Citations")
                        st.json(citations)
                        st.write("---")
                        
                        tab1, tab2, tab3 = st.tabs(["🛡️ Technical Remediation", "📊 Audit Evidence", "🏥 Operational Governance"])
                        with tab1: st.info(blueprint.get("technical_remediation"))
                        with tab2: st.warning(blueprint.get("audit_evidence"))
                        with tab3: st.success(blueprint.get("operational_procedure"))
                    else:
                        st.error("Backend validation error.")
                except Exception:
                    st.error("Connection error.")
        else:
            st.info("Awaiting execution parameters.")

# =========================================================
# PANEL 2: READ MATRIX HISTORY
# =========================================================
elif app_mode == "📜 Historical Risk Ledger":
    st.title("📜 SQLite Audit Tracking Ledger")
    st.markdown("Direct historical readout of persistent compliance blueprints saved inside the local database archives.")
    st.write("---")
    try:
        history_response = requests.get(f"{BACKEND_URL}/historical-risks", timeout=10)
        if history_response.status_code == 200:
            history_data = history_response.json()
            if not history_data:
                st.info("The local database cache is currently empty.")
            else:
                st.subheader(f"📑 Registered Audit Entries ({len(history_data)})")
                df_ledger = pd.DataFrame(history_data)
                df_ledger.columns = ["Risk Tracking ID", "Vulnerability Finding Title", "Matrix Pivot Key", "Audit Generation Timestamp"]
                st.dataframe(df_ledger, use_container_width=True, hide_index=True)
    except Exception:
        st.error("Connection error loading history.")