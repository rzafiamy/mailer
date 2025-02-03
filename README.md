# Mailer

## Overview
Mailed is a Python-based application designed to send emails securely using SMTP with SSL/TLS encryption. It leverages the `smtplib` library for sending emails and `argparse` for command-line argument parsing. The application is configured using environment variables stored in a `.env` file and a `config.py` file for easy management of email settings.

## Features
- **Secure Email Sending**: Uses SSL/TLS encryption to secure email communications.
- **Command-Line Interface**: Supports command-line arguments for flexible email sending.
- **Configuration Management**: Uses environment variables and configuration files for easy setup and management.
- **Customizable**: Allows customization of sender, recipient, subject, and body of the email.
- **Error Handling**: Provides detailed error messages for troubleshooting.

## Installation
To install and set up the Mailer application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rzafiamy/mailer.git
   cd mailer
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**:

   Create a `.env` file (copy the .env.example file provided) in the project directory with the following content:

   ```plaintext
   SENDER_EMAIL=your_email@example.com
   SENDER_PASSWORD=your_password
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=465
   ```

## Usage
To send an email using the Mailer application, use the following command-line arguments:

- **Sender Email**: (Optional) The email address of the sender. Defaults to the value in the `.env` file.
- **Recipient Email**: The email address of the recipient.
- **Subject**: The subject of the email.
- **Body**: The body of the email.

### Examples
- **Send an Email with Default Sender**:
  ```bash
  python send_email.py --recipient recipient@example.com --subject "Test Email" --body "This is a test email."
  ```

- **Send an Email with Custom Sender**:
  ```bash
  python send_email.py --sender custom_sender@example.com --recipient recipient@example.com --subject "Test Email" --body "This is a test email."
  ```

## Configuration
The Mailer application is configured using environment variables stored in a `.env` file and a `config.py` file. Here is how to configure the application:

1. **Environment Variables**:
   - `SENDER_EMAIL`: The email address of the sender.
   - `SENDER_PASSWORD`: The password for the sender's email account.
   - `SMTP_SERVER`: The SMTP server address (e.g., `smtp.gmail.com`).
   - `SMTP_PORT`: The port number for the SMTP server (e.g., `465` for SSL).

2. **Configuration File**:
   The `config.py` file loads the environment variables and provides them to the `send_email.py` script.

## Contributing
Contributions to the Mailer application are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact