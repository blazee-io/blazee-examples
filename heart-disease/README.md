# Heart Disease Random Classifier

In this example we use the Heart Disease data from <https://www.kaggle.com/ronitf/heart-disease-uci>

We train a pipeline composed of a DictVectorizer, RobustScaler and a RandomForest classifier and deploy it on Blazee.

While this model is used in production, we found a SGDClassifier that performed better and deployed it to Blazee as well.

This example demonstrates how you can simply manage the lifecycle of your models in production and A/B test them with Blazee.

## Deployment

Model is trained and deployed in the Jupyter Notebook

## Predictions

Predictions can be accessed from anywhere using the HTTP API

```shell
>> curl -H "X-Api-Key: YOUR-API-KEY" -d '{"age": 48, "sex": 1.0, "cp": 0.0, "trestbps": 130.0, "chol": 256.0, "fbs": 1.0, "restecg": 0.0, "thalach": 150.0, "exang": 1.0, "oldpeak": 0.0, "slope": 2.0, "ca": 2.0, "thal": 3.0}' https://api.blazee.io/v1/models/989da70d-ec73-43ce-a41f-d70a2446fef0/predict
{
    "prediction": 1,
    "probas": [0.12, 0.88]
}
```
