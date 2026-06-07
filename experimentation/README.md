# Coframe Applied Science — Take-Home

## Background

Coframe runs experimentation using agents. Before a client signs, the sales team needs to answer a simple question — grounded in the client's *real* traffic: *what can they expect from an experimentation program over the next 12 months — in tests, in winners, in conversion lift, and in dollars?*

Right now that answer lives in someone's head and isn't tied to traffic limits. The goal is to make it a tool for sales.

---

## Your task

Build an **Experimentation ROI & Roadmap Planner** — a tool that takes a client's website inputs and produces a credible **12-month outlook** for what a structured experimentation program could achieve.

Two things make the outlook credible: the numbers are **grounded in statistics** and in the client's **real traffic limits**, and the result is a **clear, plain-English story** a sales rep can walk a client through without explaining statistics.

**Deterministic or LLM-wrapped — your call.** You can wrap the math in an LLM for the narrative or keep it a purely deterministic dashboard. Either way the numbers must be realistic, and every assumption must be visible and editable.

See [clients/](clients/) for sample client inputs you can use to develop and demo your tool.

---

## Inputs

Inputs come in two groups: **program-level** (set once) and **per-page**. Program-level inputs have sensible defaults; the per-page inputs describe the client's actual pages and are required.

### Program-level (set once)


| Input             | JSON key                 | Description                                                                                                                                                              | Default |
| ----------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| Horizon           | `horizon_days`           | How far ahead to plan — the length of the outlook, in days                                                                                                               | `365`   |
| Reporting cadence | `reporting_cadence_days` | How often the client expects a results report (typically `7`, `14`, or `30`). A test isn't required to fit inside one window — it's just when the client wants an update | `30`    |
| Win rate          | `win_rate`               | Share of completed tests that produce a deployable winner (Coframe's track-record assumption)                                                                            | `0.15`  |
| Confidence target | `confidence_target`      | Confidence needed to call a winner                                                                                                                                       | `0.95`  |


### Per-page (each page modelled independently)


| Input                    | JSON key                 | Description                                                                                                                                            | Example     |
| ------------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| Page name                | `name`                   | Label for the page                                                                                                                                     | `"Pricing"` |
| Daily visitors           | `daily_visitors`         | Total daily visitors to the page                                                                                                                       | `1200`      |
| Baseline conversion rate | `baseline_rate`          | Current conversion rate on the page                                                                                                                    | `0.021`     |
| Revenue per conversion   | `revenue_per_conversion` | Value of one conversion; `0` ⇒ a non-monetized page (no direct dollar value)                                                                           | `89`        |
| Minimum detectable lift  | `min_detectable_lift`    | The relative improvement to detect on this page — also the size a winning change is assumed to deliver. Smaller lifts need much more traffic to detect | `0.05`      |


---

## Outputs

The format and structure are up to you. At minimum, an Account Executive should be able to run it with a client's numbers, walk away with a clear and credible story, and see how that story changes when the assumptions change.

---

## Deliverables

Email back a **recorded video** and your **code**.

The video should cover:

1. **Demo** — run the tool with at least one of the example clients; show how the output changes when assumptions shift.
2. **Solution** — what you built, how, and why; include every AI tool and test harness you used during the build.
3. **Edge cases** — what you handled, what you consciously left out, and why.
4. **Productionization** — how would this evolve from a sales tool to a PoC to an actual planning tool?

A **public GitHub repository is preferred** for the code. A gist or zip is acceptable if that isn't possible.