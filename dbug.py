import os
import sys
import traceback
import code
import bpython

def print_banner():
    message = "Select a frame to view using the select(<frame #>) command"
    print '\n\x1b[0;34;40m' + message + '\x1b[0m'
    message = "Reload the script using the reload() command"
    print '\x1b[0;34;40m' + message + '\x1b[0m'

def print_with_color(text):
    print '\x1b[0;34;40m' + text + '\x1b[0m',

def catch_with_bpython(_type, _value, _traceback):
    listing = traceback.format_exception(_type, _value, _traceback)
    counter = 0
    for line in listing:
        if line.strip().startswith("File "):
            print_with_color(str(counter) + ") ")
            counter += 1
        print line
    print_banner()

    all_locals = [_traceback.tb_frame.f_locals]
    while _traceback.tb_next != None:
        _traceback = _traceback.tb_next
        all_locals.append(_traceback.tb_frame.f_locals)

    def select(frame_no):
        bpython.embed(all_locals[frame_no])

    def reload():
        os.execv(sys.executable, ['python'] + sys.argv)

    code.interact(local=locals(), banner='')

if __name__ == '__main__':
    sys.excepthook = catch_with_bpython

    args = sys.argv[1].split(":")
    filename = args[0]
    # remove the line argument so it doesn't interfere with 
    # user's program
    sys.argv.pop(0)
    if len(args) > 1:
        line = int(args[1])
    else:
        line = None

    fp = open(filename)
    source = fp.readlines()
    fp.close()
    if line != None:
        if source[line - 1].strip() == "": # causes indentation issues
            source[line - 1] = "raise Exception('breakpoint')\n"
        else:
            source[line - 1] = source[line - 1] \
                .replace("\n", "; raise Exception('breakpoint')\n")
    source = ''.join(source)

    exec(compile(source, filename=filename, mode='exec'))
