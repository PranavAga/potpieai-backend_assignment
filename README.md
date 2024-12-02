# Pull Request Analysis Tool

A FastAPI-based service for analyzing GitHub pull requests using AI language models. The tool integrates asynchronous task processing with Celery and supports both remote and local model execution.

---

## 🚀 Project Setup

### Prerequisites
- Python 3.8+
- PostgreSQL for task queue management
- API key for your chosen LLM provider (e.g., OpenAI or Anthropic) if using remote models

### Installation
1. **Clone the repository**: <!-- TODO -->

   ```bash
   git clone git@github.com:PranavAga/potpieai-backend_assignment.git
   cd <repo>
   ```

2. **Run the FastAPI application**: <!-- TODO -->

   ```bash
   uvicorn app.main:app --reload
   ``` 

---

## 📚 API Documentation

### POST `/analyze-pr`
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

### GET `/status/{task_id}`
- **Description**: Checks the status of an analysis task.
- **Response**:
  ```json
  {
    "task_id": "unique-task-id",
    "status": "PENDING|STARTED|SUCCESS|FAILURE"
  }
  ```

### GET `/results/{task_id}`
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

2. **Celery for Task Queue**: <!-- TODO -->
   

3. **PostgreSQL**: <!-- TODO -->


4. **LLM Integration**: <!-- TODO -->
   

5. **Scalability**: <!-- TODO -->

---

## 🚀 Future Improvements <!-- TODO -->

1. **Enhanced Authentication**:
   - Add OAuth integration for secure GitHub API interactions.

2. **WebSocket Support**:
   - Provide real-time status updates for task progress.

3. **Frontend Integration**:
   - Build a simple dashboard for visualizing pull request analysis.

5. **Structured logging**:
   

---

## 🧪 Running Tests

1. **Install testing dependencies**:
   ```bash
   pip install pytest
   ```

2. **Run tests**:
   ```bash
   pytest
   ```

---
