import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

# Import core analysis logic
from .core.analyzer import analyze_repository

app = FastAPI(
    title="CommitIQ API",
    description="AI-powered tool for Git commit message analysis."
)

class CommitAnalysis(BaseModel):
    hash: str
    author: str
    message: str
    score: int  
    feedback: str 

class RepositoryReport(BaseModel):
    repo_path: str
    total_commits: int
    average_score: float
    analysis_results: List[CommitAnalysis]

@app.get("/analyze", response_model=RepositoryReport)
async def analyze_repo(repo_path: str = ".", limit: int = 10):
    """
    Analyzes commit messages of a local Git repository.
    
    Args:
        repo_path: Path to the local repository (e.g., '.', '..', or absolute path).
        limit: Maximum number of commits to analyze.
        
    Returns:
        A structured report on the commit analysis.
    """

    if not os.path.isdir(repo_path):
        raise HTTPException(status_code=400, detail="The specified path is not a directory.")
    
    try:
 
        report_data = analyze_repository(repo_path, limit)
        scores = [c['score'] for c in report_data]
        avg_score = sum(scores) / len(scores) if scores else 0
        return RepositoryReport(
            repo_path=os.path.abspath(repo_path),
            total_commits=len(report_data),
            average_score=round(avg_score, 2),
            analysis_results=report_data
        )

    except Exception as e:
        print(f"Error during analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error during analysis.")