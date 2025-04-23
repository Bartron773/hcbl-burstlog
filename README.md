# hcbl-burstlog
A system designed to detect and measure creativity over time through semantic embedding analysis and novelty scoring 
🧠 HCBL: Human Creative Burst Log – Novelty Analysis Notebook

Welcome to the creative cognition lab! This notebook simulates a local version of Bart’s Human Creative Burst Log (HCBL) system — designed to detect and measure creativity over time through semantic embedding analysis and novelty scoring.

📍 Purpose

This notebook serves as a tool to:
	•	Analyze the semantic novelty of new thoughts (“creative bursts”) compared to prior ones.
	•	Visualize how each idea deviates from your historical thinking patterns.
	•	Track ideational growth, divergence, or self-similarity over time.

🔍 How It Works
	1.	Stores a log of previous bursts (each with a cosine distance-style embedding score).
	2.	Accepts a new burst’s distance value.
	3.	Calculates:
	•	Mean and standard deviation of past distances
	•	k-nearest distances and their average
	•	Z-score of the new burst
	•	A normalized novelty score between 0 and 1
	4.	Visualizes the data via histogram and markers

✨ Key Concepts
	•	🧠 Semantic Distance: Cosine distance from embedding vector comparison
	•	📈 Z-Score: Measures how far a burst deviates from your mean
	•	🔥 Relative Novelty Score: Z-score scaled to 0–1 (used for thresholding novelty)
	•	📊 Visualization: Highlights new burst, mean, and baseline distribution

📦 Dependencies
	•	Python 3.x
	•	numpy
	•	matplotlib

Install with:

pip install numpy matplotlib

🛠️ To Use
	1.	Open burst_analysis_notebook.py
	2.	Replace new_burst_distance with a distance value from your own model
	3.	Run the script
	4.	View novelty output + histogram

🧬 Future Integrations
	•	Connect to actual LLM-based embedding service (e.g., OpenAI, local LLaMA)
	•	Store bursts in a database or markdown log
	•	Add emotional/linguistic metadata per burst
	•	Build a live dashboard in Streamlit or React

🌈 Authored by

Lincoln (your creative AI sidekick), based on bursts from Bart Salazar’s existential explorations and AI-human design philosophy.

⸻

For more cosmic queries, poetic metrics, or robotOS prototypes, follow the signal. 🛰️
