# File Size Monitoring and Management Tool (Python)

## Overview

This Python project is designed to **simulate and manage file growth** over time by appending and removing random data at controlled intervals.  
It **monitors the file size** in real-time and **automatically reduces** the file content when a defined threshold is reached.  
Additionally, it **logs all critical events** to a log file and **sends an email alert** when the file size crosses the specified limit.

The tool uses **multi-threading** to handle concurrent file manipulation and size checking independently.

---

## ✨ Features

- **Multithreaded Design**:
  - One thread appends random bits to a file periodically.
  - One thread removes bits from the beginning of the file periodically.
  - One thread monitors the file size continuously.
  
- **File Growth Simulation**:
  - Random data is appended in small chunks to mimic real-world file growth.

- **Size Threshold Management**:
  - When the file size exceeds a specified limit (e.g., 20 KB), the file is automatically trimmed to a reduced size (e.g., 10 KB).

- **Logging**:
  - Each file size exceedance event is logged with a timestamp, append count, and remove count.

- **Email Notifications**:
  - When the threshold is reached, an email alert is sent to the configured recipient (requires an SMTP server).

---

## 🛠 Technologies Used

- **Python Standard Libraries**:
  - `threading`
  - `smtplib`
  - `email.mime.text`
  - `random`
  - `time`
  - `os`
  - `fractions`

---

## ⚙️ Configuration

You can customize the following parameters inside the script:

- `FileName` — The target file to manipulate (`out.bin` by default).
- `LogName` — Log file for recording events (`log.txt`).
- `RequiredAppendTime` — Interval (seconds) to append random bits (default: 10 seconds).
- `RequiredRemoveTime` — Interval (seconds) to remove random bits (default: 20 seconds).
- `RequiredFileCheckSize` — Maximum file size before action is taken (default: 19,999 bytes).
- `RequiredReduceSize` — File size to reduce to after exceeding threshold (default: 10,000 bytes).

---

## 🛡 Requirements

- Python 3.x
- Local SMTP server (or modify SMTP settings to use external email services like Gmail)

---

## 📋 How It Works

1. The appending thread writes random binary characters (`0` or `1`) to the file every 10 seconds.
2. The removing thread deletes a random small portion (up to 50 bytes) from the start of the file every 20 seconds.
3. The size checker monitors if the file exceeds 20 KB:
   - If exceeded, it logs the event and trims the file down to 10 KB.
   - Sends an email alert to notify the user.
4. Counters for appends and removes are reset after each size adjustment cycle.

---

## ⚠️ Important Notes

Running this project indefinitely will keep modifying the file unless manually stopped.
The current version does not handle graceful shutdown of threads.
Ensure SMTP settings are correct if enabling email notifications.

## ✨ Future Improvements

Command-line configuration for file names and sizes.
Graceful shutdown using thread events.
Support for multiple output formats (binary vs text mode).

## 🚀 Running the Project

Simply run the script:

```bash
python FileAppendRemove.py
