def catch_with_bpython(_type, _value, _traceback):
    import traceback
    traceback.print_exception(_type, _value, _traceback)
    while _traceback.tb_next != None:
        _traceback = _traceback.tb_next
    import bpython
    bpython.embed(_traceback.tb_frame.f_locals)
	
import sys
sys.excepthook = catch_with_bpython

