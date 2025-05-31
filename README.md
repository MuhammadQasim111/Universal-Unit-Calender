

# 🌍 Universal Unit Converter

A clean, intuitive, and powerful **unit converter web app** built using [Streamlit](https://streamlit.io/). Easily convert values across multiple categories such as **Length**, **Mass**, **Temperature**, **Volume**, **Digital Storage**, **Time**, and **Speed** — all in one place.

Made with ❤️ by **Muhammad Qasim**.

---

## 🚀 Features

* ✅ **Real-time unit conversion**
* 📁 Categories supported:

  * Length (meter, kilometer, mile, inch, etc.)
  * Mass (gram, kilogram, pound, etc.)
  * Temperature (Celsius, Fahrenheit, Kelvin)
  * Volume (liter, gallon, cubic meter, etc.)
  * Digital Storage (bit, byte, kilobyte, megabyte, etc.)
  * Time (second, hour, week, etc.)
  * Speed (meter/second, mile/hour, knot, etc.)
* 🧠 **Smart conversion logic** using base units
* 📜 **Conversion history** tracking
* 📋 One-click **"Copy Result to Clipboard"** button
* 💡 Temperature handled with **non-linear conversion** formulas
* 🔒 Error-handling for invalid conversions

---

## 🖥️ Live Demo

> You can deploy it locally or use platforms like [Streamlit Cloud](https://share.streamlit.io) to host it online.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/unit-converter.git
cd unit-converter
```

### 2. Install required packages

Make sure you have Python 3.7 or above.

```bash
pip install -r requirements.txt
```

> Or manually install Streamlit:

```bash
pip install streamlit
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

This will launch the app in your default web browser.

---

## 📂 Project Structure

```text
.
├── app.py               # Main Streamlit app file
├── README.md            # Project documentation
└── requirements.txt     # List of Python dependencies
```

---

## 📌 Technologies Used

* [Python 3](https://www.python.org/)
* [Streamlit](https://streamlit.io/)

---

## 🧠 How It Works

* Each **unit category** (e.g., Length, Mass) has a **base unit** for internal consistency.
* Conversions follow the pattern:

  ```
  input → base unit → desired unit
  ```
* **Temperature conversions** are handled with custom formulas due to non-linear relationships.
* All conversions are stored in **session history** (in-browser) and can be cleared anytime.

---

## ✨ Future Improvements

* Add currency conversion using real-time APIs
* Include more units (e.g., pressure, energy)
* Dark mode and responsive design
* Export history as CSV

---

## 🙌 Author

**Muhammad Qasim**
Connect with me on [LinkedIn](https://www.linkedin.com/in/muhammad-qasim-a99057265?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
Email: `mqasim111786111@gmaiol.com`

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


