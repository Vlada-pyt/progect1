from flask import Flask
from utils import load_candidates

CANDIDATE = "candidatea.json"

candidates_list = load_candidates(CANDIDADET)

app = Flask(__name__)

@app.route("/")
def page_index():
    return "fgfgf"

app.run()

