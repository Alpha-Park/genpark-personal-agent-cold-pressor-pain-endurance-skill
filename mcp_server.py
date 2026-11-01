# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Cold Pressor Pain Endurance Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentColdPressorPainEndurance

mcp = FastMCP("PersonalAgentColdPressorPainEndurance")
client = PersonalAgentColdPressorPainEndurance()

@mcp.tool()
def evaluate_cpt_pain_tolerance(
    water_temp_celsius: float = 3.0,
    pain_threshold_seconds: float = 18.0,
    pain_tolerance_seconds: float = 75.0,
    subjective_pain_vas_10: float = 7.5
) -> str:
    """Evaluates cold pressor pain threshold, tolerance latency, PSI index, and central pain gating."""
    import json
    return json.dumps(client.evaluate_cpt_pain_tolerance(
        water_temp_celsius, pain_threshold_seconds, pain_tolerance_seconds, subjective_pain_vas_10
    ), indent=2)

@mcp.tool()
def model_autonomic_recovery_kinetics(
    peak_hr_bpm: float = 125.0,
    recovery_hr_1min_bpm: float = 95.0,
    recovery_hr_2min_bpm: float = 80.0
) -> str:
    """Models post-stress vagal reactivation velocity and heart rate recovery kinetics."""
    import json
    return json.dumps(client.model_autonomic_recovery_kinetics(
        peak_hr_bpm, recovery_hr_1min_bpm, recovery_hr_2min_bpm
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
