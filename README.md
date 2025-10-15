<p align="center">
  <img
    src="https://github.com/user-attachments/assets/87e18d84-9058-4a58-bdbc-be8c9c701793"
    alt="Dishly Logo"
    width="350"
    style="
      border-radius: 20px;
      background: linear-gradient(135deg, #fff8f3, #ffe9d2);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
      padding: 20px;
      margin: 10px 0;
      transition: all 0.3s ease-in-out;
    "
    onmouseover="this.style.transform='scale(1.03)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.3)';"
    onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.25)';"
  >
</p>

<h1 align="center">🍳 Dishly — Django CRUD Capstone</h1>

<p align="center">
  A warm and simple recipe manager built with <strong>Django</strong>.<br>
  Create, share, and manage your favorite dishes — because we’re <em>Hungry to be the Best.</em> 😎🔥
</p>

---

Dishly is a personal recipe manager built with Django. Authenticated users can create, view, edit, and delete recipes, mark likes, and quickly filter recipes using a live search bar.
The UI uses a clean, warm palette and a responsive layout.

---

## 🧑‍🍳 Team Description

We’re not just building websites — we’re cooking up greatness.
Because we’re **Hungry to be the Best** — and second place isn’t on the menu. 😎🔥

### 👨‍👩‍👧‍👦 Hungry Team Members

