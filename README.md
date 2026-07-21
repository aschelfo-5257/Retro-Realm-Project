# Retro Realm Games - Database Management Application

A terminal-based Python application that interfaces with a remote MySQL database instance to manage inventories, storefront branches, hardware platforms, and customer sales pipelines for **Retro Realm Games**.

## 📖 Project Overview

Retro Realm Games is a traditional retail storefront specializing in vintage gaming cartridges, classic consoles, and hardware accessories from 8-bit systems to the early 2000s. 

Historically, operations relied on manual paper logs and physical index cards, causing severe bottlenecks in stock tracking, missing receipt verification, and obscure revenue reporting. This centralized Python database management system modernizes operations, implementing rigorous transactional logging and data validation loops to streamline store operations.

---

## 🗄️ Database Schema Overview

The underlying remote database is structured across five highly normalized relational tables:

1. **`Stores`**: Centralizes physical branch locations, tracking specific city markets and official contact lines.
2. **`Platforms`**: Logs retro computing architectures and console generations alongside historical release tracking.
3. **`Games`**: Manages specific retro cartridge and disc inventory items linked to a parent platform and physical hardware quality attributes (`game_condition`).
4. **`Sales`**: Automates financial invoicing by tracking receipt dates, processing storefront locations, and gross revenue collections.
5. **`Transaction`**: Operates as a critical bridge table linking distinct inventory items to parent transactional sales receipts.

---

## 💻 Application Features

The terminal software implements a command menu system structured to manage data workflows:

*   **Add Data Records (CREATE)**: Interactive sub-menus allowing operational managers to supply arguments and safely populate rows inside the `Games` and `Platforms` tables.
*   **Update Records (UPDATE)**: Targeted database mutation handlers built to update properties (such as inventory condition updates or storefront contact alterations).
*   **Delete Entries (DELETE)**: Dedicated isolation deletion sub-menu to clear obsolete or invalid table rows cleanly.
*   **Advanced Multi-Table Reports (READ/JOINs)**: Analytical reports utilizing composite relational queries (`JOIN` syntax) to cleanly output structured strings summarizing console lines, game availability, and branch distributions.
*   **ACID Compliant Invoicing (Transactions)**: Heavy-duty single-unit execution block linking `INSERT` and `UPDATE` syntax together via rigorous `commit()` and `rollback()` error catch blocks to execute sales securely.

---

## 🚀 Installation & Setup Guide

### 📋 Prerequisites
Ensure your local terminal environment has Python 3.x installed alongside the standard MySQL database connection module:
```bash
pip install mysql-connector-python
```

### ⚙️ Database Configuration
To bridge your Python environment to the active instance, configure your server endpoints inside the initialization variables:
```python
# Configuration parameters within main.py
DB_HOST = "your-remote-host-endpoint"
DB_USER = "your-database-username"
DB_PASSWORD = "your-database-password"
DB_NAME = "retrorealmgames"
```
### Running the Application
Launch the text-driven administration interface by calling the file module:
```bash
python main.py
```
