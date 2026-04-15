from ollama import chat
import time

models = ["qwen3.5:0.8b", "gemma3:4b"]

image_path = "photo.jpg"

filename = "result_c_multimodal.txt"

with open(filename, "w", encoding="utf-8") as f:
    for model in models:
        response = chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Describe what is shown in this image.",
                    "images": [image_path]
                }
            ],
            keep_alive=0
        )

        text = response["message"]["content"]

        f.write(f"=== {model} ===\n")
        f.write(text + "\n\n")

        time.sleep(10)

print(f"Збережено: {filename}")