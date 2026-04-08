import os
import pickle
import re
import nltk
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

stop_words = stopwords.words('english')
stemmer = PorterStemmer()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'model', 'vectorizer.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)
with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

# 3. إعداد التطبيق
app = FastAPI()

# تأكد من وجود مجلد static (حتى لو كان فارغاً) لتجنب الأخطاء
if not os.path.exists(os.path.join(BASE_DIR, 'static')):
    os.makedirs(os.path.join(BASE_DIR, 'static'))

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text).lower().split()
    text = [stemmer.stem(word) for word in text if not word in stop_words]
    return ' '.join(text)

# 4. الروابط (Routes)

@app.get("/")
async def home(request: Request):
    # الحل النهائي للخطأ: تمرير request كـ argument أول صريح
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"request": request}
    )

@app.post("/predict")
async def predict(tweet: str = Form(...)):
    try:
        cleaned = clean_text(tweet)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        
        # الموديل كيعطي 1 للإيجابي و 0 للسلبي (حسب تدريبك)
        result = "Positive" if prediction == 1 else "Negative"
        return {"sentiment": result}
    except Exception as e:
        return {"error": str(e)}