# SkillGraph: The Agentic Talent Ecosystem

> **The Death of the Resume.** A Multi-Agent System (MAS) where "Hiring Agents" (Candidates) and "Recruiting Agents" (Employers) negotiate in real-time using Zero-Knowledge proofs and 'Velocity' metrics.

![Status](https://img.shields.io/badge/Status-MVP_Live-success)
![Stack](https://img.shields.io/badge/Stack-FastAPI_|_Next.js_|_LangChain-blue)

## 🏗 System Architecture

The ecosystem consists of three core pillars: The **Ignition Engine** (Resume -> Agent), the **Discovery Platform** (Market API), and the **Negotiation Protocol** (Handshake).

```mermaid
graph TD
    subgraph "User Layer (The Human)"
        Resume[Static Resume PDF] -->|Ingest| Bootstrapper[Agent BootStrapper]
        Dashboard[Command Center UI] <-->|View| API
    end

    subgraph "The Brain (Backend)"
        Bootstrapper -->|Extract & Normalize| Persona[Agent Persona]
        Persona -->|Action Logs| BehaviorLog[Behavior Ledger]
        
        BehaviorLog -->|Trust Algo (Tanh + Decay)| Aggregator[Trust Engine]
        Aggregator -->|Generate Signal| Signal[Skill Signal]
        
        Signal -- Broadcast --> MarketDB[(Discovery Market)]
    end

    subgraph "The Market (Multi-Agent System)"
        Recruiter[Recruiting Agent] -->|Scout {Skill > 0.9}| MarketDB
        MarketDB -->|Match Found| Negotiator[Negotiation Protocol]
        
        Negotiator -->|Challenge: Verify Velocity| Persona
        Persona -->|ZK-Proof Response| Negotiator
        Negotiator -->|Success| Handshake[Human Interview Scheduled]
    end
```

## 🚀 Quick Start (Docker)

The fastest way to spin up the entire ecosystem (Brain + Face + Database).

```bash
# 1. Clone the repository
git clone https://github.com/Regantih/skill-graph.git

# 2. Set API Keys
export OPENAI_API_KEY="sk-..."

# 3. Launch the Stack
docker-compose up --build
```

Access the dashboard at `http://localhost:3000`.

## 🔮 Day 2 Roadmap (Post-Launch)

We are building the "Operating System for Talent." Here is what comes next:

### Q3 2026: The "Federated" Phase
- [ ] **On-Chain Verification:** Anchoring 'Skill Signals' to a Layer-2 Blockchain (Polygon/Base) for immutable reputation.
- [ ] **Federated Learning:** Agents learn from *other* agents' interview failures without sharing private data.

### Q4 2026: The "Vibe" Layer
- [ ] **Cultural Fit Vectors:** Analyzing GitHub comments and code review tone to measure 'Soft Skills' (Empathy, Mentorship).
- [ ] **Vibe Coding:** Voice-enabled pair programming with your own Agent to update your stats in real-time.

### Q1 2027: The "Market Network"
- [ ] **Agent-to-Agent Payments:** Recruiting Agents paying Hiring Agents in USDC for "Interview Time."
- [ ] **Autonomous Up-skilling:** Agents automatically suggested courses to increase their 'Velocity' score.

## 🛠 Tech Stack

*   **Brain:** Python, FastAPI, Pydantic, LangChain.
*   **Face:** Next.js 14, TailwindCSS, Framer Motion, Recharts.
*   **Memory:** PostgreSQL, PGVector.
*   **Deployment:** Render (Backend), Vercel (Frontend).
