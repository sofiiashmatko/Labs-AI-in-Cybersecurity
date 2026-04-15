from ollama import chat
import time

models = ["qwen3.5:0.8b", "gemma3:4b"]

prompt = "Write a short text about healthy lifestyle."

filename = "result_b_generation.txt"

with open(filename, "w", encoding="utf-8") as f:
    for model in models:
        response = chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            keep_alive=0
        )

        text = response["message"]["content"]

        f.write(f"=== {model} ===\n")
        f.write(text + "\n\n")

        time.sleep(10)

print(f"Збережено: {filename}")