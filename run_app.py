import subprocess
import threading
import time
import os

def run_backend():
    subprocess.run([
        "uvicorn", "backend.main:app",
        "--host", "0.0.0.0",
        "--port", "8000"
    ])

if __name__ == "__main__":
    # Start FastAPI in background
    threading.Thread(target=run_backend, daemon=True).start()

    # Give backend time to start
    time.sleep(3)

    # Run Streamlit dashboard
    os.system("streamlit run dashboard/app.py --server.port=8501 --server.address=0.0.0.0")
