import random

from discord.ext import commands

import sqlalchemy as sa

from db.base import Base


class Player(Base):
    __tablename__ = 'players'

    user_id = sa.Column(sa.String, primary_key=True)
    user_name = sa.Column(sa.String, default='')
    toughness = sa.Column(sa.Integer, default=9)
    intelligence = sa.Column(sa.Integer, default=9)
    tact = sa.Column(sa.Integer, default=9)
    speed = sa.Column(sa.Integer, default=9)
    hit_points = sa.Column(sa.Integer, default=0)
    enemy_hit_points = sa.Column(sa.Integer, default=0)

    def reset(self):
        self.hit_points = self.toughness + self.intelligence + self.tact + self.speed
        self.enemy_hit_points = self.toughness + self.intelligence + self.speed


class Game:

    def __init__(self, bot):
        self.bot = bot
        self.battles = {}

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
        await self.bot.say("You're {}.{}".format(ctx.message.author, extra))

    @commands.command(pass_context=True)
    async def makechar(self, ctx):
        session = self.bot.Session()
        try:
            player = session.query(Player).filter(Player.user_id == ctx.message.author.id)[0]
            status = 'existing'
        except IndexError:
            player = Player(user_id=ctx.message.author.id, user_name=ctx.message.author.display_name)
            status = 'new'

        session.add(player)
        session.commit()
        await self.bot.say("```\n{}'s {} player:\nTOUGHNESS: {}\nINTELLIGENCE: {}\nTACT: {}\nSPEED: {}```".format(
            player.user_name,
            status,
            player.toughness,
            player.intelligence,
            player.tact,
            player.speed
        ))

    @commands.command(pass_context=True)
    async def battle(self, ctx):
        session = self.bot.Session()
        try:
            player = session.query(Player).filter(Player.user_id == ctx.message.author.id)[0]
        except IndexError:
            await self.bot.say("You don't have a character. Make one with `!makechar`.")
            return

        if player.hit_points <= 0 or player.enemy_hit_points <= 0:
            player.reset()
            if player.user_id in self.battles:
                del self.battles[player.user_id]

        attack = random.randint(1, player.toughness)
        defense = random.randint(1, 18-player.speed)

        player.hit_points -= defense
        player.enemy_hit_points -= attack

        session.add(player)
        session.commit()
        combatant = '{:30s} {:2d}'
        content = [
            '```',
            combatant.format(player.user_name, player.hit_points),
            combatant.format('Monster', player.enemy_hit_points),
            '```'
        ]
        if player.user_id in self.battles:
            message = await self.bot.edit_message(self.battles[player.user_id], '\n'.join(content))
        else:
            message = await self.bot.say('\n'.join(content))
        self.battles[player.user_id] = message


def setup(bot):
    bot.add_cog(Game(bot))
