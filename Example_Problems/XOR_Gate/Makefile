SIM ?= icarus
TOPLEVEL_LANG ?= verilog
PWD = $(shell pwd)
VERILOG_SOURCES += $(PWD)/v_code/XOR_gate.v
VERILOG_SOURCES += $(PWD)/Wrapper/XOR_TEST.v
 MODULE = xor_test 
 TOPLEVEL = xor_test

include $(shell cocotb-config --makefiles)/Makefile.sim
