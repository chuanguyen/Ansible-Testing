# Used to write directly to CPU register in order to apply an undervolt
# Guide from: https://github.com/mihic/linux-intel-undervolt

### Calculating wrmsr value
# Python function to generate offset value
# format(0xFFE00000&( (round({mV VALUE}*1.024)&0xFFF) <<21), '08x')

Plane Index:
0 - CPU Core
1 - Intel GPU
2 - CPU Cache

Value Breakdown:

MSR Register
0x150
Constant:
80000
Plane Index:
0
Constant:
1
Read/Write (0/1)
1
Offset
00000000

### Reading wrmsr value

# CPU Core
wrmsr 0x150 0x8000001000000000
rdmsr 0x150
# iGPU
wrmsr 0x150 0x8000011000000000
rdmsr 0x150
# CPU Cache
wrmsr 0x150 0x8000021000000000
rdmsr 0x150

### Verifying
Set the undervolt values manually before configuring the service to test for stability. View voltage changes via the i7z utility. 
