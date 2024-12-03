# Pull Request Analysis Tool

A FastAPI-based service for analyzing GitHub pull requests using AI language models. The tool integrates asynchronous task processing with Celery and supports both remote and local model execution.

---

## 🚀 Project Setup

### Requirements
- Python 3.8+
- FastAPI
- Celery
- Redis
- Local running instance of Llama
- pytest 

### Running
1. **Clone the repository**:

   ```bash
   git clone git@github.com:PranavAga/potpieai-backend_assignment.git
   cd  potpieai-backend_assignment
   ```

2. **Install required python packages**
    ```bash
    pip install -r src/requirements.txt
   ```
  
2. **Run Llama instance locally**:

   ```bash
   ollama run llama3.2
   ```

   Setup the URL in in `src/.env`. Refer to `src/.env.example`.
3. - **Run the Celery worker (Windows)**
      ```bash
      celery -A main.celery_app worker --loglevel=info --pool=solo
      ``` 
    - **Run the Celery worker (others)**
      ```bash
      celery -A main.celery_app worker --loglevel=info
      ``` 
4. **Run the FastAPI application**: 
    ```bash
    uvicorn main:app --reload
    ``` 


---

## 📚 APIs

1. ### POST `/analyze-pr`
- **Description**: Initiates analysis of a GitHub pull request.
- **Input**:
  ```json
  {
    "repo_url": "https://github.com/user/repo",
    "pr_number": 123,
    "github_token": "optional_token"
  }
  ```
- **Response**:
  ```json
  {
    "task_id": "unique-task-id"
  }
  ```

2. ### GET `/status/{task_id}`
- **Description**: Checks the status of an analysis task.
- **Response**:
  ```json
  {
    "task_id": "unique-task-id",
    "status": "PENDING|IN_PROGRESS|COMPLETED|FAILED"
  }
  ```

3. ### GET `/results/{task_id}`
- **Description**: Retrieves the results of a completed analysis.
- **Response**:
  ```json
    {
        "task_id": "abc123",
        "status": "completed",
        "results": {
            "files": [
                {
                    "name": "main.py",
                    "issues": [
                        {
                            "type": "style",
                            "line": 15,
                            "description": "Line too long",
                            "suggestion": "Break line into multiple lines"
                        },
                        {
                            "type": "bug",
                            "line": 23,
                            "description": "Potential null pointer",
                            "suggestion": "Add null check"
                        }
                    ]
                }
            ],
            "summary": {
                "total_files": 1,
                "total_issues": 2,
                "critical_issues": 1
            }
        }
    }
  ```

---

## 🛠️ Design Decisions

1. **FastAPI for APIs**:
   - Chosen for its asynchronous capabilities and easy-to-use interface.

2. **Celery for Task Queue**:
   - Using Celery for async task processing

3. **Redis**:
  - Using Redis as the message broker for Celery, along with to store the results

4. **LLM Integration**: 
  - Used localy running of Llama 3.2 with Ollama
   
---

## 🚀 Future Improvements

1. **Enhanced Authentication**:
   - Add OAuth integration for secure GitHub API interactions.

2. **WebSocket Support**:
   - GitHub webhook support.

3. **Frontend Integration**:
   - Build a simple dashboard for visualizing pull request analysis.
   

---

## 🧪 Running Tests

1. **Install testing dependencies**:
   ```bash
   pip install pytest
   ```

2. **Environmet variables**:

   Setup environmet variables in `src/.env`. Refer to `src/.env.example`.

3. **Run tests**:
   ```bash
   pytest
   ```

---
