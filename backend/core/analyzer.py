import git
import random
from typing import List, Dict, Any

def _simulate_ai_analysis(message: str) -> Dict[str, Any]:
    """
    SIMULATION of an external LLM API call (e.g., OpenAI) to score a commit.
    
    This function simulates the AI behavior based on message formatting.
    """
    
    message_lower = message.strip().lower()

    is_conventional = message_lower.startswith(('feat:', 'fix:', 'docs:', 'chore:'))
    is_short = len(message) < 70
    
    if is_conventional and is_short:
        score = random.randint(8, 10)
        feedback = "Excellent! Clear intent and concise formatting (Conventional Commit style)."
    elif is_conventional:
        score = random.randint(6, 8)
        feedback = "Good action verb used, but the message might be slightly too long."
    elif len(message_lower.split()) < 3:
        score = random.randint(1, 3)
        feedback = "Too short! Message lacks context and clarity. Score reduced."
    else:
        score = random.randint(4, 6)
        feedback = "The message lacks a clear action verb or formatting prefix. Needs improvement for readability."
        
    return {
        "score": score,
        "feedback": feedback
    }


def analyze_repository(repo_path: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Extracts commits from a Git repository and analyzes them using the simulated AI function.
    """
    
    results = []
    
    try:
       
        repo = git.Repo(repo_path, search_parent_directories=True)

        commits = repo.iter_commits(max_count=limit)
        
        for commit in commits:
            message = commit.message.strip()
            
            ai_data = _simulate_ai_analysis(message)
            
            results.append({
                "hash": commit.hexsha,
                "author": commit.author.name,
                "message": message,
                "score": ai_data['score'],
                "feedback": ai_data['feedback']
            })
            
    except git.InvalidGitRepositoryError:
  
        raise Exception(f"Path '{repo_path}' is not a valid Git repository.")
    except Exception as e:

        raise Exception(f"Error during Git log extraction: {e}")
        
    return results