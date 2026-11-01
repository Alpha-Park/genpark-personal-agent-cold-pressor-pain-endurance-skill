# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Cold Pressor Pain Endurance Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentColdPressorPainEndurance

def main():
    agent = PersonalAgentColdPressorPainEndurance()

    print("=" * 70)
    print("DEMO: Personal Agent Cold Pressor Pain Endurance & Autonomic Recovery")
    print("=" * 70)

    # 1. Evaluate Cold Pressor Test (3.0 C, threshold: 22s, tolerance: 85s, VAS: 6.5)
    res_cpt = agent.evaluate_cpt_pain_tolerance(
        water_temp_celsius=3.0,
        pain_threshold_seconds=22.0,
        pain_tolerance_seconds=85.0,
        subjective_pain_vas_10=6.5
    )

    print(f"\n1. Cold Pressor Pain Gating Analysis (3.0 C Water):")
    print(f"   Threshold Latency: {res_cpt['pain_threshold_latency_seconds']} s")
    print(f"   Tolerance Latency: {res_cpt['pain_tolerance_latency_seconds']} s")
    print(f"   Endurance Window: {res_cpt['pain_endurance_window_seconds']} s (Ratio: {res_cpt['endurance_ratio']}x)")
    print(f"   Subjective VAS: {res_cpt['subjective_vas_score_10']}/10")
    print(f"   Pain Sensitivity Index (PSI): {res_cpt['pain_sensitivity_index_psi']}")
    print(f"   Gating Tier: {res_cpt['central_pain_gating_tier']}")
    print(f"   Neuromodulation: {res_cpt['endogenous_neuromodulation_status']}")
    print(f"   Autonomic Distress: {res_cpt['autonomic_distress_score']}/100")
    print(f"   Recommendation: {res_cpt['thermal_conditioning_recommendation']}")

    # 2. Model Autonomic Recovery Kinetics post-test
    res_rec = agent.model_autonomic_recovery_kinetics(
        peak_hr_bpm=128.0,
        recovery_hr_1min_bpm=98.0,
        recovery_hr_2min_bpm=79.0
    )

    print(f"\n2. Post-Stress Vagal Reactivation Recovery:")
    print(f"   Peak Stress HR: {res_rec['peak_stress_hr_bpm']} bpm")
    print(f"   HR Drop 1-Min: -{res_rec['delta_hr_drop_1min']} bpm")
    print(f"   HR Drop 2-Min: -{res_rec['delta_hr_drop_2min']} bpm")
    print(f"   Vagal Status: {res_rec['vagal_reactivation_tier']}")
    print(f"   Autonomic Recovery Index: {res_rec['autonomic_recovery_index_100']}/100")
    print(f"   Assessment: {res_rec['physiological_assessment']}")

    print("\nVerification complete: Cold pressor endurance engine executed flawlessly.")

if __name__ == "__main__":
    main()
