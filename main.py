from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mlModel import MLmodel

app = FastAPI()
mlModel = MLmodel()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def get_body(request: Request):
    print(request)
    json = await request.json()
    print(json)
    # print(json["volatile acidity"])
    print(type(json))
    data = list(json.values())
    print(data)
    print(type(data[0]))
    
    prediction = mlModel.predict(data)
    print(f'{prediction = }')
    value = str(int(prediction[0].round(0)))
    return value

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