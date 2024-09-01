# Mutual Fund Broker Web Application

This is a full-stack web application designed for a mutual fund brokerage firm. The application allows users to select a fund family house, fetch open-ended schemes for that family, and view mutual fund data via integration with RapidAPI. Users can also initiate the purchase of mutual fund units through the application. The backend is developed using FastAPI, and the frontend can be built using a modern framework like React, Angular, Vue.js, or plain HTML/CSS/JavaScript.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (FastAPI)](#backend-setup-fastapi)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
  - [Login](#login)
  - [Dashboard](#dashboard)
  - [View and Buy Mutual Funds](#view-and-buy-mutual-funds)
- [Integration with RapidAPI](#integration-with-rapidapi)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [License](#license)

## Features
- User authentication using dummy credentials.
- Integration with RapidAPI to fetch mutual fund data.
- Dashboard for selecting fund family houses and viewing open-ended schemes.
- Ability to view details of individual mutual funds.
- Option to purchase mutual fund units.
- Responsive design for seamless usage across devices.

## Technology Stack
- **Backend**: Python, FastAPI
- **Frontend**: [Your choice: React, Angular, Vue.js, or plain HTML/CSS/JavaScript]
- **Authentication**: JWT (JSON Web Tokens)
- **API Integration**: RapidAPI (https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav)
- **Environment Variables**: Python-dotenv

## Setup Instructions

### Backend Setup (FastAPI)
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo/mutual-fund-broker.git
    cd mutual-fund-broker/backend
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4**Run the FastAPI Server**:
    ```bash
    uvicorn main:app --reload
    ```
   The backend will be running on `http://127.0.0.1:8000`.

## Usage

### Login
1. Open the application in your browser (e.g., `http://localhost:3000` for React, Angular, Vue.js).
2. Enter the dummy username and password defined in your `.env` file to log in.

### Dashboard
1. After logging in, you will be redirected to the dashboard.
2. Select a fund family house from the dropdown menu to view available open-ended schemes.

### View and Buy Mutual Funds
1. Click on any mutual fund from the list to view more details.
2. Use the "Buy" button to initiate the purchase of units for the selected mutual fund.

## Integration with RapidAPI
The application uses the RapidAPI service to fetch the latest mutual fund data. Ensure that you have signed up on RapidAPI and obtained the necessary API key, which should be included in your `.env` file.

## Environment Variables
Ensure that the following environment variables are set in your `.env` file:
```env
RAPIDAPI_KEY=your-rapidapi-key
DUMMY_USERNAME=your-dummy-username
DUMMY_PASSWORD=your-dummy-password
