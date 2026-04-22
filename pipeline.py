from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.prompts import json_prompt

pipe = pipeline("text-generation", model="google/flan-t5-base", max_length=100)
llm = HuggingFacePipeline(pipeline=pipe)

chain = json_prompt | llm

def run_pipeline(resume, jd):
    return chain.invoke({"resume": resume, "jd": jd})