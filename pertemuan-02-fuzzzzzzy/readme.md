# Fuzzy Movie Quality Classification

Notebook: [pertemuan-02-fuzzzzzzy/fuzzy.ipynb](pertemuan-02-fuzzzzzzy/fuzzy.ipynb)  
Supporting data:

- Cleaned input dataset: [pertemuan-02-fuzzzzzzy/data-cleaned.csv](pertemuan-02-fuzzzzzzy/data-cleaned.csv)
- Generated ranked output: [pertemuan-02-fuzzzzzzy/top-movies.csv](pertemuan-02-fuzzzzzzy/top-movies.csv)  
  Environment checks:
- Setup script: [pertemuan-01-setup/verify_installation.py](pertemuan-01-setup/verify_installation.py)
- Notebook check: [pertemuan-01-setup/setup_check.ipynb](pertemuan-01-setup/setup_check.ipynb)  
  Dependencies: [requirements.txt](requirements.txt)

## Objective

Build a fuzzy inference system to score and categorize movies using:

1. IMDb average rating
2. Release year
3. Number of IMDb votes

Output: A fuzzy-derived movie_quality score ($0$–$10$) and a discrete category: High / Medium / Low.

## Fuzzy Variables

Inputs:

- imdb_rating: universe 0–10
  - low: trapmf [0, 0, 3, 5]
  - medium: trimf [4, 5.5, 7]
  - high: trapmf [6, 8, 10, 10]
- release_year: dynamic range [min_year, max_year] from dataset
  - classic: trapmf [min, min, 1970, 1990]
  - modern: trimf [1985, 2000, 2010]
  - contemporary: trapmf [2000, 2020, max, max]
- num_votes: 0–max_votes (step 10,000)
  - few: trapmf [0, 0, 50k, 150k]
  - average: trimf [100k, 200k, 400k]
  - many: trapmf [300k, 500k, max, max]

Output:

- movie_quality: universe 0–10
  - low: trapmf [0, 0, 3, 5]
  - medium: trimf [4, 5.5, 7]
  - high: trapmf [6, 8, 10, 10]

## Rule Base (skfuzzy.control)

Rules (logical AND/OR over membership grades):

1. High rating & Many votes → High
2. Medium rating & Average votes → Medium
3. Low rating & Few votes → Low
4. High rating & Classic → High
5. Medium rating & Modern → Medium
6. Low rating OR Few votes → Low
7. High rating → High
8. Medium rating → Medium
9. Low rating → Low

Redundancy is intentional for stability and coverage.

## Inference Flow

1. Load dataset.
2. Define universes dynamically (year, votes).
3. Build membership functions.
4. Instantiate ControlSystem with rules.
5. For each row:
   - Clip inputs to defined universes.
   - Compute fuzzy output.
6. Defuzzification method: centroid (default in skfuzzy).
7. Post-process:
   - movie_quality_score stored in column.
   - Classification:
     - High: score ≥ 6.0
     - Medium: 4.0 ≤ score < 6.0
     - Low: score < 4.0

Category thresholds are crisp, outside fuzzy system. You can adjust them if distribution skews.

## Generated Artifacts

- Top ranked list: [pertemuan-02-fuzzzzzzy/top-movies.csv](pertemuan-02-fuzzzzzzy/top-movies.csv)
- Visualizations:
  - Membership function plots
  - Distribution histogram of scores
  - Bar chart of category counts

## How to Run

1. Create and activate virtual environment.
2. Install dependencies:
   pip install -r requirements.txt
3. (Optional) Run environment check:
   python pertemuan-01-setup/verify_installation.py
4. Open the notebook:
   jupyter notebook pertemuan-02-fuzzzzzzy/fuzzy.ipynb
5. Run all cells sequentially.

## Extending

- Add new input (e.g., genre popularity) as another Antecedent.
- Tune membership breakpoints using quantiles.
- Replace rule6 (broad OR) if it over-suppresses medium/high outcomes.
- Export rule surface by sampling inputs and plotting.

## Notes

- Each row uses a fresh ControlSystemSimulation to avoid state leakage.
- Inputs are clipped to prevent out-of-universe errors.
- If NaNs appear, check for missing source fields in data-cleaned.csv.

## Quick Math Summary

Score domain: $score \in [0, 10]$  
Classification mapping:

$$
category(score)=
\begin{cases}
\text{High}, & score \ge 6.0 \\
\text{Medium}, & 4.0 \le score < 6.0 \\
\text{Low}, & score < 4.0
\end{cases}
$$

## Troubleshooting

- All outputs NaN: check that rules list is passed into ControlSystem.
- Slow execution: vectorize by batching only if you redesign simulation; current approach trades speed for correctness.
- Skewed categories: adjust membership overlaps or thresholds.

## License / Usage

Academic / instructional usage implied. Add a LICENSE file if distribution needed.
