"""
Optional LLM utilities for text generation.

This module is intentionally non-blocking:
- If USE_LLM is False, deterministic templates are used.
- No API keys are required to run the pipeline.
"""

from models.config import USE_LLM

def generate_text(prompt: str) -> str:
    """
    Generate text using an LLM if enabled, otherwise return
    a deterministic placeholder based on the prompt.

    Parameters
    ----------
    prompt : str
        Input prompt describing the desired text.

    Returns
    -------
    str
        Generated text.
    """
    if not USE_LLM:
        return fallback_text(prompt)

    # Placeholder for future LLM integration
    # Example:
    # from openai import OpenAI
    # client = OpenAI()
    # response = client.responses.create(...)
    return fallback_text(prompt)


def fallback_text(prompt: str) -> str:
    """
    Deterministic fallback for reproducibility.
    """
    return f"{prompt} (generated)"
