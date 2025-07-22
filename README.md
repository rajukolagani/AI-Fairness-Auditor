# AI Fairness & Bias Auditor ⚖️

This web application audits a machine learning model for ethical bias. It trains a model to predict income based on census data and then measures its fairness across different demographic groups using the **Disparate Impact** metric. This project highlights the importance of building responsible and equitable AI systems.

## Features

-   **Fairness Auditing:** Audits a classification model for fairness based on protected attributes like gender and race.
-   **Calculates Disparate Impact:** Provides a clear, industry-standard score to measure the level of bias.
-   **Dynamic Reporting:** Shows how model performance and positive outcome rates differ between privileged and unprivileged groups.
-   **Simple Web Interface:** Built with Flask for easy interaction.

## Tech Stack

-   **Backend:** Python, Flask
-   **Machine Learning:** Scikit-learn, Pandas, Numpy
-   **Frontend:** HTML, CSS

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rajukolagani/AI-Fairness-Auditor.git](https://github.com/rajukolagani/AI-Fairness-Auditor.git)
    cd AI-Fairness-Auditor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv
    
    # Activate on Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare the dataset:**
    (This only needs to be run once)
    ```bash
    python prepare_data.py
    ```

5.  **Run the Flask app:**
    ```bash
    flask run
    ```
    Open your browser and navigate to `http://127.0.0.1:5000`.
