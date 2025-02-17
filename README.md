# ✨ URL Shortener Pro 🔗🚀

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##  Short Description

This is an elegant and feature-rich GUI-based URL Shortener application built with Python and Tkinter. It utilizes the `pyshorteners` library to shorten long URLs using various providers and offers advanced functionalities like QR code generation, URL shortening history, and clipboard integration, all wrapped in a smooth and user-friendly interface.

## ✨ Features

*   **URL Shortening:** Easily shorten long URLs with a clean and intuitive graphical interface.
*   **Provider Selection:** Choose from a list of popular URL shortening services: `dagd`, `clickru`, `isgd`, `osdb`.
*   **Clipboard Integration:** Automatically copy the shortened URL to your clipboard for easy pasting.
*   **QR Code Generation:** Generate QR codes for your shortened URLs for easy sharing on mobile devices.
*   **Shortening History:** Keep track of all your shortened URLs with timestamps, providers, and original URLs. Easily clear the history when needed.
*   **Elegant and Fresh UI:**  A visually appealing and user-friendly interface with a modern look and feel, utilizing `ttk` themes and custom styling.
*   **Status Messages:** Clear and informative status messages to guide you through the shortening process.
*   **Error Handling:** Robust error handling for invalid URLs and issues with shortening services.
*   **URL Validation:** Basic input validation to ensure you enter a valid URL.
*   **"Made with ❤️ by Sufyaan"**:  A personal touch indicating the creator.

## 🖼️ Screenshots & GIF

<!-- You can replace this with actual screenshots or a GIF of your application in action -->

**Home Screen:**
![Screenshot of URL Shortener Home](path/to/your/screenshot-home.png)
*(Replace `path/to/your/screenshot-home.png` with the actual path to your screenshot)*

**Shortened URL & QR Code:**
![Screenshot of Shortened URL and QR Code](path/to/your/screenshot-shortened.png)
*(Replace `path/to/your/screenshot-shortened.png` with the actual path to your screenshot)*

**Shortening History:**
![Screenshot of Shortening History](path/to/your/screenshot-history.png)
*(Replace `path/to/your/screenshot-history.png` with the actual path to your screenshot)*

<!-- If you have a GIF, you can embed it like this: -->
<!--
![URL Shortener Demo GIF](path/to/your/demo.gif)
*(Replace `path/to/your/demo.gif` with the actual path to your GIF)*
-->

**[💡 Tip: Create a GIF using tools like [ScreenToGif](https://www.screentogif.com/) or [LICEcap](https://www.cockos.com/licecap/).  Take screenshots of your application in action and replace the placeholder image paths above with your image/GIF paths.]**

## 🚀 Installation

**Prerequisites:**

*   **Python 3.x:** Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).
*   **pip:** Python package installer (usually included with Python installations).

**Steps:**

1.  **Clone the Repository (if you have one):**
    ```bash
    git clone [YOUR_GITHUB_REPOSITORY_URL]
    cd [REPOSITORY_DIRECTORY_NAME]
    ```
    *(Replace `[YOUR_GITHUB_REPOSITORY_URL]` with your repository URL and `[REPOSITORY_DIRECTORY_NAME]` with your repository folder name, if applicable. If you are just using the Python script directly, skip this step).*

2.  **Install Required Libraries:**
    Open your terminal or command prompt and run the following command to install the necessary Python libraries:
    ```bash
    pip install pyshorteners tkinter pyperclip validators qrcode Pillow
    ```

3.  **Run the Application:**
    Navigate to the directory where you saved the Python script (`elegant_url_shortener.py` or the name you chose) and run it using:
    ```bash
    python elegant_url_shortener.py
    ```

    *(Replace `elegant_url_shortener.py` with the actual name of your Python script file if you named it differently).*

## ⚙️ Usage

1.  **Enter Long URL:** In the "Enter Long URL" field, paste or type the long URL you want to shorten.
2.  **Select Provider:** Choose your preferred URL shortening provider from the "Shortening Provider" dropdown menu (options are `dagd`, `clickru`, `isgd`, `osdb`).
3.  **Click "Shorten URL ➡️":** Press the "Shorten URL ➡️" button to shorten the URL using the selected provider.
4.  **Shortened URL Displayed:** The shortened URL will be displayed in the "Shortened URL" text area. A QR code for the shortened URL will also be generated and shown on the right side.
5.  **Copy to Clipboard:** Click the "Copy to Clipboard 📋" button to copy the shortened URL to your clipboard.
6.  **Clear Input:** Use the "Clear 🗑️" button to clear the input URL and the shortened URL output.
7.  **View History:** The "Shortening History 📜" section at the bottom will display a list of your previously shortened URLs.
8.  **Clear History:** Click "Clear History 🗑️" in the history section to clear the shortening history.

## 🔗 Supported URL Shortening Providers

The application supports the following URL shortening providers, powered by `pyshorteners`:

*   **dagd**
*   **clickru**
*   **isgd**
*   **osdb**

## ✨ Advanced Features

*   **QR Code Generation:** Easily generate QR codes for shortened URLs, perfect for sharing via mobile devices or printed materials.
*   **Shortening History:**  A persistent history of all your URL shortening activities, making it easy to revisit and reuse shortened links.
*   **Elegant UI with `ttk` Themes:**  A visually appealing and modern user interface using `ttk` styling for a smooth and fresh experience.

## 👨‍💻 Made By

Made with ❤️ by **Sufyaan**


<!-- Optional sections - you can add or remove these as needed -->

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please feel free to open an issue or submit a pull request.

## 🙏 Acknowledgments

*   This project utilizes the awesome [pyshorteners](https://pypi.org/project/pyshorteners/) library for URL shortening functionality.
*   Thanks to the [Tkinter](https://docs.python.org/3/library/tkinter.html) library for providing the GUI framework.
*   The [qrcode](https://pypi.org/project/qrcode/) library is used for QR code generation.
*   [Pillow (PIL)](https://pypi.org/project/Pillow/) is used for image handling in Tkinter.
*   [pyperclip](https://pypi.org/project/pyperclip/) for clipboard functionality.
*   [validators](https://pypi.org/project/validators/) for URL validation.

---

**Enjoy shortening your URLs with ✨ URL Shortener Pro! 🔗🚀**
