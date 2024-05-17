from cleanit import preprocess_text
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from cleanit import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


with open('model.pkl', 'rb') as file:
    CV_pipe, CV, LR1 = pickle.load(file)

class TextRequest(BaseModel):
    text: str

@app.post("/evaluate_text/")
async def evaluate_text_endpoint(text_request: TextRequest):
    text = text_request.text
    cleaned_text = preprocess_text(text)
    transformed_text = CV.transform([cleaned_text])
    prediction = LR1.predict(transformed_text)

    if prediction[0] == 1:
        return {"detail": "Offensive"}
    else:
        return {"detail": "Not Offensive"}
