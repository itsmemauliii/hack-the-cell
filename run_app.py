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

# Start FastAPI in a background thread
threading.Thread(target=run_backend, daemon=True).start()

# Wait for backend to start
time.sleep(3)

# Launch Streamlit
os.system("streamlit run dashboard/app.py --server.port=8501 --server.address=0.0.0.0")
