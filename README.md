 <div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101828,50:164E63,100:0891B2&height=220&section=header&text=Python%20Programs%20Collection&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Practical%20Scripts%20%7C%20Mini%20Projects%20%7C%20Automation&descAlignY=62&descSize=15" width="100%" alt="Python Programs Collection Banner">

# 🐍 Python Programs Collection

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=22D3EE&center=true&vCenter=true&width=650&lines=One+Repository%2C+Multiple+Python+Programs;Simple+Utilities+and+Automation;Learning+Python+by+Building+and+Experimenting" alt="Typing SVG">

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Projects-Multiple%20Programs-0891B2?style=for-the-badge">
<img src="https://img.shields.io/badge/Type-Learning%20%26%20Automation-16A34A?style=for-the-badge">

**A collection of Python programs, useful utilities, and automation experiments.**

</div>

---

## 📌 About This Repository

Welcome to **Python Programs Collection**!

This repository contains multiple independent Python programs developed to explore Python programming, solve simple tasks, and experiment with automation.

Each program focuses on a particular functionality and demonstrates the practical use of Python concepts, built-in modules, and programming techniques.

The main objective of this repository is to continuously learn, experiment, develop useful programs, and improve problem-solving skills using Python.

## ✨ Programs Included

| S.No | Program Name | File Name | Description |
|---|---|---|---|
| 01 | 🔐 Password Generator | `Password Generator.py` | Generates random passwords using different character combinations. |
| 02 | 📩 OTP Generator | `Otp.py` | Generates OTPs and demonstrates email-based OTP delivery using SMTP. |
| 03 | 🌐 Browser Automation | `Browser Automation.py` | Automates opening configured URLs in browser tabs. |

> This repository is continuously evolving. More Python programs and utilities will be added over time.

## 🧰 Technologies & Tools

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Random | Random character and OTP generation in the current demos |
| SMTP | Email communication |
| MIME | Email message creation |
| Webbrowser | Browser automation |
| Git & GitHub | Version control and project hosting |
| VS Code / PyCharm | Development environments |


## 📂 Repository Structure

```text
Python-Projects/
│
├── Browser Automation.py
│
├── Otp.py
│
├── Password Generator.py
│
└── README.md
```

Each Python file is a standalone program and can be executed independently.

## ⚙️ Installation & Setup

### Prerequisites

Before running the programs, make sure you have:

- Python 3 installed.
- A code editor such as VS Code or PyCharm.
- Git installed (for cloning the repository).
- Internet connectivity for email and browser-related functionality.

### Step 1: Clone the Repository

```bash
git clone https://github.com/RBharath77/Python-Projects.git
```

### Step 2: Navigate to the Project

```bash
cd Python-Projects
```

### Step 3: Verify Python Installation

```bash
python3 --version
```

### Step 4: Execute Individual Programs

**🔐 Password Generator**

```bash
python3 "Password Generator.py"
```

**📩 OTP Generator**

```bash
python3 Otp.py
```

**🌐 Browser Automation**

```bash
python3 "Browser Automation.py"
```

On Windows, use `python` instead of `python3` if required by your Python installation.

## 🔍 Program Overview

### 1. 🔐 Password Generator

**File:** `Password Generator.py`

The Password Generator is a Python utility designed to create random passwords using different character combinations.

**Features:**

- Generates passwords based on the requested length.
- Supports uppercase letters.
- Supports lowercase letters.
- Includes numeric characters.
- Includes special characters.
- Allows generating another password.

**Concepts Used:**

- Python strings
- Random module
- Loops
- Conditional statements
- User input handling

**Possible Enhancements:**

- Secure password generation using the `secrets` module.
- Password-strength evaluation.
- Custom character selection.
- Copy-to-clipboard functionality.

### 2. 📩 OTP Generator

**File:** `Otp.py`

The OTP Generator demonstrates a simple one-time password generation and email delivery workflow using Python.

**Features:**

- Generates a four-digit OTP.
- Demonstrates email delivery through SMTP.
- Uses an email message format.
- Includes a simulated SMS output in the terminal.

**Concepts Used:**

- Python random module
- SMTP protocol
- Email MIME
- Functions
- Conditional statements
- Exception handling

**Important Security Notes:**

- The current implementation is a learning demonstration, not production-ready authentication.
- The OTP uses the `random` module rather than a cryptographically secure generator.
- The SMS message is simulated through terminal output; an actual SMS provider is not integrated.
- OTP expiry, attempt limits, and server-side verification should be implemented before production use.
- Never upload email passwords, app passwords, or credentials to GitHub.

### 3. 🌐 Browser Automation

**File:** `Browser Automation.py`

Browser Automation demonstrates how Python can interact with the default web browser using its built-in `webbrowser` module.

**Features:**

- Opens a configured URL.
- Automates browser tab opening.
- Reduces repetitive manual browser actions.

**Concepts Used:**

- Python webbrowser module
- Loops
- Variables
- Automation fundamentals

**Possible Enhancements:**

- Open multiple configurable websites.
- Add a user-defined number of browser tabs.
- Create a menu-based browser launcher.
- Add URL validation.

## 📚 Python Concepts Practised

This repository provides practical exposure to the following Python concepts:

- Variables and data types
- Strings and character manipulation
- Conditional statements
- Loops and iterations
- Functions and modules
- Random number generation
- Exception handling
- Standard library usage
- Email communication
- Basic browser automation

## 🔒 Security & Best Practices

- Never commit credentials or sensitive information to a public repository.
- Use Python's `secrets` module for security-sensitive password and OTP generation.
- Store configuration and credentials using environment variables.
- Use OTP expiry and rate limiting in real authentication systems.
- Validate user inputs.
- Test automation scripts using trusted websites.

## 🚀 Future Development Roadmap

This repository will continue to expand with additional Python programs and practical utilities.

- [ ] Advanced Password Generator
- [ ] Password Strength Checker
- [ ] Secure OTP Verification System
- [ ] Email Automation Utility
- [ ] File Management Automation
- [ ] Web Scraping Utilities
- [ ] PDF Automation Tools
- [ ] Image Processing Programs
- [ ] Data Analysis Utilities
- [ ] API Integration Programs
- [ ] GUI-Based Python Applications
- [ ] Additional Automation Projects

## 🤝 Contributing

Contributions, ideas, and improvements are welcome!

To contribute:

1. Fork this repository.
2. Create a new branch.
3. Add your Python program or improve an existing one.
4. Test your changes.
5. Commit your updates.
6. Submit a pull request.

## 🎯 Project Objective

The goal of this repository is to build a growing collection of practical Python programs while improving programming knowledge, logical thinking, automation skills, and software development experience.

**One program at a time. One improvement at a time.**

## 👨‍💻 Author

<div align="center">

### Bharath R

**Python Developer | Software Development Enthusiast**

<a href="https://github.com/RBharath77">
  <img src="https://img.shields.io/badge/GitHub-RBharath77-181717?style=for-the-badge&logo=github">
</a>

</div>

---

<div align="center">

### ⭐ If you find this repository useful, consider giving it a star!

**Thanks for visiting Python Programs Collection!**

<sub>Built with Python • Driven by curiosity • Improved through practice</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101828,50:164E63,100:0891B2&height=110&section=footer" width="100%" alt="Footer Banner">

</div>