* **Alaa AlTaher**
* **Abdulrhman Yaghi**
* **Abdelrazzaq Asfour**
* **Abdullah Faouri**

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Data Model (ERD)](#data-model-erd)
4. [Installation & Setup](#installation--setup)
5. [Features](#features)
6. [User Stories](#user-stories)
7. [Routing (URL Names)](#routing-url-names)
8. [Templates & Frontend](#templates--frontend)
9. [Unit Tests](#unit-tests)
10. [Challenges & Solutions](#challenges--solutions)
11. [Changelog](#changelog)
12. [Contributing](#contributing)
13. [License](#license)

---

## 🧾 Overview

Dishly is a Django web app that lets users:

* Register / log in / log out
* Create, read, update, and delete recipes
* View their own recipes on **My Recipes**
* Like recipes
* Use a **live search bar** that filters results dynamically
* View recipe details with ingredients, steps, and actions

🎯 **Goal:** A simple, pleasant recipe notebook that showcases Django CRUD best practices and a clean user experience.

---

## ⚙️ Tech Stack

| Layer              | Technologies                                       |
| ------------------ | -------------------------------------------------- |
| **Backend**        | Python 3.13, Django 5.x                            |
| **Database**       | SQLite (dev)                                       |
| **Auth**           | Django built-in Auth (LoginView, UserCreationForm) |
| **Frontend**       | Django Templates, Custom CSS, Vanilla JS           |
| **Static & Media** | Django `staticfiles`, local image uploads          |
| **Testing**        | Django `TestCase` / `Client` (unittest style)      |

---

## 🗂️ Data Model (ERD)

> **models and relations**.

```
User (django.contrib.auth.models.User)
  ├─< Recipe.user (FK)
  └─<> Recipe.likes (M2M)

Ingredient
  └─<> Recipe.ingredients (M2M)

Recipe
 - id (PK)
 - user (FK → User, required)
 - name (CharField)
 - description (TextField)
 - category (CharField)
 - image_url (URLField or ImageField, optional over commits)
 - created_at (DateTime, often auto_add)
 - updated_at (DateTime, often auto_now)
 - likes (ManyToManyField → User, blank=True)
 - ingredients (ManyToManyField → Ingredient, optional)
```

**Relations**

* A **User** can create many **Recipes** (`ForeignKey`).
* A **User** can **like** many recipes, and a **Recipe** can be liked by many users (`ManyToMany`).
* A **Recipe** can reference many **Ingredients** (and each **Ingredient** can belong to many recipes) via `ManyToMany`.

> Notes from repo history: migrations include an `Ingredient` model (introduced around `0003`), an `image_url` evolution (`0004/0005`), and `likes` added on `0006`.

---

## 🧰 Installation & Setup

### 1️⃣ Clone

```bash
git clone <your-repo-url>
cd Django-crud-capstone-Dishly
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a `.env` file and add:

```
SECRET_KEY=replace-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5️⃣ Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🌟 Features

✅ **Authentication** – Signup, Login, Logout
✅ **Recipes CRUD** – Create, Read, Update, Delete
✅ **My Recipes** – View recipes created by the logged-in user
✅ **Likes** – Toggle like per recipe
✅ **Search** – Client-side filtering (JS script on home page)
✅ **Responsive Styling** – Warm color palette, clean UI
✅ **Unit Tests** – Signup flow, CRUD permissions, URL resolution, list/detail views

---

## 🧩 User Stories

1. As a visitor, I can browse public recipes.
2. As a user, I can sign up, log in, and log out.
3. As a user, I can create and manage my recipes.
4. As a user, I can like recipes.
5. As a user, I can search for recipes instantly.
6. As a user, I can view my own recipes easily.
7. As a developer, I can run automated tests to verify core flows.

---

## 🌐 Routing (URL Names)

> Taken from `dishly_app/tests/test_urls.py` and views.

| URL **name**    | Purpose                                    |
| --------------- | ------------------------------------------ |
| `recipe-list`   | Home / recipe list                         |
| `recipe-detail` | Recipe details (expects `pk`)              |
| `recipe-create` | Create a recipe                            |
| `recipe-update` | Update a recipe (expects `pk`)             |
| `recipe-delete` | Delete a recipe (expects `pk`)             |
| `myrecipe`      | Logged-in user’s recipes page              |
| `like-recipe`   | Like/Unlike a recipe (expects `recipe_id`) |
| `signup`        | Registration page                          |

---

## 🎨 Templates & Frontend

Repo paths:

| File                                            | Purpose                                                                                   |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `dishly_app/templates/dishly_app/home.html`     | Recipe cards, search input, like/login UI; includes client-side filtering script          |
| `dishly_app/templates/registration/signup.html` | Signup form; now shows an inline error message on invalid entries                         |
| Other templates                                 | `recipe_form.html`, `recipe_confirm_delete.html`, details, etc.                           |
| CSS                                             | Example: `dishly_app/static/css/signup.css` (polish/spacing/animation updated 2025-10-15) |

---

## 🔧 Unit Tests

Added **2025-10-15**:

```
dishly_app/
└─ tests/
   ├─ __init__.py
   ├─ test_crud_permissions.py
   ├─ test_signup.py
   ├─ test_urls.py
   └─ test_views_list_detail.py
```

**Coverage**

* `test_signup.py` — page loads, success flow, password mismatch shows **“Invalid sign up — please check your details.”**
* `test_crud_permissions.py` — owner vs non-owner update/delete behavior; create requires login
* `test_urls.py` — named URL reversing & resolving
* `test_views_list_detail.py` — list & detail render a seeded recipe and return 200

Run:

```bash
python manage.py test
```

---

## 💡 Challenges & Solutions

| Challenge                                     | Solution                                                                           |
| --------------------------------------------- | ---------------------------------------------------------------------------------- |
| Signup tests failed due to missing error text | Added inline error message to `registration/signup.html` when `form.errors` exists |
| NoReverseMatch / URL mismatches               | Standardized URL names in tests and views                                          |
| Like button UX for anonymous users            | Show Login button in `home.html` when not authenticated                            |
| Style polish / responsiveness                 | `static/css/signup.css` refined (radius, animation, inputs)                        |

---

## 🧾 Changelog

### 🛠️ 2025-10-15 — Unit Tests & UI Polish

* Added tests under `dishly_app/tests/`
* Signup template shows invalid message when errors exist
* Home page: login prompt next to like; client-side search polish
* CSS: `static/css/signup.css` improved
* Commit: [`16fb518`](https://github.com/Django-crud-capstone-Dishly-GA/Django-crud-capstone-Dishly/commit/16fb51870279b81ca1143009e196c79015039687)

### 🎉 2025-10-14 — MVP Release

* CRUD functionality completed
* Authentication & user recipes added
* Likes & live search implemented
* UI and CSS polish applied

---

## 🤝 Contributing

1. Create a new branch:

   ```bash
   git checkout -b feat/your-feature
   ```
2. Conventional commits:

   ```
   feat(scope): short message
   ```
3. Run tests before pushing:

   ```bash
   python manage.py test
   ```

---

## 📜 License

MIT © 2025 **Hungry Team** (General Assembly Jordan – Group 4)
