# GhostTrack 👻
### Powerful OSINT Tool for IP, Phone & Username Tracking

GhostTrack is a comprehensive Open Source Intelligence (OSINT) tool designed for **Termux** and Python environments. It provides detailed information gathering capabilities using free, public APIs.

---

## 🎯 Features

✅ **IP Address Tracker**
- Geolocation (Country, City, Region)
- ISP & Organization details
- Latitude & Longitude coordinates
- Google Maps link
- ASN & Border information
- EU compliance status

✅ **Phone Number Tracker**
- Country & region detection
- Carrier information
- Number type (Mobile/Fixed)
- Validation

✅ **Username Tracker**
- Social media presence across 100+ platforms
- Account detection
- Profile URLs

✅ **Reverse IP Lookup**
- Domain information
- Hostname resolution
- Historical data

✅ **Termux Optimized**
- Works perfectly in Termux on Android
- Minimal dependencies
- Terminal UI friendly
- No GUI required

---

## 📋 Requirements

- Python 3.7+
- pip (Python package manager)
- Internet connection

---

## 🚀 Installation

### Option 1: Termux (Android)
```bash
pkg install python
pkg install git
git clone https://github.com/abhinavshiva36-hue/GhostTrack.git
cd GhostTrack
pip install -r requirements.txt
python ghosttrack.py
```

### Option 2: Linux/Mac/Windows
```bash
git clone https://github.com/abhinavshiva36-hue/GhostTrack.git
cd GhostTrack
pip install -r requirements.txt
python ghosttrack.py
```

---

## 📖 Usage

### Main Menu
```
╔═══════════════════════════════════════╗
║         GHOSTTRACK v1.0.0             ║
║    Powerful OSINT Intelligence Tool   ║
╚═══════════════════════════════════════╝

[1] IP Tracker
[2] Phone Number Tracker
[3] Username Tracker
[4] Reverse IP Lookup
[0] Exit

Select option: _
```

---

## 🔌 APIs Used (All Free)

| Feature | API |
|---------|-----|
| IP Geolocation | ip-api.com |
| Phone Number | phonenumberlib |
| Username Search | Sherlock |

---

## 📄 License

MIT License

---

## ⚠️ Disclaimer

Use this tool ONLY for legitimate purposes and respect privacy laws.
