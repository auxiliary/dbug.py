import sys
import traceback
import code
import bpython

def catch_with_bpython(_type, _value, _traceback):
    traceback.print_exception(_type, _value, _traceback)
    message = "Select a frame to view using the select(<frame #>) command"
    print '\x1b[0;34;40m' + message + '\x1b[0m'
    all_locals = [_traceback.tb_frame.f_locals]
    while _traceback.tb_next != None:
        _traceback = _traceback.tb_next
        all_locals.append(_traceback.tb_frame.f_locals)

    def select(frame_no):
        bpython.embed(all_locals[frame_no])

    code.interact(local=locals(), banner='')

if __name__ == '__main__':
    sys.excepthook = catch_with_bpython
    execfile(sys.argv[1])