import pandas as pd
import torch
from torch.utils.data import AutTokenizer
from typing import List, Dict, Union
from typing import Any, TypeVar

import pandas as pd
import pickle 


MODEL_NAME: str = ''
  
  
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCasualLM.from_pretrained(MODEL_NAME).cuda()
#Resize model  for tokenizer size 
n_tokens: int = len(tokenizer)
model.resize_token_embeddings(n_tokens)


def _generate_prompt(instruction, input=None):
    if input:
        return f"""Poniżej znajduje się instrukcja opisująca zadanie, połączona z danymi wejściowymi, które zapewniają dalszy konktekst. Napisz odpowiedź, która odpowiednio odpowie na pytanie.

### Instruction:
{instruction}

### Input:
{input}

### Response:"""
      
     
    
data = pd.read_csv("alpaca_dolly.csv")
dict_data = pd.DataFrame.to_dict(data, orient='records' )


example = data.iloc[-16, :]
print(f"Valueation for {example.instruction} \n\n\n  {example.input}\n\n")
evaluate(instruction = example.instruction, 
         input = example.input)  
      
      
