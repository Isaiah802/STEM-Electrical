"""
LaTeX Document Compiler for NLC STEM Club UAV Project
Compiles all .tex files to PDFs
"""

import subprocess
import os
from pathlib import Path

def compile_latex(tex_file):
    """Compile a LaTeX file to PDF using pdflatex"""
    print(f"\\nCompiling {tex_file.name}...")
    
    # Change to LaTeX directory
    original_dir = os.getcwd()
    os.chdir(tex_file.parent)
    
    try:
        # Run pdflatex twice (for table of contents, references, etc.)
        for run in [1, 2]:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_file.name],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=30
            )
            
            if result.returncode != 0:
                print(f"  ✗ Error on run {run}")
                print(f"    Check {tex_file.stem}.log for details")
                return False
        
        print(f"  ✓ Successfully created {tex_file.stem}.pdf")
        return True
        
    except subprocess.TimeoutExpired:
        print(f"  ✗ Compilation timeout")
        return False
    except FileNotFoundError:
        print(f"  ✗ pdflatex not found. Please install LaTeX (MiKTeX or TeX Live)")
        return False
    finally:
        os.chdir(original_dir)

def clean_auxiliary_files(tex_dir):
    """Remove auxiliary LaTeX files (.aux, .log, .toc, etc.)"""
    extensions = ['.aux', '.log', '.toc', '.fdb_latexmk', '.fls', '.synctex.gz', '.out']
    
    for ext in extensions:
        for file in tex_dir.glob(f'*{ext}'):
            try:
                file.unlink()
            except:
                pass

def main():
    """Compile all LaTeX documents"""
    
    print("=" * 80)
    print("NLC STEM Club UAV - LaTeX Compiler")
    print("=" * 80)
    print()
    
    latex_dir = Path("LaTex_files")
    
    if not latex_dir.exists():
        print("✗ LaTeX_files directory not found!")
        return
    
    # Get all .tex files
    tex_files = sorted(latex_dir.glob("*.tex"))
    
    if not tex_files:
        print("✗ No .tex files found in LaTeX_files/")
        return
    
    print(f"Found {len(tex_files)} LaTeX documents to compile\\n")
    
    # Compile each file
    success_count = 0
    for tex_file in tex_files:
        if compile_latex(tex_file):
            success_count += 1
    
    print()
    print("=" * 80)
    print(f"Compilation Complete: {success_count}/{len(tex_files)} successful")
    print("=" * 80)
    print()
    
    # Move PDFs to PDFs folder
    pdf_dir = Path("PDFs")
    pdf_dir.mkdir(exist_ok=True)
    
    print("Moving PDFs to PDFs folder...")
    for tex_file in tex_files:
        pdf_file = tex_file.with_suffix('.pdf')
        if pdf_file.exists():
            target = pdf_dir / pdf_file.name
            pdf_file.replace(target)  # Use replace() to overwrite if exists
            print(f"  ✓ Moved {pdf_file.name}")
    print()
    
    # Ask about cleanup
    response = input("Clean up auxiliary files (.aux, .log, etc.)? [Y/n]: ")
    if response.lower() != 'n':
        clean_auxiliary_files(latex_dir)
        print("✓ Auxiliary files cleaned")
    
    print()
    print(f"PDFs available in: {pdf_dir.absolute()}")
    print()

if __name__ == "__main__":
    main()
