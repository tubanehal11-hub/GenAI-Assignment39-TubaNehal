
---
title: GenAI Assignment 39 - GenAI App Deployment
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: streamlit
app_file: app.py
pinned: false
---

# GenAI Assignment 39 – GenAI App Deployment

## Objective
To deploy a GenAI application using Streamlit Community Cloud, explore Hugging Face Spaces, and compare different application deployment platforms.

## Technologies Used
- Python
- Streamlit
- GitHub
- Streamlit Community Cloud
- Hugging Face Spaces

## Project Files
- `app.py` – Main Streamlit application.
- `requirements.txt` – Required Python dependencies.
- `README.md` – Project documentation and deployment status.

## Installation
Install the required dependencies:

```bash
python3.14 -m pip install -r requirements.txt
```

## Run the Application Locally
Execute the following command:

```bash
python3.14 -m streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

## Task 1: Deployment on Streamlit Community Cloud

### Work Completed
1. Created the Streamlit application in `app.py`.
2. Added the required dependency to `requirements.txt`.
3. Uploaded the project files to GitHub.
4. Deployed the application using Streamlit Community Cloud.
5. Tested the application by entering text and clicking the Submit button.
6. Confirmed that the application displayed the submitted text with a success message.

### Pending Verification
The public application URL could not be re-verified because the Streamlit Community Cloud sign-in page returned an error during resubmission.

**Live Application URL:** Pending verification.

The local URL `http://localhost:8501/` is only for local testing and is not a public deployment URL.

## Task 2: Deployment on Hugging Face Spaces

### Work Completed
1. Opened Hugging Face Spaces.
2. Started the process of creating a new Space.
3. Reviewed the available SDK and visibility options.
4. Selected the MIT license during configuration.
5. Added Hugging Face Streamlit metadata to this README.

### Reason for Incomplete Deployment
During Space creation, the available options showed Static as free, while Gradio and Docker were marked as requiring a paid plan. The account also displayed a message stating that compute-based Spaces require PRO.

The Static SDK cannot directly run the existing Streamlit application. Therefore, the Hugging Face deployment could not be completed without a suitable Streamlit-compatible runtime.

No public Hugging Face Space has been successfully deployed or tested yet.

### Hugging Face Configuration Metadata
The YAML metadata at the top of this README specifies:

- `sdk: streamlit` – Intended SDK.
- `app_file: app.py` – Main application file.

This metadata documents the intended configuration but does not itself create or deploy a Space.

## Task 3: Comparison of Deployment Platforms

### Streamlit Community Cloud

**Advantages**
- Simple deployment for Streamlit applications.
- Integration with GitHub repositories.
- Provides a public URL for sharing applications.
- Suitable for interactive Python applications.

**Limitations**
- Intended primarily for Streamlit applications.
- Package compatibility and resource limits can affect deployment.

**When to use:** Use Streamlit Community Cloud when building an interactive application with Streamlit and requiring a straightforward deployment workflow.

### Hugging Face Spaces

**Advantages**
- Useful for sharing AI and machine-learning demonstrations.
- Integrates with the Hugging Face ecosystem.
- Supports Git-based project workflows.
- Provides a platform for showcasing models and applications.

**Limitations**
- Requires a compatible SDK and correct application configuration.
- Available compute resources depend on the selected hardware and account options.
- Some deployment configurations may require a paid plan.

**When to use:** Use Hugging Face Spaces when showcasing AI/ML applications or integrating with Hugging Face models and datasets.

### Comparison Table

| Feature | Streamlit Community Cloud | Hugging Face Spaces |
|---|---|---|
| Main purpose | Hosting Streamlit applications | Hosting AI/ML demonstrations |
| Git integration | Supported | Supported |
| Public sharing | Public application URL | Public Space URL |
| Configuration | Python file and dependencies | SDK, application file and dependencies |
| Best suited for | Interactive Streamlit apps | AI/ML demonstrations |
| Resource options | Subject to platform limits | Depends on SDK and available hardware |

## Testing and Validation

- [x] Streamlit application created.
- [x] `requirements.txt` created with the required dependency.
- [x] Project uploaded to GitHub.
- [x] Local application tested.
- [x] Streamlit deployment tested previously.
- [x] Deployment platforms compared.
- [x] Deployment limitations documented.
- [ ] Public Streamlit URL re-verified.
- [ ] Hugging Face Space deployed and tested.

## Conclusion

This assignment demonstrates the creation, testing, and deployment workflow of a Streamlit application. The project files were uploaded to GitHub, and the Streamlit application was tested successfully.

A comparison of Streamlit Community Cloud and Hugging Face Spaces was also documented. However, the public Streamlit URL could not be re-verified because of a sign-in error, and Hugging Face deployment remains incomplete because the available account options did not provide a suitable free compute-based setup.

These limitations have been documented transparently for review and further completion.