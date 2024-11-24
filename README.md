# Building a Generic Frappe Connector for Seamless Data Storage from FastAPI Service

## Summary

This project aims to connect a FastAPI service with a Frappe-based management system to store and manage data easily. Although I am new to Frappe, I am excited about learning it because it offers a great learning curve. I have already set up Frappe and created a basic FastAPI link for your reference.

The approach for this project is to:
1. Build a FastAPI service to send data.
2. Set up Frappe to store the data.
3. Create a simple dashboard to display the data in a table format.

Throughout the project, I will focus on testing each component to ensure proper functionality and will also document the entire process to help others understand the setup and usage. This will allow me to learn Frappe while working on a practical solution, ensuring reliability and ease of use.

## Screenshots

### 1. Proof of Frappe Installation
This screenshot shows the successful installation of Frappe on my system.
![Frappe Installation](https://github.com/Asp-Codes/DataConnector/blob/main/Screenshot%20from%202024-11-25%2002-32-49.png)

### 2. FastAPI Response
This screenshot demonstrates the response from the FastAPI service when the data is sent.
![FastAPI Response](https://github.com/Asp-Codes/DataConnector/blob/main/Screenshot%20from%202024-11-25%2002-38-54.png)

## FastAPI Service (`main.py`)

A basic demo file for the FastAPI service is provided. It sets up a simple endpoint to send data.
