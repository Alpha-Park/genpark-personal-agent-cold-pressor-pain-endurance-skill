# -*- coding: utf-8 -*-
"""Personal Agent Cold Pressor Pain Endurance Skill.

Zero-dependency Cold Pressor Test (CPT) pain threshold and tolerance modeler,
central autonomic pain gating quantifier, and sympathetic withdrawal recovery evaluator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentColdPressorPainEndurance:
    """Quantitative thermal nociception and autonomic resilience modeler based on
    the clinical Cold Pressor Test (CPT) standard protocol."""

    def evaluate_cpt_pain_tolerance(
        self,
        water_temp_celsius: float = 3.0,
        pain_threshold_seconds: float = 18.0,
        pain_tolerance_seconds: float = 75.0,
        subjective_pain_vas_10: float = 7.5
    ) -> Dict[str, Any]:
        """Calculates pain sensitivity index (PSI), endurance ratio, and central pain gating tier."""
        # Sanitize inputs
        temp = max(0.5, min(10.0, float(water_temp_celsius)))
        t_thresh = max(1.0, float(pain_threshold_seconds))
        t_tol = max(t_thresh, float(pain_tolerance_seconds))
        vas = max(0.0, min(10.0, float(subjective_pain_vas_10)))

        # Thermal challenge severity multiplier (colder water = exponentially higher nociceptive drive)
        # Baseline reference: 4.0 C
        temp_multiplier = math.exp((4.0 - temp) * 0.15)

        # Pain Endurance Window (latency between threshold awareness and voluntary termination)
        endurance_window_seconds = round(t_tol - t_thresh, 1)
        endurance_ratio = round(t_tol / t_thresh, 2)

        # Pain Sensitivity Index (PSI: lower is more resilient, range ~5 - 150)
        # Normalized by temperature challenge and subjective VAS
        psi_raw = (vas * 10.0) / max(1.0, (endurance_window_seconds / 10.0)) * temp_multiplier
        psi = round(min(150.0, max(5.0, psi_raw)), 1)

        # Central Pain Gating Classification
        if t_tol >= 120.0:
            gating_tier = "Elite Neurogenic Resilience / Superior Pain Gating"
            endogenous_modulation = "High descending noradrenergic and opioid inhibitory pathway activation"
        elif t_tol >= 60.0:
            gating_tier = "High Pain Tolerance / Adaptive Central Gating"
            endogenous_modulation = "Moderate central inhibition of dorsal horn nociceptive transmission"
        elif t_tol >= 30.0:
            gating_tier = "Normative Physiological Pain Response"
            endogenous_modulation = "Standard baseline spinothalamic ascending noxious signaling"
        else:
            gating_tier = "Acute Nociceptive Sensitization / Low Pain Threshold"
            endogenous_modulation = "Elevated sympathetic hyper-reactivity; rapid withdrawal reflex dominance"

        # Autonomic Distress Score (ADS: 0 - 100)
        ads = min(100.0, round((vas * 7.0) + (temp_multiplier * 15.0) - (endurance_ratio * 4.0), 1))

        return {
            "water_temperature_celsius": round(temp, 1),
            "pain_threshold_latency_seconds": round(t_thresh, 1),
            "pain_tolerance_latency_seconds": round(t_tol, 1),
            "pain_endurance_window_seconds": endurance_window_seconds,
            "endurance_ratio": endurance_ratio,
            "subjective_vas_score_10": vas,
            "pain_sensitivity_index_psi": psi,
            "central_pain_gating_tier": gating_tier,
            "endogenous_neuromodulation_status": endogenous_modulation,
            "autonomic_distress_score": max(0.0, ads),
            "thermal_conditioning_recommendation": (
                "Progress to 3x weekly 2-minute cold water immersion (4-6 C) combined with slow nasal diaphragmatic exhalations."
                if t_tol < 90.0 else
                "Preserve current parasympathetic control under acute sympathetic vasoconstrictive challenge."
            )
        }

    def model_autonomic_recovery_kinetics(
        self,
        peak_hr_bpm: float,
        recovery_hr_1min_bpm: float,
        recovery_hr_2min_bpm: float
    ) -> Dict[str, Any]:
        """Evaluates parasympathetic vagal reactivation velocity following acute cold-stress termination."""
        hr_drop_1m = round(peak_hr_bpm - recovery_hr_1min_bpm, 1)
        hr_drop_2m = round(peak_hr_bpm - recovery_hr_2min_bpm, 1)

        # Heart Rate Recovery (HRR) benchmarks:
        # 1-min drop > 25 bpm: Excellent vagal recovery
        # 1-min drop 18-25 bpm: Good / Normative
        # 1-min drop 12-17 bpm: Blunted parasympathetic reactivation
        # 1-min drop < 12 bpm: High autonomic exhaustion / delayed vagal tone
        if hr_drop_1m >= 25.0:
            vagal_status = "Optimal Vagal Reactivation / Fast Sympathetic Withdrawal"
            autonomic_margin = "High parasympathetic brake engagement; low allostatic recovery cost"
        elif hr_drop_1m >= 18.0:
            vagal_status = "Normative Vagal Recovery"
            autonomic_margin = "Standard post-stress homeostatic resolution"
        elif hr_drop_1m >= 12.0:
            vagal_status = "Blunted Parasympathetic Reactivation"
            autonomic_margin = "Delayed vagal rebound; residual adrenergic tone lingering"
        else:
            vagal_status = "Impaired Autonomic Flexibility"
            autonomic_margin = "Sympathetic overdrive persisting post-thermal stressor"

        autonomic_recovery_index = min(100.0, round((hr_drop_1m * 2.5) + (hr_drop_2m * 1.0), 1))

        return {
            "peak_stress_hr_bpm": round(peak_hr_bpm, 1),
            "hr_recovery_1min_bpm": round(recovery_hr_1min_bpm, 1),
            "hr_recovery_2min_bpm": round(recovery_hr_2min_bpm, 1),
            "delta_hr_drop_1min": hr_drop_1m,
            "delta_hr_drop_2min": hr_drop_2m,
            "vagal_reactivation_tier": vagal_status,
            "autonomic_recovery_index_100": max(0.0, autonomic_recovery_index),
            "physiological_assessment": autonomic_margin
        }
