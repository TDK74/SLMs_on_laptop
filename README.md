# SLMs_on_laptop
Run Small Language Models (Gemma2 2b, Llama 3.1 8b, Mistral 7B, phi3.5 3.8b, Qwen2.5 0.5b) on a laptop.

* Based on the guide from this site:

<https://www.dfrobot.com/blog-14068.html>

There were no Python script examples, but I created several, so that I could download and run different SLMs with scripts rather than manually from the command line in Powershell or cmd.

## 

# Setup Environment
* Laptop: Fujitsu Celcius H780
* Operating System: Windows 10 Pro x64
* Software: Python 3.10, 3.11 (virtual env - workspace), 3.12 (Anaconda)
* Environment: slmpy311 (virtual env)
* SL models: gemma2-2b-q4, llama3.1-8b-q4, mistral-7B-q4, phi3.5-3.8b-q4, qwen2.5-0.5b-q4

See **_commands.txt_** and **_pip_freeze.txt_** for more details if interested.

## Note

There are Pyton script files with different levels of complexity as I improved and developed my code.

Basic examples branch- first step should be to run **ollama_run_stop.py** and then the selected model file.

Improved examples branch - added a function and "try... except" in it, but it is also valid to run **ollama_run_stop.py** first and then the selected model fte file.

The master branch has the final versions.

The branches are left unmerged into the master, so that the files of these different levels can be easily distinguished.
