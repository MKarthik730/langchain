from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub.utils import disable_progress_bars 
disable_progress_bars()
import torch
import os
os.environ["HF_HUB_DOWNLOAD_MAX_WORKERS"] = "1" 
model_name = "mistralai/Mistral-7B-Instruct-v0.2" 



tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16,  # Changed from torch_dtype
    device_map="auto",
    low_cpu_mem_usage=True
)


pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150
)
from langchain_huggingface import HuggingFacePipeline  # New import
llm = HuggingFacePipeline(pipeline=pipe)

llm = HuggingFacePipeline(pipeline=pipe)

print(llm.invoke("Explain LangChain in simple words."))