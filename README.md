# hammy-bot

Hammy bot is a feature-rich discord bot with over 50 commands that can help staff members/regular members to have fun and keep everyone safe.


MORE ABOUT COMMANDS:

  The commands cogs can be found in cogs direcotry that has 10 sub-cogs:

    -api(commands that use public API's in order to work)
    -custom_commands(random commands for members fun)
    -donation(commands for donations)
    -games(custom basic and fun games)
    -giveaway(commands for giveaways)
    -info(commands that show information about the bot status or command list)
    -leveling(not impelemented yet)
    -moderation(commands that help staff members of a server to keep the server secure and help them to gather information about server's members)
    -music(commands that control a music player whitin a server) - no longer working due Youtube callout
    -usefull_commands(commands that help staff members/ regular members to access helpful features in daily server activities)

    Every command has a description and mini-tutorial on how it works ('help' command  display a paginated command list for these information)
    Most command errors and bugs have been fixed in the past updates.
 
 MAIN FILE:
 
 The main.py file initialize the basic bot information(status, bot prefix, owner id), import and turn on all the cogs, overwatch the member join history whitin the server and error handling messages.
 
 BOT MAINTENANCE:
 
 If there shows up a unexpected bug or error and the bot doesn't work properly, Hammy bot has the solution to fix this problem. In cogs -> moderation.py u can find the 'reload' function to reload a given cog with all commands in it.
 
