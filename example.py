#!/usr/bin/env python
# encoding: utf-8

from torchctr.datasets import MovieLens, Titanic
from torchctr.models import LogisticRegression, FactorizationMachine, FieldAwareFactorizationMachine
from torchctr.trainer import Trainer

dataset = MovieLens()
# dataset = Avazu()
# dataset = Titanic()
dataset.build_data()

dims = dataset.feature_dims
print("dataset dims", dims)

# model = LogisticRegression(dims)
# model = FactorizationMachine(dims, embed_dim=4)
model = FieldAwareFactorizationMachine(dims, embed_dim=4)

hyper_parameters = {
    "batch_size": 32,
    "device": "cpu",
    "learning_rate": 0.01,
    "weight_decay": 1e-6,
    "epochs": 1,
    "metrics": ["auc"],
}

trainer = Trainer(model, dataset, hyper_parameters)
trainer.train()
trainer.save("test.pt")
