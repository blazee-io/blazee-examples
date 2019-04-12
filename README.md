# Blazee Examples

This repo contains examples of how to use Blazee.io to deploy machine learning models to the cloud with different ML frameworks.

Each folder contains a single model.

## [Keras] ImageNet VGG 16

Deploys the raw [VGG16 image classifier trained on ImageNet](https://keras.io/applications/#vgg16) that ships with Keras.

Framework: Keras
Model Type: Classification
Problem Type: Vision

## [Keras] SklearnClassifier

Deploys a [Sklearn KerasClassifier](https://keras.io/scikit-learn-api/) trained on the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database) problem from Kaggle.

Framework: Sklearn/Keras
Model Type: Classification
Problem Type: Tabular

## [PyTorch] CIFAR10 Classifier

Deploys a (barely trained) Image Classifier neural network trained on CIFAR10.

Framework: PyTorch
Model Type: Classification
Problem Type: Vision

## [SkLearn] RandomForestClassifier

Deploys a Random Forest Classifier trained on the [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) dataset from Kaggle.
In this example, we also train a second version of the model using a SGDClassifier, and show how to simply manage the lifecycle of your models with Blazee.

Framework: SkLearn
Model Type: Classification
Problem Type: Tabular
