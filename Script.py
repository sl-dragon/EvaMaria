class script(object):
    START_TXT = """<b>කොහොමද ඉතින්...</b> {},
මම <a href=https://t.me/{}>{}</a>,
<a href=https://t.me/mybotz>My Botz</a> විසින් කල සංස්කරණයකි🔱
<b> I Can Provide Movies, Just Add Me To Your Group And Enjoy</b>😍"""
    HELP_TXT = """HEY{}
Here My Commands."""
    ABOUT_TXT = """✯ MY NAME: {}
✯ CREATOR: <a href=https://t.me/mybotz>My Botz</a>
✯ LIBRARY: PYROGRAM
✯ LANGUAGE: PYTHON 3
✯ DATA BASE: MONGO DB
✯ BOT SERVER: HEROKU
✯ BUILD STATUS: v1.0.1"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>oops!</b>
There No source code"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and This Bot will respond whenever a keyword is found the message

<b>සැලකියයුතුයි :</b>
1. BOT ට අනිවාර්යෙන් Admin ලෙස Add කර තිබිය යුතුයි .
2. Admin කෙනෙක්ට විතරයි Filters Add කරන්න පුළුවන් .
3. Alert Buttons එක බාවිතා කල හැක්කේ අකුරු 64 වඩා අඩු වාක්‍ය සදහා පමණි .

<b>Commands and Usage:</b>
• /filter - <code>Filter එකක් Add කිරීමට </code>
• /filters - <code>Chat එකට මෙතෙක් Add කර ඇති Filters list එක </code>
• /del - <code>Filter එකක් Delete කිරීමට </code>
• /delall - <code>සියලුම Filters Delete කිරීමට </code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. කිසිදු අන්තර්ගතයක් නොමැතිව බොත්තම් යැවීමට ටෙලිග්‍රාම් ඔබට ඉඩ නොදේ, එබැවින් අන්තර්ගතය අනිවාර්ය වේ.
2. BOT ඕනෑම Media සහිත බොත්තම් සඳහා සහය දක්වයි.
3. Buttons සියල්ල Markdown Format එකෙන් තිබිය යුතුය 

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ TOTAL USERS: <code>{}</code>
★ TOTAL CHATS: <code>{}</code>
★ USED STORAGE: <code>{}</code> 𝙼𝚒𝙱
★ FREE STORAGE: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
