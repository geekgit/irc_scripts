import threading
import os
import time
import hexchat

__module_name__ = "cmd-from-file"
__module_version__ = "0.1"
__module_description__ = "cmd-from-file"


class CmdffTestFile:
    @staticmethod
    def cmdff_test_file(filename):
        print("Try to read file '%s'..." % filename)
        flag = os.path.exists(filename) and os.path.isfile(filename)
        print ("is file and exists: %s" % flag)
        if flag:
            print "OK"
            return True
        else:
            print "Not OK"
            return False


class CmdffReadFile:
    @staticmethod
    def cmdff_read_line(filename, index):
        cmdff_file = open(filename)
        for i, line in enumerate(cmdff_file):
            if i == index:
                cmdff_file.close()
                return line.rstrip()
        cmdff_file.close()
        return False

    @staticmethod
    def cmdff_do_line_action(filename, func):
        index = 0
        while True:
            line = CmdffReadFile.cmdff_read_line(filename, index)
            index = index + 1
            if not line:
                break
            else:
                print("#%d: %s, call %s('%s')" % (index, line, func.__name__, line))
                func(line)


def cmdff_read_all(filename):
    index = 0
    while True:
        line = CmdffReadFile.cmdff_read_line(filename, index)
        index = index + 1
        if not line:
            break
        else:
            print("#%d: %s" % (index, line))


def testprint(s):
    print(s)
    time.sleep(5)


def hexchatexec(s):
    hexchat.command(s)
    time.sleep(5)


def testwork():
    CmdffReadFile.cmdff_do_line_action("somefile.txt", testprint)


def hexchatwork():
    CmdffReadFile.cmdff_do_line_action("somefile.txt", hexchatexec)


def cmdff_callback(word, wrod_eol, userdata):
    thread = threading.Thread(target=hexchatwork)
    thread.start()
    #thread.join()
    return hexchat.EAT_ALL


hexchat.hook_command("cmdff", cmdff_callback)
