import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# === Project Settings ===
WORKSPACE_FOLDER = os.environ.get("WORKSPACE_FOLDER", os.path.dirname(os.path.abspath(__file__)))
ENV_MODE = os.environ.get("ENV_MODE", "production")
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "yes")

# === Paths ===
UTILITIES_PATH = os.path.join(WORKSPACE_FOLDER or "", "src", "Utilities")
TASKS_PATH = os.path.join(WORKSPACE_FOLDER or "", "src", "Tasks")
SIMULATIONS_PATH = os.path.join(WORKSPACE_FOLDER or "", "src", "Simulations")

# === Sanity check (optional)
def print_config():
    print("Workspace:", WORKSPACE_FOLDER)
    print("Environment:", ENV_MODE)
    print("Debug:", DEBUG)
    print("Utilities Path:", UTILITIES_PATH)
    print("Tasks Path:", TASKS_PATH)
    print("Simulations Path:", SIMULATIONS_PATH)

def get_config(env_var: str, default: str = None) -> str:
    """
    Get the value of an environment variable, or return None if not set.
    """
    return os.environ.get(env_var, default)

if __name__ == "__main__":
    print_config()