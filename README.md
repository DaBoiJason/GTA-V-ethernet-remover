# Ethernet Controller Script for GTA V heists

## Overview

This Python script provides a simple command-line interface to control the state of the Ethernet connection on a Windows system. It allows you to disable the Ethernet connection by pressing F2, enable it again by pressing F1, and terminate the script using F3.
## Features

### Binds

- Enable Ethernet connection: Press F1.
- Disable Ethernet connection: Press F2.
- Terminate the script: Press F3.
- The script is intended for windows 10 and 11 use, I am working on an alternative for LinuxOS.
## Required dependancies/conditions

Before running the script, ensure you have the following:

- Python 3.x installed on your system.
- The `keyboard` module. Install it using the following command:
  
  ```bash
  pip install keyboard
  ```
## GTA V implication
1. Finish the Heist

2. Press F2 to disable the Ethernet connection on the very frame that you get the color change from the Heist passed message.

3. Wait till you get the save Error message from rockstar games on the bottom left.

4. Once it takes you back to offline mode, press F1 to enable it again.

5. Press Home and reconnect on socialclub and then join online

6. Press F3 to terminate the script whenever you want.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ethernet-controller-script.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ethernet-controller-script
   ```

3. Run the script:
   ```bash
   python ethernet_controller.py
   ```
   ```bash
   Or
   ```
   ```bash
   just run the py script with double click
   ```

4. Press F2 to disable the Ethernet connection on the very frame that you get the color change from the Heist passed message, F1 to enable it again, and F3 to terminate the script.
## License

This project is licensed under the [MIT License](LICENSE.md).