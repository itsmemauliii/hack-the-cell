FROM python:3.10-slim AS backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend .

FROM python:3.10-slim AS dashboard
WORKDIR /app/dashboard
COPY dashboard/requirements.txt .
RUN pip install -r requirements.txt
COPY dashboard .

# To run backend
# docker run -p 8000:8000 backend uvicorn main:app --host 0.0.0.0 --port 8000

# To run dashboard
# docker run -p 8501:8501 dashboard streamlit run app.py --server.port=8501 --server.address=0.0.0.0
