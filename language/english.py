#===================================================================================================================================================================#
																#=#=# General #=#=#
# - Language - #
Language                                    = "English"
LanguageShort                               = "en"
# - Time - #
DateFormat                                  = "dd-MMM-yyyy"
FormatLocale                                = "en"
TimeFormat                                  = "HH:mm:ss"



#===================================================================================================================================================================#
                                                                #=#=# General Data Information #=#=#
Server = "Server"
Owner = "Owner"



#===================================================================================================================================================================#
																#=#=# Administration #=#=#

# - Broadcast - #
BroadcastFooter 							= "Discord-Manager | Information"
BroadcastSuccess 							= ":rocket: Alle Server die mit der **Cheep-Netzwerk Cloud** verbunden sind wurden informiert"
BroadcastHelp 								= "**USAGE:** {PREFIX}Broadcast <Message>"
BroadcastHelpDescription 					= "Sendet eine Nachricht an alle verbundenen Server"

# - Global Administration - #
GlobalAdministrationDescription 			= "Administration - Bereich\n\n `{PREFIX}system info <Server-ID>`  -  Zeigt die Server-Informationen ab\n `{PREFIX}system warn <Server-ID>` -  Verwant einen Server\n `{PREFIX}system add <Server-ID>`  -  Fügt eine bestimmt Anzahl an Warn-Points hinzu\n `{PREFIX}system remove <Server-ID>`  -  Entfernt eine bestimmt Anzahl an Warn-Points\n `{PREFIX}system reset <Server-ID>`  -  Löscht alle Verwarnungen eines Servers\n `{PREFIX}system ban <Server-ID>`  -  Bannt einen Server\n `{PREFIX}system invite <Server-ID>`  -  Erstellt einen Invite-Link zu dem Server"
GlobalAdministrationInvalidServerID 		= ":warning:  Please enter a valid Server-ID"
GlobalAdministrationInfoTitle 				= "System-Information"
GlobalAdministrationInfoServer 				= "Server"
GlobalAdministrationInfoOwner 				= "Owner"
GlobalAdministrationInfoWarnings 			= "Warnings"
GlobalAdministrationInfoBanStatus 			= "Ban Status"
GlobalAdministrationInfoBanReason 			= "Ban Reason"
GlobalAdministrationError 					= "**Ein Fehler ist aufgetreten. Bitte Probiere es erneut.**"
GlobalAdministrationSuccessWarn 			= "Du hast den Server **{SERVER}** verwarnt! Der Server hat nun  **{WARNS}** Verwarnungen"
GlobalAdministrationSuccessDeleteWarnsAll 	= "Du hast alle Verwarnungen des Servers **{SERVER}** gel�scht"
GlobalAdministrationSuccessBan 				= "Du hast den Server **{SERVER}** gebannt"
GlobalAdministrationBanMessage 				= "The **Discord-Manager** is now banned from your server, because you broke our terms of use! You can read the terms of use on our webseite!\n	You have further questions? Than please contact our support!\n You can find our contact details on our website or you can also directly join our [Discord Server](https://discord.com/invite/YpHRzPx) to request support. \nThanks for your understanding.\n\n Best Regards\n Security-Team"
GlobalAdministrationSuccessLeave 			= "Der Discord-Manager hat erfolgreich den Server `{Server}` (`{ServerID}`) verlassen."
GlobalAdministrationCreateInviteWaite 		= "Creating a new Invite for you... Please wait!!"
GlobalAdministrationCreateInvite 			= "Invite for **{SERVER}**"
GlobalAdministrationErrorCreateInvite 		= "Ich besitze auf dem Server **{SERVER}** nicht genügend Rechte um einen Invite-Link zu erstellen"



#===================================================================================================================================================================#
																#=#=# Bot Information #=#=#

# - BotMention - #
BotMentionRespond 							= "**Network-Status:**\n Cheep-Netzwerk | API: {STATUSICON} **Online**\n Cheep-Netzwerk | Cloud: {STATUSICON} **Online**\n Cheep-Netzwerk | Discord-Manager: {STATUSICON} **Online**\n Cheep-Netzwerk | Verify-System: {STATUSICON} **Online**\n Cheep-Netzwerk | Account-System: {STATUSICON} **Online**\n Cheep-Netzwerk | Server-System: {STATUSICON} **Online**\n **Website:** [Cheep-Netzwerk.de](https://Cheep-Netzwerk.de)\n\n**Need Help?**\nDo **!help** to see my Commands.\n\nOur staff team also can help you... **[Click here](http://Discord.Cheep-Netzwerk.de)**"

