# 🏥 Patient Management System API

A lightweight, fully functional **CRUD REST API** built with **FastAPI** to manage patient health records — complete with automatic **BMI calculation** and **health verdict classification** using Pydantic's computed fields.

This project is designed as a **beginner-friendly, end-to-end reference implementation** for anyone learning FastAPI — covering request validation, path/query parameters, computed fields, custom exceptions, and file-based persistence — before moving on to database-backed applications.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Why This Project](#why-this-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Sample Data Format](#sample-data-format)
- [Concepts You'll Learn](#concepts-youll-learn)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

---

## 🩺 Overview

The **Patient Management System API** allows you to create, view, update, delete, and sort patient records via simple REST endpoints. Patient vitals (height & weight) are used to automatically compute **BMI** and a corresponding **health verdict** (`Underweight`, `Normal`, `Obese`) using Pydantic's `@computed_field` decorator — no manual calculation required on the client side.

Data is persisted in a local JSON file (`data/patients.json`), making the project dependency-light and ideal for understanding core FastAPI + Pydantic concepts without the overhead of setting up a database.

---

## 🎯 Why This Project

This repository is intentionally kept **simple, readable, and well-structured** so that developers new to FastAPI can:

- Understand how FastAPI automatically validates and documents APIs using Pydantic models
- See a realistic, real-world use case (a healthcare-style CRUD system) instead of a toy "Hello World" example
- Learn best practices like separating **create** and **update** models, using `Annotated` typing, and returning proper HTTP status codes
- Get a solid foundation before moving to production-grade concerns like databases, authentication, and deployment

If you're comfortable with Python but new to building APIs, this project is a great hands-on starting point.

---

## ✨ Features

- ✅ Full CRUD operations (Create, Read, Update, Delete) on patient records
- ✅ Auto-calculated **BMI** and **health verdict** via Pydantic computed fields
- ✅ Strict field validation (age, height, weight, gender) using Pydantic `Field` constraints
- ✅ Separate `Patient` (create) and `PatientUpdate` (partial update) models
- ✅ Sorting patients by height, weight, or BMI in ascending/descending order
- ✅ Proper HTTP status codes and error handling (`404`, `400`, `201`)
- ✅ Auto-generated interactive API documentation via Swagger UI & ReDoc
- ✅ Simple JSON file-based storage — no database setup required to get started

---

## 🛠 Tech Stack

| Component        | Technology                  |
|-------------------|------------------------------|
| Framework         | [FastAPI](https://fastapi.tiangolo.com/) |
| Data Validation   | [Pydantic v2](https://docs.pydantic.dev/) |
| Language          | Python 3.10+                |
| Server            | Uvicorn (ASGI)               |
| Storage           | JSON file (`data/patients.json`) |

---

## 📁 Project Structure

```
patient-management-api/
│
├── main.py                # Application entry point with all API routes
├── data/
│   └── patients.json      # JSON-based data store for patient records
├── requirements.txt       # Project dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/patient-management-api.git
   cd patient-management-api
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```
   *(or, if you add a `requirements.txt`)*
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the data directory and seed file**
   ```bash
   mkdir data
   echo "{}" > data/patients.json
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - Base URL: `http://127.0.0.1:8000`
   - Interactive Swagger Docs: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints

| Method | Endpoint                | Description                                  |
|--------|--------------------------|-----------------------------------------------|
| GET    | `/`                      | Welcome message                              |
| GET    | `/about`                 | Short description of the API                 |
| GET    | `/view`                  | Retrieve all patient records                  |
| GET    | `/view/{patient_id}`     | Retrieve a specific patient by ID             |
| GET    | `/sort`                  | Sort patients by `height`, `weight`, or `bmi` |
| POST   | `/create`                | Create a new patient record                   |
| PUT    | `/edit/{patient_id}`     | Update an existing patient's details          |
| DELETE | `/delete/{patient_id}`   | Delete a patient record                       |

### Example — Create a Patient

```http
POST /create
Content-Type: application/json

{
  "id": "P001",
  "name": "John Doe",
  "city": "Pune",
  "age": 30,
  "gender": "male",
  "height": 1.75,
  "weight": 72.5
}
```

**Response**
```json
{
  "message": "Patient created successfully !!"
}
```

### Example — Sort Patients

```http
GET /sort?sort_by=bmi&order=desc
```

### Example — Update a Patient

```http
PUT /edit/P001
Content-Type: application/json

{
  "weight": 68.0
}
```

Only the fields provided are updated — the rest remain unchanged, and BMI/verdict are automatically recalculated.

---

## 📄 Sample Data Format

Each patient record stored in `data/patients.json` follows this structure (the `id` is used as the dictionary key):

```json
{
  "P001": {
    "name": "John Doe",
    "city": "Pune",
    "age": 30,
    "gender": "male",
    "height": 1.75,
    "weight": 72.5,
    "bmi": 23.67,
    "verdict": "Normal"
  }
}
```

---

## 📚 Concepts You'll Learn

This project is a practical playground for the following FastAPI & Pydantic concepts:

- Defining request/response models with **Pydantic `BaseModel`**
- Field-level validation using `Field(..., gt=, lt=, description=)`
- Restricting values with `Literal` types (e.g., gender)
- Auto-generated derived attributes using `@computed_field` + `@property`
- Optional/partial update models with `Optional` and `exclude_unset=True`
- Path parameters (`Path`) vs Query parameters (`Query`)
- Raising and customizing errors with `HTTPException`
- Returning custom status codes using `JSONResponse`
- Reading and writing structured data using plain JSON files

---



## 📄 License

This project is for educational and demonstration purposes. Feel free to fork and extend.
This project is for educational purposes. Feel free to use and adapt it for your own learning.



## ⭐ If you found this helpful

Give this repository a star ⭐ 
