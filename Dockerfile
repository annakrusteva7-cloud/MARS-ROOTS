FROM python:3.12-slim

# Non-root user
RUN useradd -m -u 1000 marsuser
WORKDIR /app
COPY --chown=marsuser:marsuser . .

RUN pip install --no-cache-dir -r requirements.txt

USER marsuser

CMD ["python", "run_simulation.py"]
