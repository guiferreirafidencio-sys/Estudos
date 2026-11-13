
from transformers import RobertaTokenizer
from transformers import RobertaConfig
from transformers import RobertaForMaskedLM
from transformers import DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from datasets import load_dataset

# 1. TOKENIZADOR
tokenizer = RobertaTokenizer.from_pretrained(
    "RAM_MODEL",
    model_max_length=128
)

# 2. CONFIGURAÇÃO DA ARQUITETURA
config = RobertaConfig(
    vocab_size=len(tokenizer),
    max_position_embeddings=130,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1
)

# 3. CRIAÇÃO DO MODELO
model = RobertaForMaskedLM(config=config)

# 4. CARREGAMENTO DO DATASET
dataset = load_dataset(
    "text",
    data_files={"train": "crepusculoDosIdolos.txt"}
)

# 5. TOKENIZAÇÃO
def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=128
    )

tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=["text"]
)

# 6. MASCARAMENTO DOS TOKENS
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=True,
    mlm_probability=0.1
)

# 7. CONFIGURAÇÕES DO TREINAMENTO
training_args = TrainingArguments(
    output_dir="RAM_MODEL_TREINADO_100",
    num_train_epochs=10,
    per_device_train_batch_size=2,
    save_steps=500,
    save_total_limit=2,
    logging_steps=10,
    prediction_loss_only=True,
    report_to="none"
)

# 8. TRAINER
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=tokenized_dataset["train"]
)

# 9. TREINAMENTO
trainer.train()

# 10. SALVAR MODELO E TOKENIZADOR
trainer.save_model("RAM_MODEL_TREINADO_100")
tokenizer.save_pretrained("RAM_MODEL_TREINADO_100")

print("Treinamento concluído!")
