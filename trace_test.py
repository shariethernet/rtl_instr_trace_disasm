from capstone import Cs, CS_ARCH_RISCV, CS_MODE_RISCV32

def disassemble_riscv(instruction):
    # Initialize Capstone for RISC-V 32-bit
    md = Cs(CS_ARCH_RISCV, CS_MODE_RISCV32)

    # Convert the instruction to bytes (assuming little-endian)
    instruction_bytes = instruction.to_bytes(4, byteorder='little')
    print(f"Instruction bytes: {instruction_bytes}")

    # Disassemble the instruction
    for i in md.disasm(instruction_bytes, 0x1000):  # 0x1000 is a dummy address
        return f"{i.mnemonic} {i.op_str}"

    return "Unable to disassemble"

# Test instruction
instr = 0x00128293

# Disassemble and display the instruction
asm = disassemble_riscv(instr)
print(f"Instruction: 0x{instr:08x}")
print(f"Assembly: {asm}")