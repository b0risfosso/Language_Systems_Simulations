Language Systems Simulation Pack
================================

interactive 3D Python simulations built with VPython.

Included simulations
--------------------
1. Word Formation System
2. Sentence Construction Machine
3. Grammar as a Force Field
4. Meaning Network
5. Language Evolution Over Time

Install
-------
Install Python 3, then install the required package:

    pip install -r requirements.txt

Run the launcher
----------------
From inside this folder:

    python launch.py

Run an individual simulation
----------------------------
    python simulations/word_formation_system_ai_simulation.py
    python simulations/sentence_construction_machine_ai_simulation.py
    python simulations/grammar_force_field_ai_simulation.py
    python simulations/meaning_network_ai_simulation.py
    python simulations/language_evolution_over_time_ai_simulation.py

Common controls
---------------
A       toggle AI/autonomous controller
P       pause/resume
R       reset
M       cycle AI behavior mode
C       clear temporary particles, trails, or marks
+ / -   adjust simulation speed
H       print controls

Each simulation has its own controls in the file header and in the running VPython scene.

Important note
--------------
These are visual and educational language simulations, not full natural-language parsers,
linguistic analyzers, or historically exact language-evolution models. They use simplified
symbolic rules so word formation, syntax, meaning, grammar, and evolution are visible.
