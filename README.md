# 🚚 Crapules Express - Discord Bot ![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)

Welcome to the official repository of the **Crapules Express** Discord bot, developed for the virtual VTC *(trucking company)* on *Euro Truck Simulator 2* (ETS2).

This bot is designed to handle **recruitment**, **ticketing**, **convoy scheduling**, **HR processes**, and **internal moderation** for Crapules Express.

> 🔧 **Developed by**: [nerfine](https://github.com/nerfine)

---

## ✅ Bot Status

The bot is **now fully online**.  
If it temporarily shuts down, it's likely due to a brief **internet restart**.

All core systems are being actively tested.  
Some features may still contain **minor bugs**, which are being monitored and fixed quickly.

> **Note:** All previous data has been deleted for security and reliability reasons.

---

## 🚀 Early Release – Version 2.0.0

The bot is in **early-access release**. While stable, some flaws may occur during usage and will be addressed immediately for the best experience.

---

## 📦 Key Features (Live or Near-Complete)

- 🎟️ **Ticket System**:
  - Recruitment applications (modal form, HR pipeline)
  - Convoy slot reservations or invitations
  - Private questions to management
- 📋 **Recruitment Process**:
  - Modal-based applications
  - Locker system
  - Interview scheduling, rescheduling & override
- 🧾 **Convoy Tools** (in progress):
  - Convoy tickets with form-based input
  - Staff-side review, approval, or rejection
- 🔧 **HR/Moderation Commands**:
  - Blacklist & unblacklist users
  - Show user info and status
  - Add/remove trial drivers or fire drivers
- ⚙️ **Admin & Utility Commands**:
  - `/bot`, `/commands`, `/ticket-setup`, `!restart`, `!shutdown`
- 🔐 **Role-based permissions system** with owner override
- 🧠 **Logging System**:
  - Console logs and errors sent to Discord
  - Invite tracker & welcomer alerts
  - `/bump` tracking and reminders

---

## 💬 Slash Commands Overview

| Command | Description |
|---------|-------------|
| `/bot`  | Show bot info: version, ping, uptime, developer |
| `/commands` | Lists all available commands |
| `/user-info` | Displays a user’s HR/recruitment status |
| `/locker-show` | Show a user's locker channel |
| `/blacklist` / `/unblacklist` | Moderate access to recruitment |
| `/interview-startnow` | Start an interview manually |
| `/fire-driver` | Remove a driver from the VTC |

*(More commands listed in `/commands` output in Discord)*

---

## 🔐 Privacy Policy

Crapules Express is committed to respecting user privacy.

- ✅ [Privacy Policy](https://github.com/Nerfine/crapules-express/blob/main/privacy.md)
- 📁 Data is stored locally on a private VPS
- 🗑️ Inactive recruitment tickets auto-close after 24h
- 👤 Access restricted to authorized HR and management roles only

---

## 🧱 Tech Stack

- Language: **Python** (rewritten from Discord.js)
- Libraries: `discord.py` (nextcord/pycord), modals, buttons
- Database: Local JSON or persistent VPS storage
- Hosting: Private VPS (self-hosted)
- Logging: Webhooks for logs and error tracking

---

## 🧑‍💼 Intended Use

This bot is for **internal use only** by the **Crapules Express** VTC.

> ❌ Reuse, redistribution, or modification without permission is prohibited.

---

## 📄 License

This project uses a **private license**.  
All rights reserved © **Crapules Express** – [nerfine](https://github.com/nerfine)

---

## 🤝 Contact

For questions, issues, or requests:

- 💬 Discord: **@nerfine**
- 📺 Server: https://discord.gg/crxp
- 🐞 GitHub Issues: [Submit here](https://github.com/Nerfine/crapules-express/issues)

---

Thank you for your support and feedback during the development of Crapules Express 2.0.0!
