# https://huggingface.co/docs/huggingface_hub/quick-start

# 1. download files
# For example, to download the Pegasus model configuration file:
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="google/pegasus-xsum", filename="config.json")


# 2. Authentication

# 2.1 Login command
# huggingface-cli login

# 2.2 Environment variable
# The environment variable HF_TOKEN can also be used to authenticate yourself.
# This is especially useful in a Space where you can set HF_TOKEN as a Space secret.

# 2.3 Method parameters
# from transformers import whoami
# user = whoami(token=...)


# 3. Create a repository
from huggingface_hub import HfApi
api = HfApi()
api.create_repo(repo_id="super-cool-model")


# 4. Upload files
from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="/Users/sophia/GitHub/cookbook-ai/huggingface/README.md",
    path_in_repo="HF_README.md",
    repo_id="yuxiang204/super-cool-model",
)

