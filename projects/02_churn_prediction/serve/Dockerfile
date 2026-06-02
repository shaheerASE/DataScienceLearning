# 🟤 Dockerfile — package the API so it runs IDENTICALLY anywhere
# ================================================================
# "It works on my machine" is the oldest excuse in software. Docker kills it:
# it bundles the code + Python + every dependency into one portable "container".
# The same container runs on your laptop, a colleague's PC, or a cloud server.
#
# NOTE on "build context": Docker can only COPY files inside the folder you give
# it as context. The trained model lives one level up from serve/, so we use the
# PROJECT folder as the context and point to this Dockerfile with -f.
#
# Build (run from the repo root):
#   docker build -t churn-api -f projects/02_churn_prediction/serve/Dockerfile projects/02_churn_prediction
# Run:
#   docker run -p 8000:8000 churn-api
# Then open http://localhost:8000/docs

# 1. Start from a small official Python image.
FROM python:3.11-slim

# 2. Set a working directory inside the container.
WORKDIR /app

# 3. Install dependencies first (Docker caches this layer for faster rebuilds).
COPY serve/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the app code and the trained model into the container.
COPY serve/app.py .
COPY model/ ./model/

# 5. Document the port the API listens on.
EXPOSE 8000

# 6. The command that starts the API when the container runs.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
