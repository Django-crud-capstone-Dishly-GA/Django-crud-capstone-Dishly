<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/87e18d84-9058-4a58-bdbc-be8c9c701793"
    alt="Dishly Logo"
    width="300"
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

Dishly is a personal recipe manager built with Django. Authenticated users can create, view, edit, and delete recipes, mark favorites/likes, and quickly filter recipes using a live search bar.  
The UI uses a clean, warm palette and a responsive layout.

> **Status:** ✅ Capstone MVP Complete — CRUD, auth, search, “My Recipes”, and likes.  
> 🛠️ Ongoing polish: AJAX like button (no full reload), image placeholders, and responsive styling.

---

## 🧑‍🍳 **Team Description**

We’re not just building websites — we’re cooking up greatness.  
Because we’re **Hungry to be the Best** — and second place isn’t on the menu. 😎🔥

### 👨‍👩‍👧‍👦 **Hungry Team Members:**
- **Alaa AlTaher**
- **Abdulrhman Yaghi**
- **Abdelrazzaq Asfour**
- **Abdullah Faouri**

---

## 📚 **Table of Contents**

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Data Model (ERD)](#data-model-erd)
4. [Installation & Setup](#installation--setup)
5. [Features](#features)
6. [User Stories](#user-stories)
7. [Routing (URLs)](#routing-urls)
8. [Templates & Frontend](#templates--frontend)
9. [Challenges & Solutions](#challenges--solutions)
10. [Changelog](#changelog)
11. [Contributing](#contributing)
12. [License](#license)

---

## 🧾 **Overview**

Dishly is a Django web app that lets users:

- Register / log in / log out  
- Create, read, update, and delete recipes  
- View their own recipes on **My Recipes**  
- Like/favorite recipes  
- Use a **live search bar** that filters results dynamically  
- View recipe details with ingredients, steps, and actions  

🎯 **Goal:** A simple, pleasant recipe notebook that showcases Django CRUD best practices and a clean user experience.

---

## ⚙️ **Tech Stack**

| Layer | Technologies |
|-------|---------------|
| **Backend** | Python 3.13, Django 5.x |
| **Database** | SQLite (dev) / PostgreSQL (optional) |
| **Auth** | Django built-in Auth (LoginView, UserCreationForm) |
| **Frontend** | Django Templates, Custom CSS, Vanilla JS |
| **Static & Media** | Django `staticfiles`, local image uploads |

---

## 🗂️ **Data Model (ERD)**

```
User (django.contrib.auth.User)
 └── (1-to-Many) Recipe.user

Recipe
 - id (PK)
 - user (FK → User)
 - title (Char)
 - description (Text)
 - ingredients (Text)
 - steps (Text)
 - image (ImageField)
 - created_at (DateTime)
 - updated_at (DateTime)

Favorite / Like
 - id (PK)
 - user (FK → User)
 - recipe (FK → Recipe)
 - Unique(user, recipe)
```

---

## 🧰 **Installation & Setup**

### 1️⃣ Clone

```bash
git clone <your-repo-url>
cd Django-crud-capstone-Dishly
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
# Activate it
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

## 🌟 **Features**

✅ **Authentication** – Signup, Login, Logout  
✅ **Recipes CRUD** – Create, Read, Update, Delete  
✅ **My Recipes** – View recipes created by the logged-in user  
✅ **Likes/Favorites** – Toggle like per recipe  
✅ **Search** – Real-time client-side filtering  
✅ **Responsive Styling** – Warm color palette, clean UI  

---

## 🧩 **User Stories**

1. As a visitor, I can browse public recipes.  
2. As a user, I can sign up, log in, and log out.  
3. As a user, I can create and manage my recipes.  
4. As a user, I can like recipes.  
5. As a user, I can search for recipes instantly.  
6. As a user, I can view my own recipes easily.

---

## 🌐 **Routing (URLs)**

| Path | Description | Name |
|------|--------------|------|
| `/` | Home / Recipe List | `recipe-list` |
| `/recipes/<int:pk>/` | Recipe Details | `recipe-detail` |
| `/recipes/create/` | Create Recipe | `recipe-create` |
| `/recipes/<int:pk>/edit/` | Update Recipe | `recipe-update` |
| `/recipes/<int:pk>/delete/` | Delete Recipe | `recipe-delete` |
| `/my-recipes/` | User’s Own Recipes | `my-recipes` |
| `/like/<int:recipe_id>/toggle/` | Toggle Like | `like-toggle` |
| `/login/`, `/logout/`, `/signup/` | Auth Views | — |

---

## 🎨 **Templates & Frontend**

| Template | Purpose |
|-----------|----------|
| `base.html` | Navbar, structure, blocks |
| `home.html` | Recipe cards, live search |
| `details.html` | Recipe details, ingredients, like button |
| `myrecipe.html` | User’s recipes list |
| `recipe_form.html` | Create / Edit form |
| `recipe_confirm_delete.html` | Delete confirmation |
| `CSS` | Custom warm palette, responsive design |

---

## 💡 **Challenges & Solutions**

| Challenge | Solution |
|------------|-----------|
| **NoReverseMatch errors** | Matched URL names consistently. |
| **Redirect issues with `?next=`** | Used `login_required` + redirects to home. |
| **Like button reloading** | Added `event.preventDefault()` and AJAX toggle. |

---

## 🧾 **Changelog**

### 🧱 [Unreleased]
- Improve AJAX like toggle  
- Add pagination  

### 🎉 [2025-10-14] MVP Release
- Added CRUD functionality  
- Added authentication  
- Implemented My Recipes  
- Styled UI  
- Added Like system and live search  

---

## 🤝 **Contributing**

1. Create a new branch for your feature:
   ```bash
   git checkout -b feat/your-feature
   ```
2. Follow commit convention:
   ```
   feat(scope): message
   ```
3. Test before pushing.

---

## 📜 **License**

MIT © 2025 **Hungry Team** (GA Jordan – Group 4)
