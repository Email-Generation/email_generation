# Auto-Email-Generation

Auto Email Generation is a project that utilizes FastAPI for the backend and a React frontend to automatically generate emails based on user input using the OpenAI API.

## Table of Contents
- [Directory Structure](#directory-structure)
- [Setup and Usage](#setup-and-usage)
  - [Setting Up Environments](#setting-up-environments)
  - [Creating .env File](#creating-env-file)
  - [Running Locally](#running-locally)
  - [Local Testing of Lambda Function](#local-testing-of-lambda-function)
- [Deployment](#deployment)
  - [Docker Compose](#docker-compose)
  - [Build Lambda Docker Image](#build-lambda-docker-image)
- [Contributing Guidelines](#contributing-guidelines)
- [License](#license)

## Directory Structure

| Directory               | Purpose                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------|
| Root                    | Essential project files and configurations (e.g., .env, docker-compose.yml, README.md)   |
| .github                 | GitHub workflow configurations for automated tasks (e.g., testing, deployment)         |
| .vscode                 | Visual Studio Code IDE settings and configurations                                   |
| backend                 | Backend service code, configurations, and dependencies                                |
|                         | Organized structure with folders for different components (config, models, routes)    |
| frontend                | Frontend service's React application code                                              |
|                         | Organized in a typical React project structure (public, src)                           |
| test-events-lambda      | Test event data for local Lambda function testing                                      |

## Setup and Usage

### Setting Up Environments

1. **Node.js Environment (Frontend):**
    - Make sure you have Node.js and npm (Node Package Manager) installed on your system.
    - You can download Node.js from the official website: [nodejs.org](https://nodejs.org/)
    - To install frontend packages run the below command:
        ```bash
        cd frontend
        npm ci
        ```

2. **Python Environment (Backend):**

   > It's recommended to use a virtual environment for Python to manage dependencies.

   A. _Using `venv`_
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
   ### OR

   B. _Using Conda_

      To set up a Conda environment using a requirements file, you can follow these steps:

      1. Create a Conda Environment:
         Open your terminal and run the following command to create a new Conda environment (replace `myenv` with the desired environment name):

         ```bash
         conda create --name email_gen
         ```

      2. Activate the Environment:
         Activate the newly created environment using the following command:

         ```bash
         conda activate email_gen
         ```

      3. Install Packages from a Requirements File:
         You can use the `conda install` command to install packages from a requirements file. If your requirements file is named `requirements.txt`, run the following command:

         ```bash
         conda install --file requirements.txt
         ```

         Replace `requirements.txt` with the actual path to your requirements file if it's located in a different directory.

      4. Verify Installed Packages:
         After installing the packages, you can use the `conda list` command to verify that the required packages have been installed:

         ```bash
         conda list
         ```

      5. Deactivate the Environment:
         When you're done working in the environment, you can deactivate it using the following command:

         ```bash
         conda deactivate
         ```

### Creating .env File

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
    python-lambda-local -f handler app/main.py ../test-events-lambda/test_event.json
    ```

## Deployment

### Docker Compose

1. **Build/Start Containers**:
   - Open a terminal in your project's root directory.
   - Run the following command to build and start the containers defined in the `docker-compose.yml` file:
     ```bash
     docker-compose up
     ```
   - To build image and container from scratch, use the following command:
      ``` bash
      docker-compose up --build
      ```
   - This command will start both the backend and frontend containers, pulling necessary images if they don't exist locally.

2. **Access Frontend and Backend**:
   - Once the containers are up and running, you can access the frontend by opening your browser and navigating to `http://localhost:3000`.
   - The backend's FastAPI server will be accessible at `http://localhost:8000`.

3. **Modify Code**:
   - Make changes to your frontend or backend code as needed.
   - Docker Compose will automatically reload the containers when changes are detected in the project directories mapped into the containers.

4. **Stop Containers**:
   - When you're finished, you can stop the containers by pressing `Ctrl+C` in the terminal where `docker-compose up` is running.

5. **Cleaning Up**:
   - To stop and remove the containers, as well as their associated networks and volumes, run:
     ```bash
     docker-compose down --rmi all
     ```
### Build Lambda Docker Image

1. **Login to Amazon ECR Registry**:

   Use this command to authenticate Docker to your Amazon Elastic Container Registry (ECR) account for the specified region. Replace `<account-id>` and `<region>` with your actual account ID and region.

   ```bash
   aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com/email-gen-lambda:latest
   ```

   This command fetches an authentication token and logs Docker into your ECR registry.

2. **Get AWS Account Identity**:

   Use this command to verify the AWS account identity you're currently using.

   ```bash
   aws sts get-caller-identity
   ```

   This command provides information about your AWS account, such as the account ID, user ID, and ARN.

3. **Build Docker Image for Lambda**:

   Navigate to the `backend` directory and build the Docker image for your Lambda function using the specified Dockerfile.

   ```bash
   cd backend
   docker build -t email-gen-lambda ./ -f ./Dockerfile.lambda.dev
   ```

   This command builds the Docker image based on the specified Dockerfile (`Dockerfile.lambda.dev`) in the `backend` directory.

4. **Tag Docker Image**:

   After building the Docker image, tag it with the ECR repository's URI.

   ```bash
   docker tag email-gen-lambda:latest <account-id>.dkr.ecr.<region>.amazonaws.com/email-gen-lambda:latest
   ```

   This command assigns a new tag to the Docker image, indicating the ECR repository location.

5. **Push Docker Image to ECR**:

   Push the tagged Docker image to your ECR repository.

   ```bash
   docker push <account-id>.dkr.ecr.<region>.amazonaws.com/email-gen-lambda:latest
   ```

   This command uploads the Docker image to your ECR repository for future use.

## Contributing Guidelines

Welcome to our project! We appreciate your interest in contributing. By following these guidelines, you can help us maintain a productive and collaborative development environment. Please take a moment to review the guidelines before getting started.

### Getting Started

1. **Fork the Repository**: Start by forking this repository to your GitHub account. This will create a copy of the project under your account that you can work on.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/email-generation.git
   ```

3. **Create a New Branch**: Before making any changes, create a new branch for your feature, bug fix, or improvement. Use a descriptive and relevant name for your branch.
   ```
   git checkout -b feature/new-feature
   ```

### Making Changes

1. **Coding Standards**: Follow the existing coding style and standards used in the project. This includes formatting, naming conventions, and code organization.

2. **Testing**: Ensure that your code changes do not break existing tests, and if applicable, write new tests to cover the changes you've made.

3. **Documentation**: Update the project's documentation to reflect any changes you've made. This includes README files, code comments, and docstrings.

### Submitting Changes

1. **Commit Changes**: Once your changes are ready, commit them with clear and concise commit messages. Use the present tense and provide context for the change.
   ```
   git commit -m "Add new feature: XYZ"
   ```

2. **Push to Your Fork**: Push the changes to your forked repository on GitHub.
   ```
   git push origin feature/new-feature
   ```

3. **Create a Pull Request (PR)**: Open a pull request from your branch to the main repository's `main` branch. Provide a detailed description of the changes, why they are necessary, and any relevant information.

### Code Review

1. **Review Process**: Your pull request will be reviewed by project maintainers. Be prepared for feedback and possible discussions about your changes.

2. **Addressing Feedback**: If changes are requested, address them by making additional commits. Keep the pull request updated with the latest changes.

3. **Merge Approval**: Once the changes are approved by a maintainer, your pull request will be merged into the main repository.

### Notes

- Respect the project's code of conduct and community guidelines at all times.
- Be patient and respectful when interacting with other contributors and maintainers.
- Happy coding and thank you for contributing to our project!

## License

This project is licensed under the `BSD 3-Clause` License. See the [LICENSE](LICENSE) file for details.

---

**Note:** This README provides a basic setup guide. Additional setup and configuration might be needed depending on your environment and requirements.
