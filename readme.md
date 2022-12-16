# Discord GPT-3 Bot

This Discord bot is a Python script that uses the OpenAI API to generate responses to prompts given by users in a Discord server. It has a command called "ask" which users can invoke by typing "/ask" followed by their prompt in a Discord server. The bot will then generate a response to the prompt and send it back to the user. The bot also has a moderation feature which uses the OpenAI Moderation API to flag inappropriate prompts and prevent the bot from responding to them. In addition, the bot logs all prompts and responses in text files organized by user. To use the bot, you will need to obtain an API key from OpenAI and a token for your Discord bot. You will also need to specify the file path to the directory where you want the user logs to be saved.

You will NEED to add a folder to place the UserLogs. Ensure the path to that folder is the one used for "FilePath". I recommend placing the folder inside the same folder as the scripts.

You will also need to install the following packages using the CLI:

pip install discord.py, 
pip install openai