# - Bot Stats - #
BotStatsHelp 								= "**USAGE:** {PREFIX}botstats"
BotStatsHelpDescription 					= "Displays stats of the bot"

BotStatsTitle 								= "\🤖 **Discord-Manager STATS**"
BotStatsCommandsRegistered 					= "Registered commands:"
BotStatsServers 							= "Running on servers:"
BotStatsMembers 							= "Deserving members:"
BotStatsMessages 							= "Messages processed:"
BotStatsCommandsExecuted 					= "Commands executed:"

# - Information - #
InformationHelp 							= "**USAGE:** {PREFIX}info"
InformationHelpDescription 					= "Shows information about the bot"

InformationTitle 							= "\🤖 **Discord-Manager**"
InformationVersion 							= "Version"
InformationBotPhase 						= "Bot Phase"
InformationCopyright 						= "Copyright"
InformationCopyrightMessage 				= "Discord-Manager is copyrighted by Cheep-Netzwerk.de\n © 2015 - {YEAR} {AVATAR} GamerBoomTV | Dan"
InformationDiscord 							= "Discord"
InformationWebsite 							= "Website"
InformationWhatsApp 						= "WhatsApp-Support"
InformationDiscordManager 					= "Discord-Manager"

# - Network Invite - #
NetworkInviteHelp							= "**USAGE:** {PREFIX}invite"
NetworkInviteHelpDescription 				= "Shows bot invite links"

NetworkInviteDescription					=":loudspeaker: You can join the **Discord-Manager Community** under **_{DiscordServer}_** and invite me here: **{DiscordBot}**!"

# - Permissions-Information - #
PermissionsInfoHelp 						= "**USAGE:** {PREFIX}Rank"
PermissionsInfoHelpDescription 				= "Shows you information to your permission"

PermissionsInfoRespond 						= "Your name is **{NAME}**, your highest rank is **{ROLE}** so you had an permission level of **{LEVEL}**"

# - Ping - #
PingHelp 									= "**USAGE:** {PREFIX}ping"
PingHelpDescription 						= "Shows the ping of the Discord-Manager"

PingRespond									= ":ping_pong: **Pong!**\n\n The Discord-Manager took `%s` milliseconds to response.\n It took `%s` milliseconds to parse the command and the ping is `%s` milliseconds.\n\n Cheep-Netzwerk | Cloud {STATUSICON} **Online**\n Cheep-Netzwerk | API {STATUSICON} **Online**\n\n Cheep-Netzwerk | Ticket-Server {STATUSICON} **Online**\n Cheep-Netzwerk | Voice-server {STATUSICON} **Online**\n"

# - Uptime - #
UptimeHelp									= "**USAGE:** {PREFIX}uptime"
UptimeHelpDescription						= "Shows information to the uptime of the bot"
 
Uptime										= "Uptime"
UptimeTitle									= ":alarm_clock:   **Status - Anzeige**"
UptimeLastRestart							= "last restart"
UptimeReconnects							= "Reconnects"



#===================================================================================================================================================================#
																#=#=# Bot Information #=#=#
# - Count - #
CountHelp 									= "**USAGE:** !count <Message>"
CountHelpDescription 						= "Count chars, words and sentences of an input string"

CountTitle 									= "String Analyze"

# - Quote - #
QuoteHelp									= "**USAGE:** !quote <Message id>"
QuoteHelpDescription 						= "Quote a message in any channel on guild"

QuoteSearch 								= "Searching for message in text channels..."
QuoteSearchError 							= "There is no message in any Chat on this guild with the ID `{SearchID}`."
QuoteRespond 								= "**Quote from {User}**\n\n ▬▬▬▬▬▬▬▬▬▬▬▬**[ [Jump to message](https://discordapp.com/channels/{GuildID}/{ChannelID}/{TextMessageID})]▬▬▬▬▬▬▬▬▬▬▬▬**\n\n _Quoted message:_\n >>> {CONTENT}\n\n"
QuoteIn										= "at"
QuoteInChannel								= "in channel #"

# - Help - #
HelpDescription 							= "\"I din't need a help...\" :D"

