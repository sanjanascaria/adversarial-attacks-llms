# The Python scripts that were used to trigger harmful behaviour. 

Methodology:
- For each harmful behaviour (antisemitism and racism), LLM, and language, the script was executed 100 times, keeping the non-deterministic nature of LLMs in mind.
- For `llama3.1:70b` and `qwen2.5:72b`, the code was executed only 10 times for English, German and French, and 4 times in Malayalam.
- This was done due to hardware and time restrictions - the bigger models took too long for each execution, and the experiements were therefore shortened. 
