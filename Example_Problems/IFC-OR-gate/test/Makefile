SIM ?= icarus
TOPLEVEL_LANG ?= verilog
PWD = $(shell pwd)
VERILOG_SOURCES += $(PWD)/wrappers/ifc_test.v
VERILOG_SOURCES += $(PWD)/wrappers/or_test.v
VERILOG_SOURCES += $(PWD)/../hdl/ifc_or.v
VERILOG_SOURCES += $(PWD)/../hdl/or_gate.v
VERILOG_SOURCES += $(PWD)/../hdl/FIFO1.v
VERILOG_SOURCES += $(PWD)/../hdl/FIFO2.v
all: ifc

ifc : 
	 rm sim_build -rf
	$(MAKE) sim MODULE=ifc_test TOPLEVEL=ifc_test



#MODULE := ifc_test
#TOPLEVEL := ifc_test	
	
include $(shell cocotb-config --makefiles)/Makefile.sim	
	
