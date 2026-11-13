from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="RAM_MODEL_TREINADO_100",
    tokenizer="RAM_MODEL_TREINADO_100"
)

resultado = fill_mask("A filosofia é uma <mask>.")

for previsao in resultado:
    print(previsao)