"""
LaTeX Document Generator for NLC STEM Club UAV Project
Converts all .txt files to professional LaTeX format
"""

import os
import re
from pathlib import Path

def create_latex_preamble(title, subtitle=""):
    """Generate standard LaTeX preamble"""
    return f"""\\documentclass[11pt,letterpaper]{{article}}

% Essential Packages
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{amsmath,amssymb}}
\\usepackage{{graphicx}}
\\usepackage{{circuitikz}}
\\usepackage{{tikz}}
\\usetikzlibrary{{shapes,arrows,positioning,calc}}
\\usepackage{{booktabs}}
\\usepackage{{multirow}}
\\usepackage{{xcolor}}
\\usepackage{{fancyhdr}}
\\usepackage{{tcolorbox}}
\\usepackage{{enumitem}}
\\usepackage{{float}}
\\usepackage{{listings}}
\\usepackage{{hyperref}}

% Colors
\\definecolor{{nlcblue}}{{RGB}}{{0,51,102}}
\\definecolor{{alertred}}{{RGB}}{{204,0,0}}
\\definecolor{{safgreen}}{{RGB}}{{0,128,0}}

% Header/Footer
\\pagestyle{{fancy}}
\\fancyhead[L]{{\\textbf{{NLC STEM Club UAV Project}}}}
\\fancyhead[R]{{\\textbf{{{title}}}}}
\\fancyfoot[C]{{\\thepage}}

% Title
\\title{{\\Huge\\textbf{{{title}}}\\\\
\\Large {subtitle}\\\\
\\large NLC STEM Club - Electrical Systems Team}}
\\author{{February 2026}}
\\date{{}}

\\begin{{document}}

\\maketitle
\\thispagestyle{{empty}}
\\newpage
"""

def escape_latex(text):
    """Escape special LaTeX characters and replace Unicode symbols"""
    import re
    
    # First, protect sequences that we'll handle specially
    # Replace consecutive underscores (10+ for fill-in blanks) with a placeholder
    underscore_blanks = []
    def save_underscore_blank(match):
        length = len(match.group())
        replacement = '\\underline{\\hspace{' + str(length * 0.15) + 'cm}}'
        underscore_blanks.append(replacement)
        return f'<<<BLANK{len(underscore_blanks)-1}>>>'
    
    text = re.sub(r'_{10,}', save_underscore_blank, text)
    
    # Replace Unicode characters with placeholders
    unicode_map = []
    unicode_replacements = {
        '☐': '$\\square$',
        '✓': '$\\checkmark$',
        '✗': '$\\times$',
        '🚨': '[CRITICAL]',
        '⚠️': '[WARNING]',
        '⚠': '[WARNING]',
        '📋': '',
        '💡': '',
        '🚀': '',
        '⚡': '',
        '≡': '$\\equiv$',
        '→': '$\\rightarrow$',
        '←': '$\\leftarrow$',
        '°': '$^\\circ$',
        '×': '$\\times$',
        '÷': '$\\div$',
        '≈': '$\\approx$',
        '≤': '$\\leq$',
        '≥': '$\\geq$',
        '±': '$\\pm$',
        '•': '$\\bullet$',
        'Ω': '$\\Omega$',
        'Φ': '$\\Phi$',
        'μ': '$\\mu$',
        'π': '$\\pi$',
        # Box-drawing characters
        '│': '|',
        '─': '-',
        '┌': '+',
        '┐': '+',
        '└': '+',
        '┘': '+',
        '├': '+',
        '┤': '+',
        '┬': '+',
        '┴': '+',
        '┼': '+',
        '═': '=',
        '║': '|',
        '╔': '+',
        '╗': '+',
        '╚': '+',
        '╝': '+',
        '╠': '+',
        '╣': '+',
        '╦': '+',
        '╩': '+',
        '╬': '+',
    }
    
    for unicode_char, latex_replacement in unicode_replacements.items():
        if unicode_char in text:
            unicode_map.append(latex_replacement)
            text = text.replace(unicode_char, f'<<<UNICODE{len(unicode_map)-1}>>>')
    
    # Now escape special LaTeX characters
    replacements = {
        '&': '\\&',
        '%': '\\%',
        '$': '\\$',
        '#': '\\#',
        '_': '\\_',
        '{': '\\{',
        '}': '\\}',
        '~': '\\textasciitilde{}',
        '^': '\\textasciicircum{}',
    }
    
    for char, replacement in replacements.items():
        if char in text:
            text = text.replace(char, replacement)
    
    # Restore Unicode replacements
    for i, latex_code in enumerate(unicode_map):
        text = text.replace(f'<<<UNICODE{i}>>>', latex_code)
    
    # Restore underscore blanks
    for i, blank_code in enumerate(underscore_blanks):
        text = text.replace(f'<<<BLANK{i}>>>', blank_code)
    
    return text

