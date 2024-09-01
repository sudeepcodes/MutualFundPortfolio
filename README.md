# Mutual Fund Broker Web Application with RapidAPI Integration

## Description
Your task is to create a full-stack web application for a mutual fund brokerage firm from scratch. The application should allow users to select a fund family house, fetch open-ended schemes for that family, and integrate with RapidAPI to fetch mutual fund data. All API endpoints should be authenticated. You have the freedom to choose any frontend approach, including using a modern framework like React, Angular, or Vue.js, or developing without any framework.

## Requirements

### Frontend
- Develop a web application frontend using the approach of your choice, which can include using a framework like React, Angular, or Vue.js, or developing without any framework.
- Implement a simple login page where users can enter their credentials (dummy username and password).
- Upon successful login, users should be redirected to a dashboard where they can view mutual funds.
- Create a dashboard page where users can select the fund family house (e.g., HDFC, ICICI, SBI) from a dropdown menu.
- Display a list of open-ended schemes for the selected fund family house.
- Allow users to click on a mutual fund to view more details.
- Provide a "Buy" button for each mutual fund to allow users to initiate a purchase of units.
- Implement error handling and display meaningful messages to users in case of failures or invalid input.

### Backend (FastAPI)
- Develop a backend API using Python FastAPI.
- Implement a login endpoint that accepts dummy user credentials from an environment file (.env) and generates an access token upon successful authentication.
- Create API endpoints to fetch open-ended schemes for the selected fund family house and integrate with the RapidAPI to fetch mutual fund data.
- Ensure that all API endpoints are authenticated with the access token generated using the dummy user credentials.
- Implement an API endpoint to support the purchase of units for a selected mutual fund.

### Integration with RapidAPI
- Sign up for an account on RapidAPI to obtain the required API key.
- Integrate with the external API specified in the RapidAPI marketplace [latest-mutual-fund-nav](https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav) to fetch mutual fund data based on the selected fund family house.
- Integrate to fetch only the open-ended schemes. The API provides parameters to choose the fund family.

## Documentation
- Provide clear documentation for setting up and running both the frontend and backend applications.
- Include instructions for users to set up the application locally, including how to use the dummy user credentials from the environment file and integrate the RapidAPI key.

## Submission Guidelines
- Create the full-stack web application from scratch, including both frontend and backend components.
- Provide detailed instructions on how to set up and run the frontend and backend applications locally.
