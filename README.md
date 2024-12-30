# 🚀 PRODIGY_CS_04

## 📝 Task Overview

  **Task:** Create a Basic Keylogger Program
  
  **Description:** Develop a keylogger program that records and logs keystrokes. The project emphasizes ethical considerations, requiring explicit permission from the system owner.

  **Status:** ✅ Completed

---

## 🌟 Features

### 🔑 Comprehensive Keylogging Options
- **Customizable Logging:** Users can select specific types of keys to log:
  - **Characters:** Logs alphabetic keys (A-Z, a-z).
  - **Numbers:** Logs numeric keys (0-9).
  - **Special Characters:** Logs symbols (e.g., @, #, $, &, etc).
  - **Function Keys:** Logs function keys (F1-F12).

### 🔒 Ethical Use
- **Consent Prompt:** Displays a consent message requiring explicit user agreement before starting the keylogger.
- **Educational Use Only:** Clear disclaimers in the GUI to ensure responsible usage.

### 📂 Log Management
- Logs are saved in a file named `keylogged.txt` in the current working directory.
- Error handling ensures logs are securely written to the file.

### 🖥️ User-Friendly GUI
- Built using **Tkinter**, featuring:
  - **Checkbuttons:** Allow users to select desired key types for logging.
  - **Start/Stop Buttons:** Begin or end the logging session.
  - **Hide Window Option:** Temporarily hides the GUI.
  - **Dynamic Labels:** Show the current log file path.

### 🎹 Global Hotkey Support
- **Show Window:** `Ctrl + Shift + H` brings the GUI back.
- **Stop Keylogger:** `Ctrl + Shift + T` stops the keylogger and exits.

---

## 📦 Dependencies
The following Python modules are required:
- `tkinter`: For building the GUI.
- `pynput`: For capturing and handling keyboard events.

Install them using:
```bash
pip install pynput
```
(Note: `tkinter` is pre-installed with Python on most systems. For Linux, install it using: `sudo apt-get install python3-tk`.)

---

## 📥 Installation Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/idPriyanshu/PRODIGY_CS_04.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd PRODIGY_CS_04
   ```

3. **Run the Program:**
   ```bash
   python keylogger.py
   ```

---

## ▶️ Usage Instructions

1. **Launch the Program:** Run the `keylogger.py` script.
2. **Select Key Types:** Use the checkboxes to specify which types of keys to log.
3. **Start Logging:** Click the `Start` button and consent to begin keylogging.
4. **Stop Logging:** Click the `Stop` button to end logging and save logs to the file.
5. **Hide/Show Window:** Use the `Hide` button to hide the GUI and `Ctrl + Shift + H` to show it again.

---

## 🔒 Ethical Considerations
- **Permission Required:** This tool is intended for educational purposes only and requires explicit consent from the system owner.
- **Disclaimer:** Misuse of this tool is strictly prohibited and may violate privacy laws.

---

## 📜 How It Works

1. **Keyboard Event Listener:**
   - Captures keypress events using `pynput`.
   - Filters keys based on user-selected options (characters, numbers, etc.).

2. **Log Management:**
   - Logs are appended to a file (`keylogged.txt`).
   - Handles file writing errors gracefully.

3. **Global Hotkeys:**
   - `Ctrl + Shift + H` shows the GUI.
   - `Ctrl + Shift + T` stops logging and exits the program.

---

## 📂 Repository Structure
```
PRODIGY_CS_04/
├── keylogger.py         # Main Python script
├── README.md            # Documentation file
```

---

## 🛠️ Challenges & Solutions

1. **Consent Enforcement:**
   - **Challenge:** Ensure the program operates ethically.
   - **Solution:** Added a consent dialog requiring user approval before starting.

2. **Selective Logging:**
   - **Challenge:** Allow users to customize key types to log.
   - **Solution:** Implemented checkboxes for dynamic selection.

3. **Global Hotkey Management:**
   - **Challenge:** Enable GUI toggling without interfering with logging.
   - **Solution:** Integrated `pynput.GlobalHotKeys` for efficient hotkey handling.

---

## 🌟Future Improvements

1. **Enhanced Logging:**
   - Detect and log mouse events or clipboard content.

2. **Encrypted Logs:**
   - Encrypt log files for added security.

3. **Advanced GUI:**
   - Add more themes and customization options.

4. **Cross-Platform Optimization:**
   - Ensure seamless operation on Windows, macOS, and Linux.

---
## 📜 License
This project is distributed under a custom **Educational Use License**.  

### 🔒 Terms of Use:
- This software is provided "as is" for educational and research purposes only.  
- You are prohibited from using this software for illegal or unethical activities.  
- The author disclaims all warranties and is not liable for any misuse or resulting damages.  

For full terms, please refer to the [`LICENSE`](LICENSE) file in the repository.
---

## 🏆 Credits
**Developer:** [@idPriyanshu](https://www.github.com/idPriyanshu)  
**Mentorship:** Prodigy InfoTech Cyber Security Internship Program

---

## 📧 Contact
For queries or suggestions, email: [iiit.Priyanshu@gmail.com](mailto:iiit.priyanshu@gmail.com)

