# 🧠 CommitIQ: AI-Powered Commit Message Analyzer



**CommitIQ** is a modern Python backend service built with **FastAPI** designed to analyze the quality, clarity, and adherence to best practices of Git commit messages. It uses an AI model (simulated, ready for LLM integration) to provide objective feedback and a quality score, helping teams maintain high standards in their code history.

## ✨ Features and Value

| Feature | Description |
| :--- | :--- |
| **AI Quality Scoring** | Provides a score (0-10) and structured feedback for each commit message, ensuring clarity and intent. |
| **FastAPI Backend** | Offers a clean, modern, and high-performance API endpoint (`/analyze`) for easy integration with frontend dashboards or CI/CD pipelines. |
| **Git Log Extraction** | Utilizes **GitPython** for efficient retrieval and parsing of commit history from any local repository. |
| **Structured Output** | Returns detailed analysis in a standard JSON format, ready for data visualization. |

---

## 🛠️ Quick Setup

### Prerequisites

* Python 3.9+
* **Git** installed on your system.
* A local Git repository for testing (CommitIQ itself is a good candidate!).

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/ewhx-dev/CommitIQ.git](https://github.com/ewhx-dev/CommitIQ.git)
    cd CommitIQ
    ```
2.  Install dependencies (FastAPI, Uvicorn, GitPython):
    ```bash
    pip install -r requirements.txt
    ```

### Running the Service

1.  Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn backend.main:app --reload
    ```
    *The server will be accessible at `http://127.0.0.1:8000`.*

### Testing the API

Open your browser at `http://127.0.0.1:8000/docs` to access the Swagger UI interface and test the `GET /analyze` endpoint.

**Example Call (using the current repository):**

-   **Endpoint:** `http://127.0.0.1:8000/analyze`
-   **Query Parameter:** `repo_path=.`

---

## ⚙️ Project Structure

The project follows a standard backend service structure with a clear separation of concerns:

* `backend/main.py`: The FastAPI application entry point, defining the API route.
* `backend/core/analyzer.py`: Contains the core logic for **Git log extraction** and the **simulated AI analysis**.
* `requirements.txt`: Lists all Python dependencies (`fastapi`, `GitPython`, etc.).

---

## 🚀 Future Integration

This project is designed to be easily upgraded:

1.  **External LLM Integration:** Replace the `_simulate_ai_analysis` function in `analyzer.py` with an actual API call (using libraries like `openai` or `anthropic`) to leverage powerful models for deep qualitative analysis.
2.  **Frontend Dashboard:** Build a companion **React/Next.js** frontend to visualize the average score, author contribution, and the distribution of scores across the project timeline.

---

**Developed by [ewhx-dev]**