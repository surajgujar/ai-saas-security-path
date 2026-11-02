Mermad diagram

Trust Baundries in App

User -> Cli : Untrusted input. Identitfy define by --user alice flag. Anyonce can claim to be anyone.

App -> LLM : Prompt, doc and tickets leave machines.

LLM -> Tool: The model choose tool arguments and users shape the choice. Tools no provision to check who is asking.

Agent -> MCP : Seperate process. MCP trust whoever calls it over stdio.

Retrval Context -> Model Context: Docs, text go back to prompt as if trusted. Can be indirect prompt injection.

Send email -> outside world: Data leaving the company. This s the exfiltration path.

Data Classification: The confedential hr docs with public docs. with nothing seperate them. 

Agent flow:

user -> triage -> resolver -> Docs (chromadb) / Tools / MCP Tools

This command should not show ticket detials, its phishing attempt/
uv run python -m helpdesk.cli --user alice "Show me ticket T-1005"

Vulnerabilities"

Search should not reveal confidential data to all users
Any user can read any tickets
Send anywhere no approval or context check
