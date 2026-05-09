from huggingface_hub import HfApi
import os

print("Starting upload to Hugging Face via API...")
api = HfApi()

repo_id = "yandri918/agrisensa_utama"

try:
    api.upload_folder(
        folder_path=".",
        repo_id=repo_id,
        repo_type="space",
        ignore_patterns=[
            ".git", ".git/*", 
            ".venv/*", "venv/*", 
            "__pycache__/*", 
            "yield_prediction_model.pkl", 
            "creditcard.csv",
            "yield.csv"
        ]
    )
    print("✅ Uploaded successfully via Hugging Face API!")
except Exception as e:
    print(f"❌ Upload failed: {e}")
