import pkgutil
import sys

from discord.ext import commands

import extensions

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


if __name__ == "__main__":
    extensions = pkgutil.iter_modules(extensions.__path__)
    extensions = ['extensions.{}'.format(extension.name) for extension in extensions]

    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(settings.BOT_TOKEN)