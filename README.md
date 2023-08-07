# Auto-Email-Generation

Auto Email Generation is a project that utilizes FastAPI for the backend and a React frontend to automatically generate emails based on user input using the OpenAI API.

## Setup and Usage

### Setting Up Environments

1. **Node.js Environment (Frontend):**
    - Make sure you have Node.js and npm (Node Package Manager) installed on your system.
    - You can download Node.js from the official website: [nodejs.org](https://nodejs.org/)
    - To install frontend packages run the below command:
        ```bash
        npm ci
        ```

2. **Python Environment (Backend):**
    - It's recommended to use a virtual environment for Python to manage dependencies.
    - Create a virtual environment in the `backend` directory:
      ```bash
      cd backend
      python -m venv email_gen
      ```
    - Activate the virtual environment:
      - On Windows:
        ```bash
        email_gen\Scripts\activate
        ```
      - On macOS and Linux:
        ```bash
        source email_gen/bin/activate
        ```
    - Install the required Python packages:
      ```bash
      pip install -r requirements.txt
      ```

### Running Locally

1. **Start FastAPI Server (Backend):**
    ```bash
    cd backend
    uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
    ```
   This command starts the FastAPI server on `http://127.0.0.1:8000`.

2. **Start Frontend Server:**
    ```bash
    cd frontend
    npm start
    ```
   In a separate terminal, run this command to start the React frontend server. This will typically start on `http://localhost:3000`.

### Local Testing of Lambda Function

1. **Test Lambda Function:**
    Use `python-lambda-local` to test your Lambda function locally. Run the following command:
    ```bash
    cd backend
    python-lambda-local -f handler app/main.py ../test-events-lambda/events.json
    ```

## Additional Notes

- Setting up the environment variables
    1. Navigate to the root directory of your project.
    2. Create a new file named `.env` in the root directory.

    Inside the `.env` file, add the following lines with your actual values for the environment variables:

    ```dotenv
    OPENAI_ORGANIZATION=your-organization-id
    OPENAI_API_KEY=your-api-key
    ```

    Replace `your-organization-id` with your actual OpenAI organization ID and `your-api-key` with your actual OpenAI API key.

    Make sure not to include any quotes around the values. The `.env` file is used to store sensitive information, so keep it private and do not share it publicly.

- Further Configuration:
    Adjust any other configurations as necessary in the respective files and directories.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** This README provides a basic setup guide. Additional setup and configuration might be needed depending on your environment and requirements.
