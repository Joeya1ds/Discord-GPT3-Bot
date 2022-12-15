import discord
from discord.ext import commands
import openai

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)
openai.api_key = "OPENAI-API-KEY-HERE"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ask(ctx, *, prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.8,
        top_p=0.8,
    )
    moderate = openai.Moderation.create(
        input=prompt,
    )
    naughtyask = moderate['results'][0]['flagged']
    if str(naughtyask) == "False":
        await ctx.send(response['choices'][0]['text'])
    else:
        await ctx.send("I cannot respond to what you have said, it has been flagged by the moderation API.")

bot.run('BOT-TOKEN-HERE')
