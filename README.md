<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101828,50:164E63,100:0891B2&height=210&section=header&text=Python%20Programs%20Collection&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Practical%20Scripts%20%7C%20Mini%20Projects%20%7C%20Automation&descAlignY=62&descSize=15" width="100%" alt="Python Programs Collection banner"/>🐍 Python Programs Collection
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=22D3EE&center=true&vCenter=true&width=650&lines=One+repository%2C+multiple+Python+programs;Simple+utilities+and+automation+experiments;Learning+Python+by+building+and+practising" alt="Animated typing text"/>



A growing collection of standalone Python programs, utilities, and experiments.
</div>📌 About the Repository
This repository brings multiple small Python programs together in one place. Each script focuses on a specific task, making the collection useful for practising Python fundamentals, exploring standard-library modules, and learning how small automation utilities work.

The programs are independent: you can open, understand, and run each script separately. New scripts can be added as the collection grows.
✨ Programs Included
Program	File	What it does
🔐 Password Generator	Password Generator.py	Generates a random password using letters, digits, and special characters.
📩 Email OTP Demo	Otp.py	Generates a four-digit OTP and demonstrates sending it by email through SMTP. The SMS message is currently printed in the terminal.
🌐 Browser Tab Opener	test.py	Opens the configured image URL in multiple new browser tabs.


Note: These are small standalone learning programs, not one integrated application. The program list above reflects the Python files currently included in this repository.

🧰 Built With
Technology / Module	Purpose
Python 3	Main programming language
random	Random character selection and demo OTP generation
smtplib	Connecting to an SMTP email server
email.mime.text	Creating the email message body
webbrowser	Opening a URL in the default browser

<img width="338" height="145" alt="Screenshot 2026-11-02 at 10 26 03 AM" src="https://github.com/user-attachments/assets/84931bea-57ab-4fe2-ac0c-6e32119e7083" />

The current scripts use Python's standard library, so no third-party packages are required.

As more programs are added, place each .py file in this folder and update the Programs Included table with its purpose and run command.
⚙️ Getting Started
Requirements
- Python 3 installed on your computer.
- A terminal or command prompt.
- An internet connection for the email and browser examples.
Check your Python version:
python3 --version
Clone the Repository
Replace the URL with your repository's actual GitHub URL:
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
Run an Individual Program
Run only the script you want to use:

Password Generator
python3 "Password Generator.py"
Email OTP Demo
python3 Otp.py
Browser Tab Opener
python3 test.py
On Windows, use python instead of python3 if that is how Python is configured on your system.
🔍 Program Details
<details>
<summary><strong>🔐 Password Generator</strong></summary>File: Password Generator.py

Generates a password of a length entered by the user. The character pool contains lowercase letters, uppercase letters, digits, and special characters.

How it works:
1. Enter the required password length.
2. The script selects characters from the combined character pool.
3. It displays the generated password.
4. The script asks whether you want to finish or generate another password.
Current implementation note: The script uses Python's random module. It is suitable as a basic programming exercise, but it should use the secrets module before being used to generate real account passwords.
</details><details>
<summary><strong>📩 Email OTP Demo</strong></summary>
File: Otp.py

Demonstrates generating a four-digit one-time password and sending it to an email address through Gmail SMTP.

Before running:
1. Configure SENDER with the sender email address.
2. Configure PASSWORD with an app password; do not use or publish your normal account password.
3. Replace the sample recipient email and phone number.
4. Run the script and check the terminal for the email sending result.
Current implementation notes:
- The SMS OTP is printed in the terminal; no SMS provider is connected.
- The OTP is generated with random, has no expiry, and has no attempt limit.
- This is a learning demonstration, not a production authentication system.
- Never commit real email credentials to a public repository. Prefer environment variables or a secrets manager.
</details><details>
<summary><strong>🌐 Browser Tab Opener</strong></summary>File: test.py

Uses Python's built-in webbrowser module to open the URL configured in the script.

How it works:
1. Set the target URL in the url variable.
2. Run the script.
3. The loop opens that URL in 30 new browser tabs.
Tip: Change the loop count to a small number before testing. Opening 30 tabs at once can clutter your browser.
</details>🛡️ Safety & Good Practices
- Do not upload passwords, API keys, SMTP credentials, or personal data to GitHub.
- Use secrets, not random, for security-sensitive password or token generation.
- Add OTP expiry, verification, and rate limiting before building a real authentication workflow.
- Test browser automation with trusted URLs and a small number of tabs.
- Validate user input before using it in a larger application.
🗺️ Future Improvements
- [ ] Add a simple menu to select and launch programs.
- [ ] Improve password generation with secrets and configurable character rules.
- [ ] Add password-strength feedback.
- [ ] Add OTP expiry and limited verification attempts.
- [ ] Move email settings into environment variables.
- [ ] Integrate an SMS provider for actual SMS delivery.
- [ ] Add input validation and tests for each script.
- [ ] Add new Python programs to the collection and document them here.
🤝 Contributing
This is a growing learning collection. To add a program:
1. Create a separate, clearly named .py file.
2. Keep the program focused on one task.
3. Add usage instructions and any required dependencies.
4. Update the Programs Included table and project structure.
5. Test the script before committing your changes.
👨‍💻 Author
Bharath R


<div align="center">⭐ Thanks for visiting this Python programs collection!

Built to practise, experiment, and keep improving with Python.
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101828,50:164E63,100:0891B2&height=100&section=footer" width="100%" alt="Footer banner"/></div>
