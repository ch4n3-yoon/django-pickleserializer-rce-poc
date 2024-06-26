# django-pickleserializer-rce-poc

## Description
This repository provides a Proof of Concept (PoC) for demonstrating the Remote Code Execution (RCE) vulnerability found in Django's `PickleSerializer`, which was present up to version 4.0. The goal of this repository is to educate developers and security professionals about this vulnerability, its implications, and how to mitigate it.

## Vulnerability Overview
Django's `PickleSerializer` was vulnerable to RCE due to its unsafe deserialization of user-controlled data if `SECRET_KEY` leaked. This PoC showcases how an attacker could exploit this vulnerability to execute arbitrary code on the server.

## Contents
- **PoC Code**: Sample Django project with vulnerable configurations.
- **Exploitation Steps**: Detailed instructions on how to exploit the vulnerability.
- **Mitigation**: Guidelines on how to secure Django applications against this type of vulnerability.

## Requirements
- Python 3.x
- Django <= 4.0

## Usage
1. Clone the repository:
    ```sh
    git clone https://github.com/ch4n3-yoon/django-pickleserializer-rce-poc.git
    cd django-pickleserializer-rce-poc
    ```

2. Set up the virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django server:
    ```sh
    python manage.py runserver 0.0.0.0:8000
    ```

5. Run the exploit code:
    ```sh
    python exploit.py http://localhost:8000 id
    ```

## Disclaimer
This project is for educational purposes only. Use this information to understand and fix the vulnerability in your own applications. Do not use this information for malicious purposes.

