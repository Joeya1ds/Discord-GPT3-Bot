import os
import openai
import json
import discord
from discord import app_commands

with open('./config.json') as data:
    config = json.load(data)

path = config['LOG_PATH']
openai.api_key = config['OPENAI_API_KEY']

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your prompts!'))
        if not self.synced:
            await tree.sync()
            self.synced = True
        print('Logged in as:')
        print(str(self.user.name) + ", " + str(self.user.id))
        print("Created by Joeyy#4628. The most up-to-date code can be found on github: https://github.com/Joeya1ds/Discord-GPT3-Bot")
        print('--------------------------------------------------------------------------------------------------------------------')


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name="ask", description="Ask the AI bot a question!")
async def ask(interaction: discord.Interaction, prompt: str):
    username = interaction.user.name
    user = interaction.user.id

    # Moderation API flagging and response creation
    moderate = openai.Moderation.create(
        input=prompt,
    )
    moderateresult = moderate['results'][0]['flagged']
    if str(moderateresult) == "False":
        openairesponse = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.8,
            top_p=0.8,
        )
        await interaction.response.send_message(openairesponse['choices'][0]['text'])
    else:
        await interaction.response.send_message("I cannot respond to what you have said, it has been flagged by the Moderation API.")
        print("User " + str(username) + " with ID: " + str(user) + " has had a prompt flagged by the Moderation API. Consider checking UserLogs.")

    # Logging User Messages inside text file
    if not os.path.exists(path + "/" + str(user)):
        print("User " + str(username) + " with ID: " + str(user) + " does not have a log file created. Creating.")
        os.makedirs(path + "/" + str(user))
    with open(path + "/" + str(user) + "/" + str(user) + ".txt", "a") as f:
        f.write("User " + str(username) + ' wrote: "' + prompt + '" using '  + str(openairesponse['usage']['total_tokens']) + " tokens." + "\n")


client.run(config['DISCORD_BOT_TOKEN'])
