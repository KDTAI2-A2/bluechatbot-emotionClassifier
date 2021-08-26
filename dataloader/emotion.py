import pandas as pd

import torch
import torch.nn as nn
from torch.utils.data import Dataset # 데이터로더

from kogpt2_transformers import get_kogpt2_tokenizer
from kobert_transformers import get_tokenizer

# Dataloader For koGPT2
class EmotionAutoRegressiveDataset(Dataset):
  """Emotion Auto Regressive Dataset"""

  def __init__(self,
               file_path = "../dataset/corpus.xlsx",
               n_ctx = 1024
               ):
    self.file_path = file_path
    self.data =[]
    self.tokenizer = get_kogpt2_tokenizer()


    bos_token_id = [self.tokenizer.bos_token_id]
    eos_token_id = [self.tokenizer.eos_token_id]
    pad_token_id = [self.tokenizer.pad_token_id]

    corpus = pd.read_excel(self.file_path)

    def lineTokenizer(line):
      index_of_words = bos_token_id + self.tokenizer.encode(line) + eos_token_id
      return index_of_words
      
    def padAdder(index_of_words):
      pad_token_len = n_ctx - len(index_of_words)
      index_of_words += pad_token_id * pad_token_len
      return index_of_words
      
    self.data = list((corpus["사람문장1"].apply(lineTokenizer) + corpus["시스템응답1"].apply(lineTokenizer)).apply(padAdder))

  def __len__(self):
    return len(self.data)

  def __getitem__(self,index):
    item = self.data[index]
    return item

# Dataloader for koBERT, koELECTRA
class EmotionTextClassificationDataset(Dataset):
  """Emotion Text Classification Dataset"""
  def __init__(self,
               file_path = "../dataset/corpus_labeled.xlsx",
               num_label = 58,
               device = 'cpu',
               max_seq_len = 512, # KoBERT max_length
               tokenizer = None
               ):
    self.file_path = file_path
    self.device = device
    self.data =[]
    self.tokenizer = tokenizer if tokenizer is not None else get_tokenizer()

    corpus = pd.read_excel(self.file_path)
      
    def lineTokenizer(line):
      index_of_words = self.tokenizer.encode(line)
      token_type_ids = [0] * len(index_of_words)
      attention_mask = [1] * len(index_of_words)
      
      # Padding Length
      padding_length = max_seq_len - len(index_of_words)

      # Zero Padding
      index_of_words += [0] * padding_length
      token_type_ids += [0] * padding_length
      attention_mask += [0] * padding_length
      
      data = {
              'input_ids': torch.tensor(index_of_words).to(self.device),
              'token_type_ids': torch.tensor(token_type_ids).to(self.device),
              'attention_mask': torch.tensor(attention_mask).to(self.device),
             }
      return data
      
    def labelAdder(pair):
        pair[0]['labels'] = torch.tensor(pair[1]).to(self.device)
        return pair[0]
      
    self.data = list(map(labelAdder, zip(corpus["사람문장1"].apply(lineTokenizer), corpus["감정_레이블"])))

  def __len__(self):
    return len(self.data)
    
  def __getitem__(self,index):
    item = self.data[index]
    return item

if __name__ == "__main__":
  dataset = EmotionAutoRegressiveDataset()
  dataset2 = EmotionTextClassificationDataset()
  print(dataset)
  print(dataset2)