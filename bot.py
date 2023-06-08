import lightbulb
import hikari
import random

bot = lightbulb.BotApp(
    token='$DiscordToken$',
    # default_enabled_guilds=[$YourGuild$, $AnotherOneOfYourGuilds$] # first is my server. second is $SomeoneElsesServer$ server
    # IMPORTANT BECAUSE YOU'LL FORGET: bot status stuff is at the bottom of the program
)


eightball = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.',
             'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
             'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
             'Concentrate and ask again.', 'Dont count on it.', 'My reply says no.', 'My sources say no.',
             'Outlook not so good.', 'Very doubtful.']

blocked_words = ["idiot"]

white = '#FFFFFF'
yellow = '#FFFF00'
pink = '#FFC0CB'
dark_purple = '#301934'
red = '#FF0000'


@bot.command
@lightbulb.command('ping', 'Says pong! (And the bots latency)')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f'Pong! *Anyway...* The latency is: {bot.heartbeat_latency*1000:.2f}ms')


@bot.command
@lightbulb.option('second', 'The second number', type=int)
@lightbulb.option('first', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.first + ctx.options.second)


@bot.command
@lightbulb.option('sentence', 'The word/sentence you want to uwu-ify', type=str)
@lightbulb.command('uwu', 'Uwu-ify a word/sentence')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    string = ctx.options.sentence
    string = string.replace('r', 'w')
    string = string.replace('l', 'w')
    await ctx.respond(string)


@bot.command
@lightbulb.option('sentence', 'The word/sentence you want to nerd-ify', type=str)
@lightbulb.command('nerd', 'Nerd-ify a word/sentence')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    string = ctx.options.sentence
    string = string.replace('s', 'sh')
    string = string.replace('c', 'sh')
    string = string + ' :nerd:'
    await ctx.respond(string)


@bot.command
@lightbulb.command("patch", "Sends an image of the current patch for League of Legends.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    embed = hikari.Embed(title="Latest LoL Patch", description="Image displaying current LoL Patch", color=yellow)
    embed.add_field("Features:", 'Champion Buffs, Champion Nerfs, Champion Adjustments, System Nerfs,'
                                 ' System Adjustments.')
    embed.set_thumbnail("https://pbs.twimg.com/media/Fnw7YMsaAAA-aAh?format=png&name=small") # This needs to be worked on
    # embed.set_footer("")
    await ctx.respond(embed)


@bot.command
@lightbulb.option('second_name', 'The second name', type=str)
@lightbulb.option('first_name', 'The first name', type=str)
@lightbulb.command("luv", "Calculate your compatibility (luv) based on names.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    first_name = ctx.options.first_name
    second_name = ctx.options.second_name
    postotak = random.randint(0, 100)
    if first_name == 'Tamir' and second_name == 'yamato':
        embed = hikari.Embed(title=f"{first_name}  :heart:  {second_name}  :arrow_right:  **100%**"
                             , description="Literally a match made in heaven.\n(JoJo's reference)", color=red)
        embed.set_image('https://i.imgur.com/G88LTW2.png')
    elif postotak <= 50:
        embed = hikari.Embed(title=f"{first_name}  :broken_heart:  {second_name}  :arrow_right:  **{postotak}%**"
                             , description="Nah yall ain't finna work lmao.", color=dark_purple)
        embed.set_image('https://i.imgur.com/yNfvyhD.png')
    elif 51 <= postotak <= 80:
        embed = hikari.Embed(title=f"{first_name}  :heartpulse:  {second_name}   :arrow_right:  **{postotak}%**"
                             , description="Not bad, yall might have a *slight* chance.", color=pink)
        embed.set_image('https://i.imgur.com/6Q1SH3V.png')
    else:
        embed = hikari.Embed(title=f"{first_name}  :heart:  {second_name}  :arrow_right:  **{postotak}%**"
                             , description="Literally a match made in heaven.\n(JoJo's reference)", color=red)
        embed.set_image('https://i.imgur.com/G88LTW2.png')
    await ctx.respond(embed)


@bot.command
@lightbulb.command("anime", "Sends anime websites (Legal and illegal)")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    embed = hikari.Embed(title="Best anime websites!", description="Links below:", color=white)
    embed.add_field("Legal (Crunchyroll):", 'https://www.crunchyroll.com/')
    embed.add_field("Legal (Netflix):", 'https://www.netflix.com/')
    embed.add_field("Legal (Funimation):", 'https://www.funimation.com/')
    embed.add_field("Illegal (9anime):", 'https://www.9anime.to/')
    embed.add_field("Illegal (Animension):", 'https://www.animension.to/')
    embed.add_field("Illegal (Gogoanime):", 'https://www.gogoanime.gg/')
    embed.add_field("Illegal (Zoro):", 'https://www.zoro.to/')
    embed.set_thumbnail("https://imgur.com/AXp86zF.png")
    # embed.set_thumbnail("https://pbs.twimg.com/media/Fj0BFakUAAAyP_S?format=png&name=small")
    embed.set_footer("Use the illegal links at your own risk.")
    await ctx.respond(embed)


@bot.command
@lightbulb.command("yamato", "Sends a gif of Yamato waving at you (You have no life)")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    await ctx.respond('https://media.tenor.com/fk77xC7Ds8IAAAAd/yamato-yamato-one-piece.gif')


@bot.command
@lightbulb.command("thatswhatimsaying", "Sends a gif of the guy falling over a chair")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    await ctx.respond('https://tenor.com/view/dirty-docks-shawty-triflin-shawty-triflin-she-gif-22455514')


@bot.command
@lightbulb.command("dance", "Just sends the classic hood dance (Reactionary)")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    await ctx.respond('https://tenor.com/view/black-man-dance-yoasobi-racing-into-the-night-gif-23875910')


@bot.command
@lightbulb.command("hort", "Heads or tails.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    number = random.randint(1, 2)
    if number == 1:
        await ctx.respond('You got: **Heads**')
    else:
        await ctx.respond('You got: **Tails**')


@bot.command
@lightbulb.command("dice", "Throws a dice.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    kockica = random.randint(1, 6)
    await ctx.respond(f'You got: **{kockica}** :game_die:')


@bot.command
@lightbulb.option('question', 'The future to be foretold.', type=str)
@lightbulb.command("8ball", "Foretells the future.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    pitanje = ctx.options.question
    fortune = random.randint(0, 19)
    embed = hikari.Embed(title=f"**Q:** *{pitanje}*"
                         , description=f"**A: {eightball[fortune]}**", color=white)
    embed.set_image('https://i.imgur.com/NyCeUKr.png')
    await ctx.respond(embed)


bot.run(
    status=hikari.Status.DO_NOT_DISTURB,
    activity=hikari.Activity(
        name="$YourName$-sama",
        type=hikari.ActivityType.LISTENING,
    ),
)
