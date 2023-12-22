from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, set_seed
import torch

model = AutoModelForSeq2SeqLM.from_pretrained('Helsinki-NLP/opus-mt-zh-en', cache_dir="F:/models/huggingface/cache/").eval()
tokenizer = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-zh-en', cache_dir="F:/models/huggingface/cache/")


def translate(text):
    if len(text) > 512:
        text = text[:512].strip()
        text = text[:text.rfind("\n")]
    with torch.no_grad():
        encoded = tokenizer([text], return_tensors='pt')
        sequences = model.generate(**encoded)
        return tokenizer.batch_decode(sequences, skip_special_tokens=True)[0]


import random
import re

text_pipe = pipeline('text-generation', model='succinctly/text2image-prompt-generator')
                     # cache_dir="F:/models/huggingface/cache/")


def text_generate(input):
    seed = random.randint(100, 1000000)
    set_seed(seed)
    text_in_english = translate(input)
    for count in range(6):    
        sequences = text_pipe(text_in_english, max_length=random.randint(60, 90), num_return_sequences=8)
        list = []
        for sequence in sequences:
            line = sequence['generated_text'].strip()
            if line != text_in_english and len(line) > (len(text_in_english) + 4) and line.endswith((':', '-', '—')) is False:
                list.append(line)

        result = "\n".join(list)
        result = re.sub('[^ ]+\.[^ ]+','', result)
        result = result.replace('<', '').replace('>', '')
        if result != '':
            return result
        if count == 5:
            return result
