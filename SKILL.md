---
name: genpark-personal-agent-cold-pressor-pain-endurance-skill
version: "1.0.0"
description: "Zero-dependency Cold Pressor Test (CPT) pain threshold and tolerance modeler, central autonomic pain gating quantifier, and sympathetic withdrawal recovery evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Cold Pressor Pain Endurance Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to evaluate somatic pain tolerance, descending inhibitory central pain gating, and parasympathetic recovery velocity during and after acute thermal distress.

## Agent In-Context Capabilities

- **Clinical CPT Protocol**: Evaluates noxious cold immersion ($0.5^\circ\text{C} - 10.0^\circ\text{C}$), separating first awareness threshold from voluntary withdrawal tolerance.
- **Pain Sensitivity Index (PSI)**: Quantifies resilience by normalizing subjective VAS against the physical endurance latency window.
- **Vagal Reactivation Kinetics**: Tracks 1-minute and 2-minute post-test heart rate deceleration to assess autonomic nervous system recovery efficiency.

## Tools Summary

1. `evaluate_cpt_pain_tolerance`: Computes PSI, tolerance ratio, and central descending gating tier.
2. `model_autonomic_recovery_kinetics`: Analyzes 1-min and 2-min heart rate drops for vagal rebound competence.
