import hexchat
import os

__module_name__ = "auto-ldr"
__module_version__ = "0.1"
__module_description__ = "Scripts loader"

hexchat.prnt("auto-ldr")
hexchat.command("echo Hello, user!")


def load_cmdff_callback(word, wrod_eol, userdata):
    hexchat.prnt("-->load_cmdff_callback")
    hexchat.prnt("-- start ./irc_scripts/hexchat/cmd-from-file.py")
    hexchat.command("load %s" % os.path.expanduser('~/irc_scripts/hexchat/cmd-from-file.py'))
    return hexchat.EAT_ALL


def unload_cmdff_callback(word, wrod_eol, userdata):
    hexchat.prnt("-->unload_cmdff_callback")
    hexchat.prnt("-- unload cmd-from-file.py")
    hexchat.command("unload cmd-from-file.py")
    return hexchat.EAT_ALL


hexchat.hook_command("load_cmdff", load_cmdff_callback)
hexchat.hook_command("unload_cmdff", unload_cmdff_callback)

# auto load
hexchat.command("load_cmdff")
