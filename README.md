# AI Business Automation · Ticket triage baseline

A deterministic, explainable baseline for classifying fictional customer-support tickets. It demonstrates a safe preprocessing stage that could precede an AI-assisted workflow. No actual model or customer data is used.

## Run
```sh
python triage.py sample.csv
python -m unittest discover -v
```
Output is JSON with ticket IDs, proposed queues and explicit review flags. No tickets are sent or modified.

## Design
Input CSV → validate schema → classify using transparent keyword rules → structured review queue. Conflicting or unmatched categories require review. No external calls, credentials or integrations.

Português: exemplo de triagem de chamados fictícios com regras transparentes e revisão humana. Implementação assistida por IA, com decisões verificáveis.
