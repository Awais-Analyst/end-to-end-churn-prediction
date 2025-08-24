Project Description
This project demonstrates a complete, end-to-end machine learning pipeline to predict customer churn. It showcases all the key phases of a modern data science project, from data processing and modeling to deployment.

Key Components
Data Processing: Utilized Polars for highly efficient data manipulation and DuckDB as an in-process analytical database for fast data querying.

Modeling: Employed PyCaret, a low-code machine learning library, to streamline model training, evaluation, and selection. This approach allowed for rapid experimentation and the selection of the best-performing model.   

API: The trained model was containerized using FastAPI and Uvicorn and then deployed on Render to serve predictions via a REST API.

Dashboard: An interactive web dashboard was built with Streamlit to provide a user-friendly interface for interacting with the live prediction API.

Deployment: The entire project is professionally hosted, with the API on Render and the Streamlit dashboard on Streamlit Community Cloud.

Live Demo
Access the live Streamlit dashboard here:
(https://end-to-end-churn-prediction-mgdmhobuc7vgfqgiylsfr3.streamlit.app/)

How to Run the Project Locally
Clone the repository:

Bash

git clone https://github.com/Awais-Analyst/end-to-end-churn-prediction.git
cd end-to-end-churn-prediction
Set up the virtual environment:
Creating a dedicated environment is a best practice to manage project dependencies.

Bash

# You might use conda, venv, or other tools
# Example for venv:
python -m venv pycaret-env
pycaret-env\Scripts\activate.ps1
Install the required packages:

Bash

pip install -r requirements.txt
Run the Streamlit app:

Bash

streamlit run app.py
This will open the dashboard in your web browser.

Author
Muhammad Awais Mustafa