def convert_txt_to_latex(input_file, output_file, title, subtitle=""):
    """Convert txt file to LaTeX with basic formatting"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    latex_content = create_latex_preamble(title, subtitle)
    
    # Split into lines
    lines = content.split('\n')
    
    in_list = False
    skip_table_line = False
    
    for line in lines:
        # Skip ASCII art header/footer lines (═══, ───, etc.)
        if all(c in '═─│┌┐└┘┏┓┗┛━├┤┬┴┼╔╗╚╝║╠╣╦╩╬' + ' ' for c in line) and len(line) > 20:
            continue
        
        # Skip box corners and single-line boxes  
        if line.strip() and all(c in  '┌┐└┘─│' + ' ' for c in line):
            continue
            
        # Handle table header lines with box drawing
        if '│' in line and len(line) > 30:
            # Convert to bold subsection
            content_text = line.replace('│', '').strip()
            if content_text:
                if in_list:
                    latex_content += "\\end{itemize}\n\n"
                    in_list = False
                latex_content += f"\\subsection*{{{content_text}}}\n\n"
            continue
        
        # Detect section headers (ALL CAPS with spaces, not in tables)
        if line.strip() and line.strip().isupper() and len(line.strip()) > 5 and '|' not in line:
            if in_list:
                latex_content += "\\end{itemize}\n\n"
                in_list = False
            section_name = escape_latex(line.strip())
            latex_content += f"\\section{{{section_name}}}\n\n"
            continue
        
        # Detect subsections (Title Case with colon)
        if re.match(r'^[A-Z][a-z].*:$', line.strip()):
            if in_list:
                latex_content += "\\end{itemize}\n\n"
                in_list = False
            subsection = escape_latex(line.strip().rstrip(':'))
            latex_content += f"\\subsection{{{subsection}}}\n\n"
            continue
        
        # Detect bullet points or list items
        if line.strip().startswith(('•', '-', '*', '☐', '✓', '✗')) and not line.strip().startswith('---'):
            if not in_list:
                latex_content += "\\begin{itemize}\n"
                in_list = True
            # Remove bullet and escape text
            item_text = line.strip()[1:].strip() if line.strip()[0] in '•-*' else line.strip()[2:].strip()
            latex_content += f"  \\item {escape_latex(item_text)}\n"
            continue
        elif in_list and line.strip() == '':
            latex_content += "\\end{itemize}\n\n"
            in_list = False
            continue
        
        # Handle indented sub-items (starts with spaces and not empty)
        if line.startswith(('  ', '\t')) and line.strip() and not line.strip().startswith('---'):
            if not in_list:
                latex_content += "\\begin{itemize}\n"
                in_list = True
            item_text = line.strip()
            latex_content += f"  \\item {escape_latex(item_text)}\n"
            continue
        
        # Skip lines that look like table separators
        if line.strip().startswith('---') or line.strip().startswith('───'):
            continue
            
        # Regular text (skip empty lines that aren't breaking lists)
        if line.strip():
            if in_list:
                latex_content += "\\end{itemize}\n\n"
                in_list = False
            latex_content += escape_latex(line.strip()) + "\\par\n\n"
    
    if in_list:
        latex_content += "\\end{itemize}\n\n"
    
    latex_content += "\\end{document}\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"✓ Created: {output_file}")

def main():
    """Convert all txt files to LaTeX"""
    
    print("=" * 80)
    print("NLC STEM Club UAV - LaTeX Document Generator")
    print("=" * 80)
    print()
    
    # Define base directory
    base_dir = Path(".")
    latex_dir = base_dir / "LaTex_files"
    latex_dir.mkdir(exist_ok=True)
    
    # Files to convert
    conversions = [
        # txt_files directory
        ("txt_files/Power_Budget_Analysis.txt", "Power_Budget_Analysis.tex", 
         "Power Budget Analysis", "Electrical System Energy Calculations"),
        
        ("txt_files/Safety_Protocol.txt", "Safety_Protocol.tex",
         "Safety Protocol", "LiPo Handling and Electrical Safety"),
        
        ("txt_files/Technical_Terminology_Definitions.txt", "Technical_Terminology_Definitions.tex",
         "Technical Terminology \\& Definitions", "Reference Guide for Electrical Team"),
        
        ("txt_files/Meeting_1_Agenda.txt", "Meeting_1_Agenda.tex",
         "First Meeting Agenda", "Electrical Team Kickoff"),
        
        ("txt_files/Subsystem_Assignment_Detailed.txt", "Subsystem_Assignment_Detailed.tex",
         "Subsystem Assignments", "Team Organization and Responsibilities"),
        
        ("txt_files/README_Scripts.txt", "README_Scripts.tex",
         "Documentation Scripts Guide", "How to Use Automation Tools"),
        
        # Root directory files
        ("TEAM_LEAD_ACTION_CHECKLIST.txt", "TEAM_LEAD_ACTION_CHECKLIST.tex",
         "Team Lead Action Checklist", "March 6 Deadline Preparation"),
        
        # Background info
        ("Background_info/Project_overview.txt", "Project_Overview.tex",
         "Project Overview", "3D-Printed Solar Floatplane UAV"),
        
        ("Background_info/Project_parts_list.txt", "Project_Parts_List.tex",
         "Complete Parts List", "Components and Costs"),
        
        ("Background_info/recent_design_decisions.txt", "Recent_Design_Decisions.tex",
         "Design Decisions Log", "Engineering Choices and Rationale"),
    ]
    
    for input_rel, output_name, title, subtitle in conversions:
        input_file = base_dir / input_rel
        output_file = latex_dir / output_name
        
        if input_file.exists():
            try:
                convert_txt_to_latex(input_file, output_file, title, subtitle)
            except Exception as e:
                print(f"✗ Error converting {input_file}: {e}")
        else:
            print(f"⚠ File not found: {input_file}")
    
    print()
    print("=" * 80)
    print("Conversion Complete!")
    print("=" * 80)
    print(f"\\nLaTeX files created in: {latex_dir}")
    print("\\nNote: Complex documents (Block Diagram, Wiring Diagram) created manually")
    print("      for professional circuitikz circuit diagrams.")
    print()

if __name__ == "__main__":
    main()
