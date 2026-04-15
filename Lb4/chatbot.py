from ollama import chat
import time

models = ["qwen3.5:0.8b", "gemma3:4b"]

question = "What is artificial intelligence?"

filename = "result_a_chatbot.txt"

with open(filename, "w", encoding="utf-8") as f:
    for model in models:
        response = chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            keep_alive=0
        )

        answer = response["message"]["content"]

        f.write(f"=== {model} ===\n")
        f.write(answer + "\n\n")

        time.sleep(10)

print(f"Збережено: {filename}")