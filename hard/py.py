import torch
from transformers import AutoTokenizer, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from mambapy.lm import LM, MambaConfig

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
tokenizer.pad_token = tokenizer.eos_token

# Load and tokenize the dataset
with open('inst.txt', 'r') as f:
    lines = f.readlines()

inputs = tokenizer(lines, return_tensors='pt', padding=True, truncation=True)

# Define the model configuration
config = MambaConfig(d_model=16, n_layers=2, vocab_size=tokenizer.vocab_size)

# Initialize the model
model = LM(config)

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10,
    save_total_limit=2,
    prediction_loss_only=True,
)

# Define data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=inputs['input_ids'],
)

# Start training
trainer.train()
