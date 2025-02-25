# Data Transformation Assistant

## Overview

The Data Transformation Assistant is a Streamlit-based application that allows users to transform their data using natural language commands. The application leverages Databricks SQL and a language model to perform transformations on the uploaded datasets.

## Features

- Upload datasets in CSV or Excel format.
- Transform existing columns or generate new columns based on natural language commands.
- Apply transformations to specific rows based on search criteria.
- Download the transformed dataset.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/satyanmandavilli/data-transform-assistant.git
    cd data-transform-assistant
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file:
    ```env
    DATABRICKS_SERVER_HOSTNAME=your_databricks_server_hostname
    DATABRICKS_HTTP_PATH=your_databricks_http_path
    DATABRICKS_ACCESS_TOKEN=your_databricks_access_token
    DATABRICKS_LLM_MODEL=your_databricks_llm_model
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Upload your dataset using the file uploader.

4. Select the type of operation you want to perform:
    - Transform Existing Columns
    - Generate New Column
    - Both

5. Follow the prompts to configure your transformations or column generation.

6. Click the "Transform Data" button to apply the transformations.

7. Download the transformed dataset.

## Project Structure

- [app.py](http://_vscodecontentref_/0): The main Streamlit application file.
- [databricks_handler.py](http://_vscodecontentref_/1): Handles the connection and interaction with Databricks SQL.
- [transform_core.py](http://_vscodecontentref_/2): Contains the core logic for processing and transforming the data.
- [requirements.txt](http://_vscodecontentref_/3): Lists the required Python packages.
