# Neo4j FastAPI Application

This is a FastAPI-based backend application that integrates with a Neo4j graph database.

---
## 🚀 Getting Started

1. **Clone the Repository :**

```
   git clone <repo-url> 
   cd <project-folder>
```

2. **Set Up Virtual Environment :**

 ```
    python -m venv .venv_gsheet
.venv_gsheet\Scripts\activate

python -m venv .venv_global
.venv_global\Scripts\activate
 ```

   On Windows:
 ```
   .{name}\Scripts\activate
```

   On Unix/macOS:
```
   source .{name}/bin/activate
 ```

3. **Install Dependencies :**
```
   pip install -r requirements.txt
```

---
## 🛠️ Neo4j Setup

Make sure Neo4j is installed and running locally.

Download Neo4j from: [Neo4j.download](https://neo4j.com/download/)

Use the following connection settings (or set them in a `.env` file):

  ```
  URI = "bolt://localhost:7687"

  USER = "neo4j"

  PASSWORD = "12345678"
```

**Tip :**
Create a `.env` file in the project root and add the above variables.

---
## 🏃 Run the Application

Run the FastAPI server with :
```
   uvicorn main:app --reload
```

**Visit :**
  + [Base API](http://127.0.0.1:8000)           - for base API
  + [Swagger UI](http://127.0.0.1:8000/docs)     - for Swagger UI API docs

----

## ✅ Summary

- Python backend using FastAPI
- Connects to Neo4j via `neo4j` driver
- Configurable via `.env`
- Run locally using `uvicorn`

---
## 🔗 Useful Links


- [FastAPI](https://fastapi.tiangolo.com/)
- [Neo4j](https://neo4j.com/docs/)
- [Uvicorn](https://www.uvicorn.org/)
