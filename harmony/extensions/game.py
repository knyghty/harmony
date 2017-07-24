from discord.ext import commands


class Game:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, *game: str):
        """
        Play a game

        Keyword arguments:
        game -- The game you want to play
        """
        game: str = ' '.join(game) if game else 'with yourself'
        if game.lower() == 'thermonuclear war':
            await self.bot.say('You die.')
            await self.bot.say('Everyone dies.')
        else:
            await self.bot.say('You start playing {}.'.format(game))

    @commands.command()
    async def run(self):
        """
        Run away from the fight
        """
        await self.bot.say('You run away like a coward.')

    @commands.command(pass_context=True)
    async def whoami(self, ctx, *words: str):
        words: str = ' '.join(words) if words else None
        extra: str = ''
        if words:
            extra = ' You said: {}'.format(words)
        await self.bot.say('You\'re {}.{}'.format(ctx.message.author, extra))


def setup(bot):
    bot.add_cog(Game(bot))
