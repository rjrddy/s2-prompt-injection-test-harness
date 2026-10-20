"""Download the small public instruction model for actual agent attack evaluation."""
from pathlib import Path
from huggingface_hub import snapshot_download
root=Path(__file__).resolve().parents[1]
snapshot_download('HuggingFaceTB/SmolLM2-135M-Instruct',local_dir=root/'.cache/model',allow_patterns=['*.json','*.safetensors','*.txt','*.jinja'])
print('Open instruction model ready')
