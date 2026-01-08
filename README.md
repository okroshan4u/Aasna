# Asana RL Seed Data Generator

## Overview

This repository provides a complete, reproducible pipeline for generating high-quality synthetic seed data for a **reinforcement learning (RL) environment** simulating **Asana**, an enterprise project management platform.

The generated dataset models a realistic **B2B SaaS organization** (~7,000 users) using Asana across **Product**, **Marketing**, and **Operations** teams. The primary goal is to create data that supports meaningful evaluation and fine-tuning of **computer-use AI agents**, while avoiding unrealistic shortcuts or uniform distributions.

The output is a fully populated **SQLite database** representing a realistic Asana workspace, including:

- Tasks  
- Subtasks  
- Comments  
- Collaboration metadata  

This dataset can be used for testing RL agents in a realistic enterprise collaboration setting.

## Features

- Realistic user and team structure across multiple departments  
- Task hierarchies with subtasks  
- Rich metadata including comments and collaboration events  
- Fully reproducible synthetic dataset  

## Getting Started

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Follow the instructions in the pipeline scripts to generate the synthetic database.  

## Use Cases

- Training reinforcement learning agents for productivity tools  
- Evaluating AI agents in realistic task and collaboration scenarios  
- Testing analytics or reporting algorithms on enterprise task data  

---

