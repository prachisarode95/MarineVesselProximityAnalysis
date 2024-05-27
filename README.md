
# Marine Vessel Proximity Analysis

This project demonstrates the marine vessel proximity analysis using data science libraries. It analyzes vessel proximity events using the Haversine formula, Pandas vectorization method, and visualizes final results using Matplotlib or Plotly.

## Project Structure

- **data/sample_data.csv**: Contains the Vessel positions, Vessel IDs, and Timestamp data.
- **src/Marine_Vessel_Proximity_Analysis.py and Marine_Vessel_Proximity_Analysis.ipynb**: Python scripts to run the analysis.
- **README.md**: Project documentation.
- **requirements.txt**: Python dependencies.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/<repository-name>.git
    cd <repository-name>
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the analysis script:

    ```bash
    python src/Marine_Vessel_Proximity_Analysis.py
    ```

## Explanation of the Code

1. **Import Libraries**:
    - `pandas`: For data manipulation.
    - `numpy`: For numerical operations.
    - `plotly`: For interactive visualization.

2. **Load Data**:
    - Load vessel positions from the `sample_data.csv`.

3. **Haversine Formula**:
    - Calculate distances between geographic coordinates of vessels using the Haversine formula.

4. **Calculate Pairwise Distances**:
    - Generate all possible pairs of vessel positions and calculate distances between them.

5. **Filter Proximity Events**:
    - Identify vessel pairs within the specified proximity threshold.

6. **Visualization**:
    - Visualize vessel positions and highlight proximity events using Plotly.

## Data

- Ensure your data file (`sample_data.csv`) is in the `data` directory.

## Final Results

![Marine Vessel Proximity Plot](https://github.com/prachisarode95/MarineVesselProximityAnalysis/assets/60979131/c6f651b1-275d-466b-8118-6e3b81aeaeaa)



