# Dishly 🍳 — Django CRUD Capstone

Dishly is a personal recipe manager built with Django. Authenticated users can create, view, edit, and delete recipes, mark favorites/likes, and quickly filter recipes using a live search bar. The UI uses a clean, warm palette and a responsive layout.

> **Status**: Capstone MVP complete — CRUD, auth, search, “My Recipes”, and likes. Ongoing polish: AJAX like button (no full reload), image placeholders, and responsive styling.


**Team Description 🍽️**
We’re not just building websites and projects — we’re cooking up greatness. 
Because we’re Hungry to be the Best — and second place isn’t on the menu. 😎🔥

**Hungry members:** 
Alaa AlTaher
Abdulrhman Yaghi
Abdelrazzaq Asfour
Abdullah Faouri 

---

## Table of Contents

* Overview
* Tech Stack
* Data Model (ERD)
* Installation & Setup
* Features
* User Stories
* Routing (URLs)
* Templates & Frontend
* Challenges & Solutions
* Changelog
* Contributing

---

## Overview

Dishly is a Django web app that lets users:

* Register / log in / log out
* Create, read, update, and delete recipes
* View their own recipes on **My Recipes**
* Like/favorite recipes
* Use a **live search** bar that filters sections in-page
* View a recipe details page with ingredients, steps, and actions

**Goal:** a simple, pleasant recipe notebook with clear code structure for learning and showcasing Django CRUD best practices.

---

## Tech Stack

* **Backend:** Python 3.13, Django 5.x
* **Database:** SQLite (dev) / PostgreSQL (optional)
* **Auth:** Django built-in auth (LoginView, signup via UserCreationForm)
* **Frontend:** Django templates, custom CSS, vanilla JS (live search, like toggle)
* **Static/Media:** Django staticfiles, local media uploads

---

## Data Model (ERD)

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

## Installation & Setup

### 1) Clone

```bash
git clone <your-repo-url>
cd Django-crud-capstone-Dishly
```

### 2) Virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Environment variables

Create `.env` with:

```
SECRET_KEY=replace-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5) Migrate and create superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6) Run server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

---

## Features

* **Auth:** Signup, Login, Logout
* **Recipes CRUD:** Create, Read, Update, Delete
* **My Recipes:** User-specific recipe list
* **Likes/Favorites:** Toggle per recipe
* **Search:** Live client-side search
* **Styling:** Responsive UI with warm colors

---

## User Stories

1. As a visitor, I can browse public recipes.
2. As a user, I can sign up, log in, and log out.
3. As a user, I can create and manage my recipes.
4. As a user, I can like recipes.
5. As a user, I can search for recipes instantly.
6. As a user, I can view my own recipes easily.

---

## Routing (URLs)

* `/` → Home / Recipe list (`name="recipe-list"`)
* `/recipes/<int:pk>/` → Recipe details (`name="recipe-detail"`)
* `/recipes/create/` → Create recipe (`name="recipe-create"`)
* `/recipes/<int:pk>/edit/` → Update recipe (`name="recipe-update"`)
* `/recipes/<int:pk>/delete/` → Delete recipe (`name="recipe-delete"`)
* `/my-recipes/` → Current user’s recipes (`name="my-recipes"`)
* `/like/<int:recipe_id>/toggle/` → Toggle like (`name="like-toggle"`)
* `/login/`, `/logout/`, `/signup/`

---

## Templates & Frontend

* Base: `base.html` (navbar + content block)
* Home: recipe cards, search bar
* Details: ingredients, steps, like button, view full recipe button
* CSS: warm gradient background, rounded cards

---

## Challenges & Solutions

**1. NoReverseMatch errors**
→ Fixed by matching URL names consistently.

**2. Redirect issues with ?next=**
→ Used `login_required` and direct redirects to home.

**3. Like button reloading**
→ Added `event.preventDefault()` and AJAX/HTMX toggle.

---

## Changelog

### [Unreleased]

* Improve AJAX like toggle
* Add pagination

### [2025-10-14] MVP Release

* Added CRUD functionality
* Added authentication
* Implemented My Recipes
* Styled UI
* Added Like system and search

---

## Contributing

* Create a branch for new features
* Follow commit convention: `feat(scope): message`
* Test before push

---

## License

MIT © 2025 Hungry Team (GA Jordan – Group 4)
