import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def XOR_Test(dut):
   a = (0, 0, 1, 1)
   b = (0, 1, 0, 1)
   y = (0, 1, 1, 0)

   for i in range(len(y)):
       dut.a.value = a[i]
       dut.b.value = b[i]
       await Timer(1,'ns')
       assert dut.y.value == y[i], "### Error at iteration {i}"
