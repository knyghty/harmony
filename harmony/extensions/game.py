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
        game: str = ' '.join(game)
        await self.bot.say('You start playing %s.' % (game if game else 'with yourself'))

    @commands.command()
    async def run(self):
        """
        Run away from the fight
        """
        await self.bot.say('You run away like a coward.')


def setup(bot):
    bot.add_cog(Game(bot))
