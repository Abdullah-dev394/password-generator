# 🔒 Password Generator

A modern, secure, and responsive password generator built with **Python (Quart)**. Available as both a **Windows Desktop app** (via pywebview) and a **Web app**.

![License](https://img.shields.io/badge/license-Unlicense-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Framework](https://img.shields.io/badge/framework-Quart-green.svg)

---

## 📁 Project Structure

```
password-generator/
├── LICENSE
├── README.md
└── password generator/
    ├── gui/                    # Desktop Application (Windows)
    │   ├── app.py              # Quart backend + pywebview launcher
    │   └── index.html          # Frontend UI (Cyan/Dark theme)
    └── web/                    # Web Application
        ├── app.py              # Quart backend server
        ├── favicon.svg         # Site favicon
        └── index.html          # Frontend UI (Green/Dark theme)
```

---

## ✨ Features

- **Cryptographically Secure**: Uses Python's `secrets` module (CSPRNG) instead of `random` for production-grade security
- **Dual Deployment**: Same codebase runs as both a desktop app and a web server
- **Customizable Options**:
  - Password length: 6–64 characters (slider control)
  - Toggle: Uppercase letters (A–Z)
  - Toggle: Lowercase letters (a–z)
  - Toggle: Digits (0–9)
  - Toggle: Symbols (!@#$%^&* and more)
- **Modern UI**: Dark-themed, responsive design with smooth animations and toast notifications
- **One-Click Copy**: Copy generated passwords to clipboard instantly
- **Input Validation**: Prevents generation when no character sets are selected
- **Cross-Platform Web**: Runs in any modern browser
- **Windows Desktop**: Native-feeling app via pywebview (Edge Chromium engine)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdullah-dev394/password-generator.git
   cd password-generator
   ```

2. Install dependencies:
   ```bash
   pip install quart uvicorn pywebview
   ```

---

## 🖥️ Usage

### Web Application

```bash
cd "password generator/web"
python app.py
```

Then open your browser to: `http://127.0.0.1:36048`

### Desktop Application (Windows)

```bash
cd "password generator/gui"
python app.py
```

A native window will open automatically — no browser needed.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Quart (async web framework) |
| Server | Uvicorn (ASGI) |
| Desktop Shell | pywebview (Edge Chromium) |
| Frontend | Vanilla HTML5, CSS3, JavaScript |
| Security | Python `secrets` module (CSPRNG) |
| Styling | CSS Custom Properties (variables), Flexbox |

---

## 🔐 Security Notes

- **Never uses `random`**: The `secrets` module provides cryptographically strong random numbers suitable for managing passwords, tokens, and secrets.
- **No data persistence**: Passwords are generated on-the-fly and never stored server-side.
- **Local-only desktop mode**: The GUI version runs entirely locally — no network exposure.

---

## 📝 API Reference

### `POST /api/generate`

Generates a random password based on provided criteria.

**Request Body (JSON):**
```json
{
  "password_length": 16,
  "upper": true,
  "lower": true,
  "digit": false,
  "symbol": false
}
```

**Response (JSON):**
```json
{
  "password": "xK9mPqRtLvNwZfBj"
}
```

**Error Response:**
```json
{
  "error": "Please select at least one option!"
}
```

---

## 📸 Screenshots

| Web App (Green Theme) | Desktop App (Cyan Theme) |
|----------------------|-------------------------|
| Azerbaijani UI with green accents | English UI with cyan accents |
| Browser-based, responsive | Native Windows window |

---

## 📄 License

This project is released into the **public domain** under the [Unlicense](https://unlicense.org). You are free to use, modify, distribute, or sell it without any restrictions.

---

##  Author

**Abdullah-dev394**

Feel free to ⭐ star the repo if you find it useful!
