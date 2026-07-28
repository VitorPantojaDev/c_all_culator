# 🧮 C-All-Culator

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Application-FF4B4B)
![Project Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)

A multifunctional calculator developed with **Python** and **Streamlit**. The application brings together mathematical, educational, medication dosage, and personal finance calculators in a single interface.

The project is available in **English** and **Brazilian Portuguese**.

## 🔗 Live application

[Open C-All-Culator on Streamlit](https://c-all-culator.streamlit.app/)

## 📑 Table of contents

- [Features](#-features)
- [Languages](#-languages)
- [Technologies](#-technologies)
- [Project structure](#-project-structure)
- [Requirements](#-requirements)
- [Running locally](#-running-locally)
- [How to use](#-how-to-use)
- [Important notice](#%EF%B8%8F-important-notice)
- [Project status](#-project-status)
- [Author](#-author)

## ✨ Features

| Category | Calculator | Description |
|---|---|---|
| Mathematics | Basic Math | Performs addition, subtraction, multiplication, and division. |
| Education | Golden Material | Represents addition and subtraction visually using base-ten blocks inspired by Golden Beads teaching materials. |
| Mathematics | Scientific | Calculates percentages, square roots, squares, and cubes. |
| Health | Medication Dosage | Calculates the medication volume based on patient weight, prescribed dosage in `mg/kg`, and medication concentration. |
| Finance | Monthly Expenses | Calculates the monthly balance by comparing income with expenses entered directly or separated by category. |
| Finance | Financial Runway | Estimates how many months the available savings can support recurring withdrawals, deposits, and investment yield. |
| Finance | Savings Goal | Estimates how long it will take to reach a financial reserve goal based on monthly deposits and investment yield. |

## 🌐 Languages

The application provides two language versions:

- 🇺🇸 **English:** `main.py`
- 🇧🇷 **Brazilian Portuguese:** `pages/main_br.py`

The language can be changed using the button displayed at the top of the application.

## 🛠 Technologies

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## 📁 Project structure

```text
c_all_culator/
├── main.py                   # English version and application entry point
├── pages/
│   └── main_br.py            # Brazilian Portuguese version
├── .streamlit/
│   └── config.toml           # Streamlit theme configuration
├── requirements.txt          # Project dependencies
├── CNAME                     # Custom domain configuration
└── README.md                  # Project documentation
```

## ✅ Requirements

Before running the application, make sure the following tools are installed:

- Python `3.9` or newer
- `pip`
- Git

## 🚀 Running locally

### 1. Clone the repository

```bash
git clone https://github.com/VitorPantojaDev/c_all_culator.git
cd c_all_culator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux or macOS:**

```bash
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run main.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## 🧭 How to use

1. Open the application in your browser.
2. Select a calculator from the sidebar.
3. Enter the requested values.
4. Review the calculated result.
5. Use the language button at the top of the page to switch between English and Brazilian Portuguese.

## ⚠️ Important notice

The medication dosage calculator is intended for **educational and support purposes only**. Its results do not replace evaluation, prescription, or verification by a qualified healthcare or veterinary professional.

Always confirm the entered values, measurement units, medication concentration, and prescribed dosage before using the result.

## 🚧 Project status

This is a personal project under active development, created to practice and demonstrate skills with **Python** and **Streamlit**.

Some features, especially the financial calculators, may still receive calculation, validation, and interface improvements.

## 👤 Author

**Vitor A. Pantoja**

- Email: [vitorpantoja.dev@gmail.com](mailto:vitorpantoja.dev@gmail.com)
- GitHub: [VitorPantojaDev](https://github.com/VitorPantojaDev)
- Linkedin: [Vitor Pantoja](https://www.linkedin.com/in/vitorapantoja/)

---

Developed with Python and Streamlit.
