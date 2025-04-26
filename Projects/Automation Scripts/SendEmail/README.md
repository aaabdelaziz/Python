# File Size Monitoring, Management, and Alert System

## Overview

This Python project provides a multithreaded tool to **simulate file growth**, **periodically manage file size**, and **send an alert** when a critical size threshold is reached.

The tool is designed for educational and demonstration purposes — especially useful for learning about multithreading, file I/O, and basic alerting mechanisms in Python.

---

## 📚 Features

- **Multithreaded architecture**:
  - Append random data to a file at regular intervals.
  - Remove random data from the file to simulate usage.
  - Monitor file size continuously.
- **File Size Management**:
  - Auto-trims file to a reduced size when a maximum threshold is reached.
- **Logging**:
  - Records all threshold exceedance events with timestamps in a log file.
- **Email Notification**:
  - Sends an alert email when the file exceeds the defined maximum size. (Configurable SMTP server)

---

## ⚙️ Technologies Used

- Python 3.x
- Libraries:
  - `threading`
  - `smtplib`
  - `email.mime.text`
  - `random`
  - `time`
  - `os`

---

## 🔧 Configuration

You can adjust the following settings inside the script:

| Setting | Description | Default Value |
|:---|:---|:---|
| `FileName` | Target file name to append/remove data | `"out.bin"` |
| `LogName` | Log file name | `"log.txt"` |
| `RequiredAppendTime` | Interval to append random bits (in seconds) | `10` |
| `RequiredRemoveTime` | Interval to remove random bits (in seconds) | `20` |
| `RequiredFileCheckSize` | Max allowed file size in bytes | `19999` |
| `RequiredReduceSize` | Size to reduce file to after exceeding limit | `10000` |

The script will start 3 threads automatically:

Append thread
Remove thread
File size monitor thread

---

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. (Optional) Configure SMTP server settings if you want email notifications.
3. Run the script:

```bash
python SendEmail.py
