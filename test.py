from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from cleanit import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

with open('english_model.pkl', 'rb') as file:
    CV, LR1 = pickle.load(file)

@app.post("/evaluate_text/{text}")
async def evaluate_text_endpoint(text: str):
    try:
        cleaned_text = preprocess_text(text)
        transformed_text = CV.transform([cleaned_text])
        prediction = LR1.predict(transformed_text)

        if prediction[0] == 1:
            return {"detail": "Offensive"}
        else:
            return {"detail": "Not Offensive"}
    except Exception as e:
        return {"detail": "Error", "message": str(e)}
