import random
import sys

from discord.ext import commands

try:
    from conf import settings
except ImportError:
    sys.exit('Before you can run harmony, you must follow the instructions in `conf/settings_template.py`')


bot = commands.Bot(command_prefix='!', description='Just a utility bot')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def roll(dice : str):
    try:
        num_dice, num_faces = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format is XdY')
        return

    if num_dice > 20 or num_faces > 1000:
        await bot.say('Max 20 dice and 1000 faces')
        return

    if num_dice < 1 or num_faces < 1:
        await bot.say('Stick to positive numbers')
        return

    total = sum((random.randrange(1, num_faces) for _ in range(int(num_dice))))
    await bot.say(str(total))


bot.run(settings.BOT_TOKEN)