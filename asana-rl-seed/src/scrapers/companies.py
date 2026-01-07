"""
Company name provider for realistic organization simulation.

Live scraping is intentionally avoided to ensure reproducibility.
This module can be extended to scrape sources such as YC or Crunchbase
in future iterations.
"""

import random

COMPANY_NAMES = [
    "Nimbus Systems",
    "Vertex Labs",
    "Atlas Software",
    "BlueStack Analytics",
    "Orbit Technologies",
    "PulseAI",
    "CloudNest",
    "ScaleForge",
    "NovaWorks",
    "SignalFlow"
]

def get_company_name() -> str:
    """
    Return a realistic B2B SaaS company name.
    """
    return random.choice(COMPANY_NAMES)
