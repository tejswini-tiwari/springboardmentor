from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pickle as pkl
import pandas as pd

app = FastAPI()

model = pkl.load(open("../model/pipe.pkl", "rb"))

@app.get("/",response_class=HTMLResponse)
def home():
    return """
        <html>
            <head>
                <title>IPL Win Predictor</title>
            </head>
            <body>
                <h1>🏏 IPL Win Predictor API</h1>
                <p>Frontend:</p>
                <a href="http://localhost:8501">Open App</a>
            </body>
        </html>
    """

@app.post("/predict")

def predict(data: dict):

    df = pd.DataFrame({
        'batting_team':[data["batting_team"]],
        'bowling_team':[data["bowling_team"]],
        'city':[data["city"]],
        'runs_left':[data["runs_left"]],
        'balls_left':[data["balls_left"]],
        'wickets':[data["wickets"]],
        "total_runs_x":[data["target"]],
        "cur_run_rate":[data["cur_run_rate"]],
        "req_run_rate":[data["req_run_rate"]]
    })

    result = model.predict_proba(df)

    return {
        "loss": float(result[0][0]),
        "win": float(result[0][1])
    }
