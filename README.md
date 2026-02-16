# CS50 Web Programming – Project 1: Wiki

## 📌 Overview

This project is a simple online encyclopedia similar to Wikipedia, built using Django.

Users can:
- View encyclopedia entries
- Search for entries
- Create new pages
- Edit existing pages
- Visit a random page

Markdown is used to write content, and it is converted to HTML before being displayed.

---

## ⚙️ Technologies Used

- Python
- Django
- HTML
- Markdown (markdown2 library)

---

## 🚀 Features

### 1️⃣ Entry Page
Each encyclopedia entry can be accessed via a unique URL:
If the entry exists, its Markdown content is converted to HTML and displayed.
If it does not exist, an error page is shown.

---

### 2️⃣ Index Page
The home page lists all available entries.
Each entry is clickable and redirects to its corresponding page.

---

### 3️⃣ Search
The search bar allows users to search for entries.

- If the query exactly matches an entry, the user is redirected to that page.
- If the query partially matches multiple entries, a list of results is displayed.

---

### 4️⃣ Create New Page
Users can create a new encyclopedia entry by providing:
- A title
- Markdown content

If the title already exists, an error message is displayed.
Otherwise, the page is saved and the user is redirected to the new entry.

---

### 5️⃣ Edit Page
Each entry has an Edit button.
Users can modify the existing Markdown content.
After saving, they are redirected back to the updated page.

---

### 6️⃣ Random Page
The "Random Page" button selects a random entry and redirects the user to it.

---

## 🧠 Markdown Support

This project uses the `markdown2` library to convert Markdown content into HTML before displaying it.

Example Markdown:
```markdown
# Heading
**Bold text**
- List item

