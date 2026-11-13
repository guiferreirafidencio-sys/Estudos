
from tokenizers import ByteLevelBPETokenizer

dados_treino = 'crepusculoDosIdolos.txt'
tokenizer = ByteLevelBPETokenizer()
tokenizer.train(files = [dados_treino],vocab_size = 52_000, min_frequency = 2, special_tokens =[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

resultado = tokenizer.encode("Hoje é um novo dia").ids
print(resultado)
print(tokenizer.decode(resultado))
tokenizer.save_model("RAM_MODEL")