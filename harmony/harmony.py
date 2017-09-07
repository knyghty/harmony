import pkgutil

from discord.ext import commands

import extensions
from conf import settings


bot = commands.Bot(command_prefix='!', description='Just a utility bot')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


if __name__ == '__main__':
    for extension in ('extensions.{}'.format(ext.name) for ext in pkgutil.iter_modules(extensions.__path__)):
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(settings.BOT_TOKEN)
