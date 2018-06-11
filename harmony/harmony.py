import pkgutil

from discord.ext import commands

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

import extensions
from conf import settings
from db.base import Base


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.engine = sa.create_engine(settings.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        super().__init__(*args, **kwargs)


bot = Bot(command_prefix='!', description='Just a utility bot')


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

    Base.metadata.create_all(bot.engine)
    bot.run(settings.BOT_TOKEN)
