# Air Quality AI
Educational Flask prototype: synthetic urban sensor readings, backward Monte Carlo particle search, candidate source ranking and CSV export. No API keys needed. The map is a fictional city coordinate grid, not a geographic map. PM2.5 is simulated; other pollutants are illustrative proxies. Scores are relative proximity weights, not real source probabilities. No official AQI, live sensors, historical storage or physical validation. Wind is a constant direction toward which air travels, not meteorological wind-from convention. The model uses arbitrary spatial units and is not a calibrated dispersion model.

## Windows / VS Code
Extract ZIP, open the AirQualityAI folder in VS Code, then Terminal > New Terminal. Run:

    python -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    .\.venv\Scripts\python.exe app.py

Open http://127.0.0.1:5000 in browser. Stop with Ctrl+C.

## Tests
    .\.venv\Scripts\python.exe -m unittest discover -s tests

## Deployment
Upload files to GitHub (exclude .venv). Render Python web service: build `pip install -r requirements.txt`; start `gunicorn app:app`. Hosting terms may vary.

## Pro interface
New responsive dashboard styling, navigation, sensor search and read-only backend console at /monitor. Health and diagnostic endpoints report real application/model status for the synthetic scenario. No authentication or database is included; use this as a public academic demonstration only.