HelpErrorNoInformation 						= ":information_source: No Information find in the **Cheep-Netzwerk Cloud** (**!{Command}**)"
HelpErrorNotRegistered 						= ":information_source: This Command ist not registered in the **Cheep-Netzwerk Cloud** (**!{Command}**)"
HelpRespond 								= ":clipboard:  __**Discord-Manager Commands**__  :clipboard: \n\n Support:\n :black_small_square: **http://Discord.Cheep-Netzwerk.de**\n Website:\n :black_small_square: **https://Cheep-Netzwerk.de**\n :white_small_square:  -  For everyone\n :small_blue_diamond:  -  Only for groups `{GROUPS} :small_orange_diamond:  -  Only for groups `{GROUPS}`\n :small_red_triangle_down:  -  Only for Owners and users with the right Administrator"

# - ID - #
IdHelp                                      = "**USAGE:** !id <search query>"
IdDescription                               = "Get the ID of server elements by name query"

IdTitle                                     = "Found results for search query ```%s```"
IdRoles                                     = "Roles"
IdVoiceC                                    = "Voice Channels"
IdTextC                                     = "Text Channels"
IdMembers                                   = "Members"
IdErrorNoMatchesFound                       = "*No matches found*"

# - Stats - #
StatsHelp                                   = "**USAGE:** {PREFIX}stats"
StatsDescription                            = "Get stats of the server"

StatsTitle                                  = "**All Clients:**   %d\n **Members:**   %d   (Online:  %d)\n **Bots:**   %d   (Online:  %d)"
StatsName                                   = "Name"
StatsID                                     = "ID"
StatsOwner                                  = "Owner"
StatsServerRegion                           = "Server Region"
StatsChannels                               = "Channels"
StatsChannelsVoice                          = "Text Channel"
StatsChannelsText                           = "Voice Channel"
StatsMembers                                = "Members"
StatsRoles                                  = "Roles"
StatsAFKChannel                             = "AFK Channel"
StatsServerAvatar                           = "Server Avatar"
StatsErrorNotSet                            = "not set"

# - User Info - #
UserInfoHelp                                = "**USAGE:** {PREFIX}user <@user>"
UserInfoHelpDescription                     = "Get some info about a user"

UserInfoErrorNoRoles                        = "No roles on this server."
UserInfoErrorNoAvatar                       = "No Avatar"
UserInfoTitle                               = ":spy: **User information for {USER}:**"
UserInfoUserName                            = "Name / Nickname"
UserInfoUserTag                             = "User Tag"
UserInfoID                                  = "ID"
UserInfoCurrentStatus                       = "Current Status"
UserInfoCurrentGame                         = "Current Game"
UserInfoRoles                               = "Roles"
UserInfoGuildPermissonLevel                 = "Guild Permission Level"
UserInfoGuildJoin                           = "Guild Joined"
UserInfoDiscordJoined                       = "Discord Joined"
UserInfoAvatarURL                           = "Avatar-URL"



#===================================================================================================================================================================#
                                                                #=#=# FUN #=#=#
# - GIF - #
GIFHelp                                     = "gif <search query>"
GIFHelpDescription                          = "Search funny GIF's, to hold your chat crazy"

GIFSearch                                   = "I am searching for a awesome gif"
GIFError                                    = "GIF ERROR"
GIRErrorNSWF                                = "This channel is not a NSWF Channel. Please try the command again in a NSWF Channel. Protection is possible!"


# - JOKE - #
JokeHelp                                    = "**USAGE:** {PREFIX}joke "
JokeHelpDescription                         = "Read funny jokes, to make you happy"

Joke1                                       = ""
Joke2                                       = ""
Joke3                                       = ""
Joke4                                       = ""
Joke5                                       = ""
Joke6                                       = ""
Joke7                                       = ""
Joke8                                       = ""
Joke9                                       = ""
Joke10                                      = ""
Joke11                                      = ""
Joke12                                      = ""
Joke13                                      = ""
Joke14                                      = ""
Joke15                                      = ""
Joke16                                      = ""
Joke17                                      = ""
Joke18                                      = ""
Joke19                                      = ""
Joke20                                      = ""
Joke21                                      = ""
Joke22                                      = ""
Joke23                                      = ""
Joke24                                      = ""
Joke25                                      = ""
Joke26                                      = ""
Joke27                                      = ""
Joke28                                      = ""
Joke29                                      = ""
Joke30                                      = ""
Joke31                                      = ""
Joke32                                      = ""
Joke33                                      = ""
Joke34                                      = ""
Joke35                                      = ""

