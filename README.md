# LinkedIn Easy Apply Bot

_Automate your LinkedIn job applications with ease!_

This Python and Selenium-based bot automates applying to jobs using the Easy Apply feature on LinkedIn.

## Key Features

- Apply to thousands of jobs effortlessly.
- Track application dates and times for performance analysis.

## Important

- Use at your own risk. LinkedIn may restrict or suspend accounts for bot usage.
- Consider this an educational project.

## Getting Started
# Setting up EASYAPPLYBOT on Windows with VSCode

This guide will walk you through the process of setting up a Python 3.10 project in Visual Studio Code (VSCode) on Windows and installing the required dependencies for the EASYAPPLYBOT GitHub project using the PowerShell terminal.

## Prerequisites

- Python 3.10 installed on your system
- Visual Studio Code (VSCode) installed
- Git installed

## Steps

1. Open VSCode
   
2. Open the Powershell integrated terminal in VSCode by selecting `Terminal` > `New Terminal` from the menu.
   
3. Clone the EasyApplyBot Repository:
   ```powershell
   git clone https://github.com/Valiant-Armory/EasyApplyBot.git
   ```

4. In the terminal, make sure you are in the project folder directory. You can use the `cd` command to navigate to the desired folder. For example:
   ```powershell
   cd EasyApplyBot
   ```
   
5. Create a new Python 3.10 virtual environment by running the following command in the terminal:
   ```powershell
   python -m venv venv
   ```
   This will create a new virtual environment named `venv` in your project folder.

6. Activate the virtual environment by running the following command:
   ```powershell
   .\venv\Scripts\activate
   ```
   You should see `(venv)` appended to your terminal prompt, indicating that the virtual environment is active.

8. Install the required dependencies listed in the `requirements.txt` file by running the following command:
   ```powershell
   pip install -r requirements.txt
   ```
   This will install all the necessary packages for the EASYAPPLYBOT project.

9. Configure the config.yaml file with your desired settings.

10. Once the installation and configuartion is complete, you can run the EASYAPPLYBOT script using the following command:
   ```powershell
   python main.py
   ```
   Or click the play button in the top right corner.

If you encounter any issues during the setup process, please refer to the project's documentation or seek further assistance from the project maintainers.

Conclusion
You have successfully set up a Python 3.10 project in Visual Studio Code on Windows and installed the dependencies required for the EasyApplyBot project using the PowerShell terminal. You can now proceed with using and customizing the EasyApplyBot as per your requirements.

Optionally, watch this video tutorial by [voidbydefault](https://github.com/voidbydefault) during his time maintaining the project, on [YouTube](https://youtu.be/IXflenwJzhQ).

## Troubleshooting

- Try setting an absolute reference for the config file in the main.py if it cant find the config.yaml
- Check for extra spaces, wrong formatting or typos in config if the script isnt launching. Almost all errors I've encoutnered so far are related to syntex errors in the config.

## Additional Resources

- Optional BI dashboard setup: Watch this [YouTube](https://youtu.be/4LH8WTrMCxw) video.
- **Troubleshooting:** Encounter errors? Ensure dependencies are installed.
- **Issues** Raise issues page at my GitHub.

## Support This Project

By supporting this project, you help maintain and improve the bot. Your support is greatly appreciated!

See the sponsor button on the top right of the page or [click here](https://github.com/sponsors/Valiant-Armory).

Also, buy a coffee for [Valiant Armory](https://github.com/Valiant-Armory) through [PayPal][(https://paypal.me/valiantarmory)] for his efforts maintaining and improving this bot!

## Credits
- Expanded Features, Options, Error Handling, Optmization: [Valiant Armory](https://github.com/Valiant-Armory)
- Maintenance and significant updates: [Micheal Dingess](https://github.com/madingess/)
- Improvements and maintenance contributions: [voidbydefault](https://github.com/voidbydefault) with fork [voidbydefault/EasyApplyBot](https://github.com/voidbydefault/EasyApplyBot)
- Original developer: [Nathan Duma](https://github.com/NathanDuma) with [NathanDuma/LinkedIn-Easy-Apply-Bot](https://github.com/NathanDuma/LinkedIn-Easy-Apply-Bot)
