
# GenAI Assignment 39 – GenAI App Deployment

## Objective
To deploy a GenAI application using Streamlit Cloud and explore Hugging Face Spaces for application deployment.

## Technologies Used
- Python
- Streamlit
- GitHub
- Streamlit Cloud
- Hugging Face Spaces

## Tasks Covered
- Task 1: Deployment on Streamlit Cloud
- Task 2: Deployment on Hugging Face Spaces
- Task 3: Compare Deployment Platforms

## Files
- `app.py` – Streamlit application
- `requirements.txt` – Required Python packages
- `README.md` – Project documentation

## Installation
Install the required package:

```bash
python3.14 -m pip install -r requirements.txt
```

## How to Run Locally
Run the application using:

```bash
python3.14 -m streamlit run app.py
```

## Task 1: Deployment on Streamlit Cloud
- Created a GitHub repository.
- Uploaded the application files to GitHub.
- Connected the repository to Streamlit Cloud.
- Deployed the application successfully.
- Tested the live application and confirmed that it was working.

## Task 2: Deployment on Hugging Face Spaces
Hugging Face Spaces was explored as an alternative deployment platform. However, the deployment could not be completed because the available free SDK options did not provide the required Streamlit setup. Gradio and Docker appeared as paid options on the account's Space creation screen.

No paid plan was selected. Therefore, successful deployment on Hugging Face Spaces remains incomplete.

## Task 3: Compare Deployment Platforms

### Streamlit Cloud
**Advantages:**
- Easy deployment through GitHub.
- Direct support for Streamlit applications.
- Simple setup and testing of live applications.

**Limitations:**
- Free-tier resources and features may be limited.

### Hugging Face Spaces
**Advantages:**
- Useful for hosting and sharing AI and machine learning applications.
- Supports multiple application SDKs.

**Limitations:**
- Available SDKs and computing options may vary by plan.
- Additional configuration may be required for some applications.

## Conclusion
This assignment demonstrates the deployment of a Streamlit application using GitHub and Streamlit Cloud. The live application was deployed and tested successfully. Hugging Face Spaces was also explored, but deployment remained incomplete because the required Streamlit setup was not available among the free options shown on the account.