import pandas as pd
from capstone import Cs, CS_ARCH_RISCV, CS_MODE_RISCV32
import os

def hex_to_assembly(hex_instruction):
    # Initialize Capstone for RISC-V 32-bit
    md = Cs(CS_ARCH_RISCV, CS_MODE_RISCV32)
      # Convert hex string to bytes
    try:
        instruction_bytes = bytes.fromhex(hex_instruction)[::-1]
    
        # Disassemble the instruction
        full_string=""
        for i in md.disasm(instruction_bytes, 0x1000):  # 0x1000 is a dummy address
            full_string= f"{i.mnemonic} {i.op_str}".strip()
            return full_string,i.mnemonic
        # If disassembly fails, return the original hex
        #return f"UNKNOWN_{hex_instruction}"
        return(f"UNKNOWN_{hex_instruction}","UNKNOWN")
    except:
        #return f"UNKNOWN"
        return(f"UNKNOWN_{hex_instruction}","UNKNOWN")

def convert_instruction_trace(input_csv_path, output_csv_dir, output_csv_name):
    # Read the input CSV
    df = pd.read_csv(input_csv_path, dtype={'Fetch_stage_Instruction': str})
    
    # Convert hex instructions to assembly
    #hex_to_assembly retuns a typle of two values, the first value is the full assembly instruction and the second value is the mnemonic
    df['Fetch_stage_instruction_asm'] = df['Fetch_stage_Instruction'].apply(lambda x: hex_to_assembly(x)[0])
    df['Fetch_stage_instruction_mnemonic'] = df['Fetch_stage_Instruction'].apply(lambda x: hex_to_assembly(x)[1])
    
    # Rename the original instruction column
    df = df.rename(columns={'Fetch_stage_Instruction': 'Fetch_stage_instruction_hex'})
    
    # Reorder columns
    df = df[['Cycle', 'PC', 'Fetch_stage_instruction_hex', 'Fetch_stage_instruction_asm', 'Fetch_stage_instruction_mnemonic']]
    
    # Write the result to the output CSV
    output_csv_path = os.path.join(output_csv_dir, output_csv_name)
    df.to_csv(output_csv_path, index=False)
    
    print(f"Converted instruction trace saved to {output_csv_path}")

def create_dir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
# Example usage
# convert_instruction_trace('input_instruction_trace.csv', 'output_instruction_trace.csv')

# Example usage
if __name__ == '__main__':
    INPUT_CSV_PATH = './dumptrace/fibo_instr_dump.csv'
    OUTPUT_CSV_DIR = './dumptrace_disasm'
    create_dir_if_not_exists(OUTPUT_CSV_DIR)
    OUTPUT_CSV_NAME = 'output_instruction_trace.csv'
    convert_instruction_trace(input_csv_path=INPUT_CSV_PATH,output_csv_dir=OUTPUT_CSV_DIR,output_csv_name=OUTPUT_CSV_NAME)