# - OP - #
OPHelp                                      = "**USAGE:** {PREFIX}op"
OPHelpDescription                           = "Gives you magical rights"

OPQueued                                    = "was added to the _highest rank_ and now have the rank:"
OP1                                         = "Ohh... you still have no higher rights"
OP2                                         = "Sryyy... This was a joke"
OP3                                         = "The rights are unfortunately too high for you... I hope you are still satisfied with your current rank.."
OP4                                         = "Why should I give you higher rights? I don't know you :jack_o_lantern:"
OP5                                         = "To :100:% I can tell you you will not get higher rights... It seems to me as if fu was not satisfied with your rank..."
OP6                                         = "Well how about to apply? Instead of trying to give the rights with the order?"
OP7                                         = "Nooo... I think you don't need higher rights..."
OP8                                         = "Already lousy you still have no higher rights..."
OP9                                         = "That would be too easy to get rights .... You must continue to live with your rank"
OP10                                        = "Why do you still only have the same rank? Muhahah you have no higher rights"

# - Questions - #
QuestionHelp                                = "**USAGE:** !? <Your Joke>"
QuestionHelpDescription                     = "Joke the bot a question"

QuestionKickBan                             = "... I think he is needed more than you ...! Please go, before I have to help you...:punch::skin-tone-1:"
Question1                                   = ":thumbsup: Yes"
Question2                                   = ":thumbsdown: No"
Question3                                   = ":handshake: Maybe"
Question4                                   = "Nope"
Question5                                   = "Unlikely"
Question6                                   = "Probably"
Question7                                   = "to 100%"
Question8                                   = "to 50%"
Question9                                   = "to 0%"
Question10                                  = "Joa"
Question11                                  = "Nope"
Question12                                  = "no way"
Question13                                  = "NO"
Question14                                  = "Do you have a bang?"
Question15                                  = "Since my knowledge is not enough... for you important question."
Question16                                  = "I think the answer you know yourself... It's _**Yes**_"
Question17                                  = "I think the answer you know yourself... It's _**No**_"
Question18                                  = "Donald Duck would say _Yes_, like me"
Question19                                  = "I love this questions, so I say _**YES**_"
Question20                                  = "I hate the questions, so I say _**NO**_"
Question21                                  = "I would say _No_"
Question22                                  = "{USER} that's a crazy question? But im currently thinking, that the answer _**No**_ makes you happy. :smile"
Question23                                  = "{USER} that's a crazy question? But im currently thinking, that the answer _**Yes**_ makes you happy. :smile:"
Question24                                  = "{USER}, the question is not nice I think the answer you have to look for yourself... sry"



#===================================================================================================================================================================#
                                                                #=#=# GUILD ADMINISTRATION #=#=#
# - Autochannel - #
AutochannelHelp = "**USAGE:**\n !autochannel set <Channel ID>`  -  Add an autochannel\n !autochannel unset <Channel ID>`  -  Remove an autochannel\n !autochannel list`  -  List all autochannel\n Autochannel"
HelpDescription = "Create, delete and manage your Voice-Autochannels"

AutochannelErrorTitle = "**Error - Autochannel** \n\n"
AutochannelErrorNotExist = "Voice channel with the ID `%s` does not exist."
AutochannelErrorAlreadySet = "This channel is just set as auto channel."
AutochannelErrorNotSet = "Voice channel `%s` is not set as auto channel."
AutochannelSuccessSet = "Successfully set voice channel `%s` as auto channel."
AutochannelSuccessUnset = "Successfully unset auto channel state of `%s`."
AutochannelListTitle = "**Auto-Channel**\n\n"
AutochannelListStyle = ":white_small_square:   `%s` *(%s)*\n"

# - BAN - #
BanHelp = "**USAGE:** {prefix}}ban <@Mention> <Reason>"
BanHelpDescription = "Ban a member from your Discord"

BanMessageSender = "{NAME} got banned by ({ROLE}) {NAME}\n\n Reason: **{REASON}**"
BanMessageReceiver = "You got banned from the Discord **{Server}** by **(ROLE) {NAME}\n\n Reason: {REASON}"
BanStandardReason = "Breaking the rules"

# - BLACKLIST - #
