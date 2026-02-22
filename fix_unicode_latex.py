"""
Script to remove Unicode characters from LaTeX files and replace with text equivalents
"""

import os

def fix_unicode_in_file(filepath):
    """Fix Unicode characters in a LaTeX file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count original Unicode characters
    original_checkmarks = content.count('✓')
    original_xmarks = content.count('✗')
    original_checkboxes = content.count('☐')
    original_arrows = content.count('→')
    original_plusminus = content.count('±')
    original_degrees = content.count('°')
    original_subscript = content.count('₂')
    
    # Replace Unicode characters with LaTeX equivalents
    replacements = {
        '✓': '[DO]',
        '✗': '[DO NOT]',
        '☐': '[ ]',
        '→': '$\\rightarrow$',
        '±': '$\\pm$',
        '°': '$^\\circ$',
        '₂': '$_2$',
    }
    
    for unicode_char, replacement in replacements.items():
        content = content.replace(unicode_char, replacement)
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filepath}:")
    print(f"  - Checkmarks (✓): {original_checkmarks}")
    print(f"  - X marks (✗): {original_xmarks}")
    print(f"  - Checkboxes (☐): {original_checkboxes}")
    print(f"  - Arrows (→): {original_arrows}")
    print(f"  - Plus/minus (±): {original_plusminus}")
    print(f"  - Degrees (°): {original_degrees}")
    print(f"  - Subscript 2 (₂): {original_subscript}")
    
    return content

if __name__ == "__main__":
    # Fix Safety_Protocol.tex
    safety_protocol_path = os.path.join("LaTex_files", "Safety_Protocol.tex")
    if os.path.exists(safety_protocol_path):
        fix_unicode_in_file(safety_protocol_path)
        print("\nSafety_Protocol.tex has been fixed!")
    else:
        print(f"Error: {safety_protocol_path} not found")
