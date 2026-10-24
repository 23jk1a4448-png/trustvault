# AI Prompt Engineering & Debugging Log (PROMPTS.md)

**Candidate Name:** Potturi Shanmuka Siva Sankar  
**Candidate Roll / Username:** 23jk1a4448  
**Challenge:** Snovasys Fresher Hiring Challenge 2026  
**Project:** TrustVault — Secure Multi-Tenant Document Management System  

---

## 1. Executive Summary
This document records the exact iterative prompts, AI diagnostic findings, architectural corrections, and debugging resolutions undertaken during the development of TrustVault.

---

## 2. Prompt Iteration Log & AI Diagnostics

### Phase 1: Architecture & Model Design
- **Prompt:** "Build a secure document vault application called TrustVault with multi-tenant isolation, role-based access control (Admin, Owner, Viewer), cryptographic status indicators, and verifiable audit logging. The UI must follow a strict cybersecurity dark emerald theme."
- **Issue Encountered:** AI generated deeply nested modules that threw `ModuleNotFoundError` when run from subdirectories in Windows.
- **My Resolution:** Consolidated the runnable application into a self-contained, robust single-file server (`run.py`) using Flask and SQLAlchemy SQLite ORM with dynamic seed records.

### Phase 2: Package Management & Windows Paths
- **Prompt:** Executed package installation in local environment.
- **Issue Encountered:** Terminal threw `npm error code ENOENT` because `npm` was executed on a Python project instead of `pip`.
- **My Resolution:** Isolated the Python runtime using `.venv` virtual environment and generated a pinned `requirements.txt` containing Flask 3.0.3, Flask-SQLAlchemy 3.1.1, and Werkzeug 3.0.3.

### Phase 3: Branding & Ownership
- **Prompt:** "Change the owner and project branding to Siva Sankar's Secure Vault."
- **Issue Encountered:** AI updated the HTML header but left backend document models defaulting to hardcoded mock owners.
- **My Resolution:** Synchronized database schema defaults and form creation handlers to bind documents to candidate Siva Sankar (`23jk1a4448`).

### Phase 4: Search & Safe Deletion
- **Prompt:** "Add live search filtering and document deletion."
- **Issue Encountered:** AI used a GET request for deletion (vulnerable to CSRF) and case-sensitive substring matching.
- **My Resolution:** Converted deletion to an authenticated POST route (`/delete/<int:doc_id>`) with user confirmation, and upgraded search queries to case-insensitive `ilike` filters via `db.or_`.

---

## 3. Honest Limitations / Future Work
- Physical Disk Encryption: Metadata and cipher statuses are tracked via SQLite; KMS envelope encryption is architected for enterprise cloud deployments.
- Automated Token Expiration: Document share links support instant manual revocation; automated cron-based token expiration is planned for the next release.
