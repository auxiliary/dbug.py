import sys
import traceback
import bpython

def catch_with_bpython(_type, _value, _traceback):
    traceback.print_exception(_type, _value, _traceback)
    while _traceback.tb_next != None:
        _traceback = _traceback.tb_next
    bpython.embed(_traceback.tb_frame.f_locals)
	
if __name__ == '__main__':
	sys.excepthook = catch_with_bpython
	execfile(sys.argv[1])
