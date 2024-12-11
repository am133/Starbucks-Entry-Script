# Starbucks Entry Script

This script automates the process of logging into the Starbucks for Life dashboard and submitting the OAMOE form using Selenium. It is designed to be configurable via environment variables for secure and flexible use.

---

## Features
- Logs into the Starbucks for Life dashboard automatically.
- Submits the OAMOE form with configurable personal details.
- Uses Selenium and Chromedriver for browser automation.

---

## Prerequisites
1. **Python**: Ensure Python is installed on your system (version 3.7 or later recommended).
2. **Dependencies**: Install the required Python libraries:
   ```bash
   pip install selenium chromedriver-autoinstaller python-dotenv
   ```
3. **Browser Path**: Update the `brave_path` variable in the script to the path of your local Brave or Chrome installation. For example:
   ```python
   brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
   ```

---

## Setting Up the `.env` File
The script uses a `.env` file to store sensitive information such as your username, password, and form details. Create a `.env` file in the root directory of the project with the following content:

```dotenv
STARBUCKS_USERNAME=your-email@example.com
STARBUCKS_PASSWORD=yourpassword
STARBUCKS_FIRST_NAME=John
STARBUCKS_LAST_NAME=Doe
STARBUCKS_EMAIL=john.doe@example.com
```

Replace the placeholder values with your actual details.

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/am133/Starbucks-Entry-Script.git
   cd Starbucks-Entry-Script
   ```

2. Ensure the `.env` file is created as described above.

3. Run the script:
   ```bash
   python script.py
   ```

---

## Customization
### Browser Path
The script uses `brave_path` to locate the Brave browser. If you are using Chrome, replace the path with the location of `chrome.exe` on your system.

For example:
```python
brave_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

---

## Security Notes
- Do not share your `.env` file publicly or commit it to version control.
- Ensure your `.env` file contains accurate information and is stored securely.

---

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## License
This project is licensed under the MIT License.
