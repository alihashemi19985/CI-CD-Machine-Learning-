
# CI/CD for Machine Learning

## Overview

**Continuous Integration and Continuous Deployment (CI/CD)** is a software development practice that enables teams to deliver code changes more frequently and reliably. CI/CD automates the process of integrating code changes from multiple contributors into a shared repository and deploying those changes to production environments.

### Key Concepts

- **Continuous Integration (CI)**: The practice of automatically testing and merging code changes into a shared repository. This ensures that new changes do not break existing functionality.
  
- **Continuous Deployment (CD)**: The practice of automatically deploying code changes to production after passing tests. This allows teams to release new features and fixes quickly.

## Project Description

This project, **WebSmart**, is about predicting passengers' survival on the Titanic using machine learning. The dataset used in this project is the Titanic dataset from Kaggle. The dataset contains information about the passengers on the Titanic and whether they survived or not. This project aims to build a machine-learning model that can predict whether a passenger survived based on the information available in the dataset. The project is designed to demonstrate CI/CD practices using GitHub Actions and Render for deployment.

## Features


- Docker containerization for consistent deployment
- CI/CD pipeline set up with GitHub Actions
- Deployment to Render

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12 or higher
- Docker installed on your machine
- GitHub account
- Docker Hub account (for pushing Docker images)
- Render account (for deployment)

## Getting Started

To get a local copy of this project up and running, follow these steps:

### Step 1: Prerequisites
Before you start, make sure you have the following:

GitHub Repository: Your project should be hosted on GitHub.
Docker Hub Account: You need an account to store your Docker images.
Render Account: You need an account on Render to deploy your application.
Secrets in GitHub: Store sensitive information like your Docker Hub credentials and Render API key in GitHub Secrets.
### Step 2: Create GitHub Secrets
Go to your GitHub repository, click on Settings, then Secrets and variables > Actions. Add the following secrets:

DOCKER_USERNAME: Your Docker Hub username.
DOCKER_PASSWORD: Your Docker Hub password.
RENDER_API_KEY: Your Render API key.
### Step 3: Create the CI/CD Workflow File
### Step 4: Create an Account on Render
Visit the Render Website:
Go to Render’s website.

Sign Up:

Click on the “Sign Up” button located at the top right corner of the homepage.
You can sign up using your GitHub account or your email address. If you choose to sign up with GitHub, you will be redirected to authorize Render to access your GitHub account.
Complete the Registration:

If you signed up with email, follow the instructions to verify your email address and complete the registration process.
### Step 5: Create a New Web Service
Log In:
After creating your account, log in to the Render dashboard.

Create a New Service:

On the Render dashboard, click on the “New” button or “Create a New Service” option.
Select “Web Service” from the dropdown menu.
Configure Your Service:

Name: Give your service a name (e.g., WebSmart_CICD).
Environment: Choose the environment type (e.g., Docker if you are using Docker).
Branch: Specify the branch you want to deploy from (e.g., main).
Repository: Connect your GitHub repository by selecting it from the list or entering the URL.
Root Directory: If your application is in a subdirectory, specify the path. Otherwise, leave it blank.
Build Command: If you are using Docker, you can leave this blank, as Docker will handle it.
Start Command: Specify the command to run your application (e.g., python run.py).
Set Up Environment Variables (if needed):
If your application requires any environment variables (like API keys), you can set them in the Environment Variables section.

Create the Service:
Click on the “Create Web Service” button to create the service.

### Step 6: Obtain the Service ID
View Your Service:
Once the service is created, you will be taken to the service dashboard.

Locate the Service ID:

In the service dashboard, you will see the service details.
The Service ID is typically displayed in the URL of the service or in the service details section. It will look something like this: srv-xxxxxxxxxxxxxxxxxxxxx.
Copy the Service ID:
Make sure to copy the Service ID, as you will need it for your CI/CD pipeline configuration.

### step 7: Commit and Push

