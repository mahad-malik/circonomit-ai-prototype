import google.generativeai as genai

genai.configure(api_key="API key")

models = list(genai.list_models())
for model in models:
    print(model.name)
