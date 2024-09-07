## Python requirements

```pip3 install pandas capstone```

## Input format

Dump the input in the form of a csv. You can do this from the testbench. Here is the example of a input csv that we will process

```
Cycle,PC,Fetch_stage_Instruction
4,00000084,00016197
5,00000088,9d018193
6,0000008c,00400117
7,00000090,f7810113
8,00000094,00000517
9,00000098,f7050513
10,0000009c,00156513
```

## Invoke rtl_instr_tracer.py (Set the paths inside the python script)

## Example Output csv

```
Cycle,PC,Fetch_stage_instruction_hex,Fetch_stage_instruction_asm,Fetch_stage_instruction_mnemonic
4,00000084,00016197,"auipc gp, 0x16",auipc
5,00000088,9d018193,"addi gp, gp, -0x630",addi
6,0000008c,00400117,"auipc sp, 0x400",auipc
7,00000090,f7810113,"addi sp, sp, -0x88",addi
8,00000094,00000517,"auipc a0, 0",auipc
9,00000098,f7050513,"addi a0, a0, -0x90",addi
10,0000009c,00156513,"ori a0, a0, 1",ori
```