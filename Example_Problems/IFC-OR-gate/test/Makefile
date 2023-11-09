SIM ?= icarus
TOPLEVEL_LANG ?= verilog
PWD = $(shell pwd)
VERILOG_SOURCES += $(PWD)/Wrappers/ifc_test.v
VERILOG_SOURCES += $(PWD)/Wrappers/or_test.v
VERILOG_SOURCES += $(PWD)/HDL/ifc_or.v
VERILOG_SOURCES += $(PWD)/HDL/or_gate.v
VERILOG_SOURCES += $(PWD)/HDL/FIFO1.v
VERILOG_SOURCES += $(PWD)/HDL/FIFO2.v
all: ifc

ifc : 
	 rm sim_build -rf
	$(MAKE) sim MODULE=ifc_test TOPLEVEL=ifc_test



#MODULE := ifc_test
#TOPLEVEL := ifc_test	
	
include $(shell cocotb-config --makefiles)/Makefile.sim	
	
