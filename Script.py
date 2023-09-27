class script(object):
    START_TXT = """
Hey there {}, This Bot lets you search the Songs in my Database and i just share with Anyware. 
It's Only supports Inline Search Queries.
Try by writing a query to search a song or type `@songsaf_bot song_name` in any chat.
You Just do type the Button below :)
"""
    HELP_TXT = """Hey {}\nHere is my commands."""
    ABOUT_TXT = """My Name: {}
👤 Creator: <a href=https://t.me/TeamEvaMyra>Team Eva</a>
📚 Library: Program 
💱 Language: Python 𝟹
💾 DataBase: Mango 𝙳𝙱
📡 Bot Server: Heroku 
📊 Build Status: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""

    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my Owner
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
    
    STATUS_TXT = """📁 Total Files: <code>{}</code>
🙋 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
💾 Used Storage: <code>{}</code> 𝙼𝙱
🆓 Free Storage: <code>{}</code> 𝙼𝙱"""
    
    LOG_TEXT_G = """#NewGroup
👥Group = {}(<code>{}</code>)
💫Total Members = <code>{}</code>
🙋Added By - {}
"""
    
    LOG_TEXT_P = """#NewUser
⭐ID - <code>{}</code>
☕ Name - {}
"""
