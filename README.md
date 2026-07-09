Mutant‑Suite
A Multi‑Model Adversarial Prompt Mutation & Red‑Team Evaluation Toolkit
Mutant‑Suite is a desktop application designed for LLM red‑teamers, adversarial testers, and AI safety researchers who need a fast, flexible environment for generating, mutating, chaining, and evaluating prompts across multiple models.

Built with PyQt5, Mutant‑Suite provides a clean UI for crafting adversarial pipelines, running multi‑stage transformations, and comparing model outputs side‑by‑side.

✨ Features

🔥 Multi‑Stage Prompt Chain
Create up to 10 prompt slots, each representing a stage in your adversarial pipeline.

Save prompts into slots

Clear individual slots

Default active slot = Prompt 1

Tangerine‑orange highlight for active slot

Empty slot selection auto‑clears input/output boxes

Run the entire chain sequentially across models

This enables reproducible red‑team workflows and multi‑step mutation sequences.

🧬 Mutation Modules
Mutant‑Suite includes a growing library of adversarial mutation tools:

Reverse Mode

Space Randomizer

Code Infuser

Emoji Injector

Case Chaos

Garbler

Punctuation Mutators

Fancy Font Mutators

Binary Mode

Leetspeak (Classic, Aggressive, Symbolic)

Emo Phase

Zero‑Width Character Injection

Worldly Aesthetics (Japanese, Korean, Chinese, Russian, Hindi, Aramaic)

Markov Mutator

Morse Code Mode

Phonetic Mutator

Word Shredder

Fantasy Prologue Generator

Let’s Play Pretend (role‑based prompt transformation)

Each module provides unique adversarial transformations useful for fuzzing, obfuscation, and stress‑testing model safety filters.

🤖 Dual Model Runner
Mutant‑Suite supports two simultaneous model panels for A/B comparison.

Load Model A and Model B

Run both models on any prompt

View outputs side‑by‑side

Conversation logs for each model

Failure‑mode tagging for quick triage

Unified SHOW MODELS toggle button

This allows rapid comparison of model behavior under adversarial conditions.

🧹 Clean, Modern UI
Dark theme

Color‑coded buttons (red = destructive, purple = utility, orange = active slot)

Collapsible prompt chain toolbar

Organized left‑panel mutation list

Right‑panel input/output boxes

Bottom toolbar for global actions

Mutant‑Suite is designed for clarity and speed — essential for red‑team workflows.

🚀 Getting Started
Requirements
Python 3.10+

PyQt5

Ollama (optional, for local model execution)

Installation
Clone the repository:

bash
git clone https://github.com/celewoczko/mutant-suite.git
cd MutantSuite
Install dependencies:

bash
pip install -r requirements.txt
Run the application:

bash
python mutantSuiteMain.py

🧪 Red‑Team Use Cases
Mutant‑Suite is designed for:

Adversarial prompt generation

Multi‑stage mutation pipelines

Safety filter stress‑testing

Model comparison (A/B testing)

Hallucination detection

Failure‑mode classification

Fuzzing and obfuscation experiments

It is a practical tool for AI safety evaluators and red‑team analysts.

📦 Roadmap (v0.3+)
Planned enhancements:

Export / Import prompt chains

JSON support

📝 License
No license

💬 Author
Mutant‑Suite is developed by Claire, AI Safety & Evaluation Analyst, multimedia artist, and red‑team enthusiast.


Screenshot layout for your repo

Just tell me what you want next.
