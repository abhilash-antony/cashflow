## 📝 Django Expense Tracker – Key Design Notes

### 🔹 Core Features

1. **Add New Record (Insertion)**

   * Use a form (`ModelForm`) to input: Date, Category, Description, Payment Method, Amount, Type (Expense/Income).
   * Data gets stored in the database (e.g., SQLite for dev, PostgreSQL for prod).

2. **Soft Delete (Safe Deletion)**

   * Model includes a field: `is_deleted = BooleanField(default=False)`.
   * “Delete” action sets `is_deleted=True` instead of removing the record.
   * Views should filter using `is_deleted=False` so deleted records are hidden.
   * Add a **confirmation popup** → “Are you sure you want to delete this record?”.
   * Optional: “Deleted Records” page (recycle bin) to restore records.

3. **Update/Edit Record**

   * Each row in the expense table has an **Edit button**.
   * Opens a pre-filled form with existing values.
   * After changes, show **confirmation popup** → “Are you sure you want to update this record?”.
   * On confirm → update DB.
   * Keep a **Last Updated timestamp** field for tracking changes.
   * Optional: maintain a **change log** (old vs new values).

4. **Balance & Summaries** (future step)

   * Balance column can be computed dynamically (Income adds, Expense subtracts).
   * Later enhancements: category-wise totals, monthly summaries, charts (Chart.js, Plotly).

---

### 🔹 User Interface (UI) Notes

* Expense list page displays records in a table with **Edit** ✏️ and **Delete** 🗑️ buttons.
* Add record → separate form page or modal popup.
* Delete → soft delete with confirmation popup.
* Edit → opens form (or inline edit) with confirmation popup before saving.

---

### 🔹 Best Practices

* Start with **CRUD basics** (Create, Read, Update, Soft Delete).
* Use **ModelForm** for Add/Edit to keep code clean.
* Always confirm destructive actions (update/delete).
* Consider a **Recycle Bin** feature for maximum safety.
* Later, add **user accounts** if multi-user support is needed.

---


## 🖥️ UI Design – Django Expense Tracker

### 🔹 1. Dashboard / Home Page

* **Header:** App name (e.g., *My Expense Tracker*).
* **Quick Stats (cards at the top):**

  * Total Balance 💰
  * Total Expenses 📉
  * Total Income 📈
* **Navigation bar / sidebar:** Links to

  * Dashboard
  * Add Expense
  * Deleted Records (Recycle Bin)
  * Reports/Summary

---

### 🔹 2. Expense List Page (Main Table View)

A table that looks like:

| Date       | Category | Description | Payment Method | Amount (₹) | Type    | Balance | Actions |            |
| ---------- | -------- | ----------- | -------------- | ---------- | ------- | ------- | ------- | ---------- |
| 08/02/2025 | Food     | Lunch       | UPI            | 250        | Expense | 9,750   | ✏️ Edit | 🗑️ Delete |

**Features:**

* **Edit button (✏️)** → opens edit form.
* **Delete button (🗑️)** → triggers confirmation popup → soft delete.
* **Filter options** at the top (by Date range, Category, Type, Payment Method).
* **Search bar** to quickly find a record.
* Pagination or scrolling for large datasets.

---

### 🔹 3. Add Expense Page (Form)

Form fields (with dropdowns):

* Date (calendar picker 📅)
* Category (dropdown)
* Description (text field)
* Payment Method (dropdown: Cash, UPI, Card, etc.)
* Amount (numeric field, currency formatted)
* Type (radio: Expense / Income)
* **Submit button** → adds record to DB.

---

### 🔹 4. Edit Expense Page

* Same form as Add, but pre-filled with current values.
* When clicking **Save**, show confirmation popup:

  ```
  Are you sure you want to update this record?
  ```
* On confirm → update DB.

---

### 🔹 5. Deleted Records Page (Recycle Bin)

* Shows all records where `is_deleted=True`.
* Table format similar to main view.
* Actions:

  * **Restore** (♻️) → sets `is_deleted=False`.
  * **Permanent Delete** (⚠️ optional) → actually removes from DB.

---

### 🔹 6. Reports / Summary (Future Feature)

* Graphs:

  * Pie chart → category-wise spending.
  * Bar chart → monthly expenses vs income.
  * Line chart → balance trend over time.
* Filters for custom date ranges.

---

👉 Overall look:

* **Clean table-based interface** (like Google Sheets but prettier).
* Buttons/icons for **Edit/Delete/Restore** to keep it intuitive.
* Popups for confirmation.
* Simple navigation (Dashboard → Records → Recycle Bin → Reports).

---