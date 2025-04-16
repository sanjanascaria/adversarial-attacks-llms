
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

### 🔹 `src/run_prompting.py`
Main script that takes a user query (from stdin), loads the selected LLM model via `ollama`, and optionally invokes tools/functions for complex reasoning. Outputs are logged in a CSV format for later analysis.

### 🔹 `outputs/*.csv`
CSV files containing structured outputs from different LLMs, including:

- User query
- Whether a tool was invoked
- Final model response
- Output flags

These files are raw logs of LLM behavior during experiments.

### 🔹 `prompts/`
Adversarial or challenging prompts used to test the limits of LLMs. Includes multilingual examples to evaluate model robustness in non-English contexts.

---

## 🛠️ How to Run

1. **Install dependencies:**

```bash
pip install -r requirements.txt
