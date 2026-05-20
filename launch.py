#!/usr/bin/env python3
"""
Language Systems Simulation Pack launcher.

Run:
    pip install -r requirements.txt
    python launch.py
"""

from pathlib import Path
import subprocess
import sys

SIM_DIR = Path(__file__).parent / "simulations"

SIMULATIONS = [
    ("Word Formation System", "word_formation_system_ai_simulation.py"),
    ("Sentence Construction Machine", "sentence_construction_machine_ai_simulation.py"),
    ("Grammar as a Force Field", "grammar_force_field_ai_simulation.py"),
    ("Meaning Network", "meaning_network_ai_simulation.py"),
    ("Language Evolution Over Time", "language_evolution_over_time_ai_simulation.py"),
]

def main():
    while True:
        print("\nLanguage Systems Simulation Pack\n")
        for i, (title, filename) in enumerate(SIMULATIONS, 1):
            status = "ready" if (SIM_DIR / filename).exists() else "missing"
            print(f"{i}. {title} [{status}]")
        print("Q. Quit")

        choice = input("\nChoose a simulation number: ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            return

        try:
            _, filename = SIMULATIONS[int(choice) - 1]
        except Exception:
            print("\nInvalid choice. Try again.")
            continue

        path = SIM_DIR / filename
        if not path.exists():
            print(f"Missing simulation file: {path}")
            continue

        subprocess.run([sys.executable, str(path)])

if __name__ == "__main__":
    main()
