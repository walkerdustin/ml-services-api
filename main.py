from fastapi import Request, FastAPI
from mlModel import MLmodel

app = FastAPI()
mlModel = MLmodel()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def get_body(request: Request):
    json = await request.json()
    print(json)
    print(type(json))
    data = list(json.values())
    print(data)
    print(type(data[0]))
    print(json["volatile acidity"])
    
    prediction = mlModel.predict(data)
    print(f'{prediction = }')
    str(prediction[0].round(0))
    return str(prediction[0].round(0))

# {
#  "volatile acidity": 0.7,
#  "citric acid": 0.0,
#  "residual sugar": 1.9,
#  "chlorides": 0.076,
#  "free sulfur dioxide": 11.0,
#  "total sulfur dioxide": 34.0,
#  "density": 0.9978,
#  "pH": 3.51,
#  "sulphates": 0.56,
#  "alcohol": 9.4
# }