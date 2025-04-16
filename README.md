
---

## 📌 Project Description

This project explores how different open-source LLMs respond to adversarial or ethically ambiguous prompts that are injected indirectly through an external function, across four languages. 

Models tested include:
- `llama3.1:70b`
- `llama3.1:8b`
- `llama3.2:1b`
- `mistral-nemo:12b`
- `granite3.1-dense:2b`
- `granite3.1-moe:1b`
- `granite3.1-moe:3b`
- `qwen2.5:1.5b`
- `qwen2.5:7b`
- `qwen2.5:72b`
- `smollm2:1.7b`


---

## 🧪 Contents

### 🔹 `python-scripts`
Python scripts that contain the code that were used to jailbreak the llm using indirect prompt injection and system prompt injection.

### 🔹 `outputs/*.csv`
CSV files containing structured outputs from different LLMs.
These files are raw logs of LLM behavior during experiments.

### 🔹 `/adversarial-prompts-all-langugaes.md/`
The adversarial prompts designed to cause a jailbreak. Includes the translated versions of the original English prompts that were used. 

---

