# Coframe Applied Science — Take-Home

## Background

Coframe runs experimentation using agents. Before a client signs, the sales team needs to answer a simple question: *what can they expect from an experimentation program — in dollars, in time, in number of tests?*

Right now that answer lives in someone's head, and is sometimes not grounded in real traffic limitations. The goal is to make it a tool for sales.

---

## Your task

Build an **Experimentation ROI Calculator** — a tool that takes inputs about a client's website and produces a 12-month outlook for what a structured experimentation program could achieve.

Numbers alone are not enough. The output must be human-readable and non-technical-user friendly — a sales rep should be able to walk a client through it without needing to explain statistics. Something like: *"With your traffic, each test takes about 18 days to reach significance. Running tests continuously at a 20% win rate, you could expect 3–4 winners in your first quarter."*

**Deterministic or non-deterministic — your call.** The math core (power analysis, expected lift, revenue model) must be grounded in statistics. You are welcome to wrap that in an LLM to generate the human-friendly narrative, or keep it purely algorithmic with a nice dashboard. Either way, the numbers must be realistic.

See [examples.md](examples.md) for sample client inputs you can use to develop and demo your tool.

---

## Inputs

| Input | Description | Example |
|---|---|---|
| Page name | Label for the page | `"Pricing"` |
| Daily active users | Traffic to that page per day | `1 200` |
| Baseline conversion rate | Current rate for the target metric | `2.1%` |
| Revenue per conversion | Average value of one conversion | `$89` |
| Target lift (total) | Overall conversion improvement goal across the full program | `10%` |
| Average lift per winning experiment | Expected conversion improvement from a single winning test | `3%` |
| Win rate | % of experiment ideas that beat the baseline by the average lift | `20%` |
| Statistical significance threshold | Confidence level to call a winner | `95%` |

Multiple pages can be added. Each is modelled independently.

---

## Outputs

The output format and structure are up to you. At minimum, an Account Executive should be able to run it with a client's numbers and walk away with a clear, credible story about what an experimentation program would deliver. Make your assumptions explicit — that's part of the work.

---

## Deliverables

Email back a **recorded video** and your **code**.

The video should cover:

1. **Demo** — run the tool with at least one of the example clients; show how the output changes when assumptions shift
2. **Solution** — what you built, how, and why; include every AI tool and test harness you used during the build
3. **Edge cases** — what you handled, what you consciously left out, and why
4. **Productionization** — how would this evolve from a sales tool to a PoC to an actual planning tool?

The code can be sent as a repo link, gist, or zip.