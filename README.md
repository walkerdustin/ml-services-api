# backend API for a ml Service
>the API is live  
[Frontend]( https://predict-red-wine-quality-with-ml.netlify.app  )  
[Backend](https://predict-wine-quality-api.herokuapp.com/docs#/default/get_body_predict_post)

backend with Python FastApi https://fastapi.tiangolo.com/

API for a ML model, that predicts the quality of a wine (from 0 to 10) using some chemical attributes of the wine



## commands

Run server

```bash
uvicorn main:app --reload
```

## API
```bash
https://predict-wine-quality-api.herokuapp.com/predict
```

POST request with body
```
{
 "volatile acidity": 0.7,
 "citric acid": 0.0,
 "residual sugar": 1.9,
 "chlorides": 0.076,
 "free sulfur dioxide": 11.0,
 "total sulfur dioxide": 34.0,
 "density": 0.9978,
 "pH": 3.51,
 "sulphates": 0.56,
 "alcohol": 9.4
}
```

