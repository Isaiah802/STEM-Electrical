===============================================================================
NLC STEM CLUB UAV PROJECT - DOCUMENTATION SCRIPTS
===============================================================================

This folder contains two Python scripts to generate professional presentation
and PDF documentation for your electrical team meeting.

===============================================================================
QUICK START GUIDE
===============================================================================

STEP 1: Install Required Libraries
-----------------------------------
Open PowerShell in this folder and run:

    pip install python-pptx reportlab

This installs both required libraries (takes ~30 seconds).


STEP 2: Generate PowerPoint Presentation (1-Hour Meeting)
----------------------------------------------------------
Run:
    python create_presentation.py

Output: NLC_UAV_Electrical_Meeting_Presentation.pptx
  • 18 professional slides
  • Optimized for 1-hour meeting format
  • Covers: architecture, power budget, safety, subsystems, action items
  • Ready to present immediately


STEP 3: Convert All Text Files to Professional PDFs
----------------------------------------------------
Run:
    python create_pdfs.py

Output: Creates "PDFs/" folder containing:
  • Power_Budget_Analysis.pdf (with cover page)
  • Electrical_System_Block_Diagram.pdf (with cover page)
  • Detailed_Wiring_Diagram.pdf (with cover page)
  • Safety_Protocol.pdf (with cover page)
  • Meeting_1_Agenda.pdf (with cover page)
  • Subsystem_Assignment_Detailed.pdf (with cover page)
  • MEETING_PREPARATION_SUMMARY.pdf (with cover page)

All PDFs include:
  ✓ Professional cover pages with project branding
  ✓ Headers showing document title
  ✓ Page numbers in footer
  ✓ Properly formatted ASCII diagrams
  ✓ Section/subsection headers
  ✓ Ready for printing


===============================================================================
WHAT EACH SCRIPT DOES
===============================================================================

create_presentation.py
----------------------
Generates a PowerPoint presentation covering:

Slide Layout (18 slides total):
  1. Title slide
  2. Meeting agenda (60 minutes)
  3. Project overview
  4. Key components (two-column layout)
  5. Critical architecture decision (Dual-BEC)
  6. Power architecture diagram (ASCII art)
  7. Power budget summary
  8. Safety protocols (RED ALERT FORMATTING)
  9. Four subsystems overview
  10-13. Individual subsystem details (Power, Flight, Payload, Testing)
  14. Week 1-2 milestones (two-column)
  15. Critical action items (RED ALERT)
  16. Resources & documentation
  17. Questions & Discussion
  18. Closing slide

Features:
  • Color-coded sections (blue headers, red alerts)
  • Professional branding (NLC STEM Club UAV Project)
  • Matching your Dual-BEC architecture decision
  • Safety emphasis throughout
  • Action-oriented content
  • 1-hour meeting timing (not 2.5-3 hours)


create_pdfs.py
--------------
Converts ALL .txt files in this folder to professional PDFs:

PDF Features:
  • Custom cover page for each document showing:
    - NLC STEM Club UAV Project branding
    - Document title
    - "Electrical Team - February 2026"
    - Professional footer
  
  • Document pages include:
    - Header with project name and document title
    - Decorative blue line under header
    - Page numbers centered in footer
    - Properly formatted body text
    - Monospace font for ASCII diagrams/code
    - Section headers (large, blue, bold)
    - Subsection headers (medium, blue, bold)
    - Justified body text with proper spacing
  
  • Automatic detection of:
    - ASCII art diagrams (preserves formatting)
    - Section headers (ALL CAPS or numbered)
    - Bullet points and lists
    - Indented technical content

Creates new folder "PDFs/" to keep organized.


===============================================================================
TROUBLESHOOTING
===============================================================================

Problem: "pip: command not found"
Solution: Python not installed or not in PATH.
  1. Verify Python installed: python --version
  2. If not installed, download from python.org
  3. During installation, CHECK "Add Python to PATH"

Problem: "python-pptx not found" or "reportlab not found"
Solution: Libraries not installed.
  Run: pip install python-pptx reportlab

Problem: Script runs but no output
Solution: Check for error messages in console.
  • For PowerPoint: Verify no existing file is open (close PowerPoint)
  • For PDFs: Check "PDFs/" folder was created

Problem: PDF formatting looks weird
Solution: Text files may have unusual characters.
  • The script handles most ASCII art automatically
  • If issues persist, check text file encoding (should be UTF-8)

Problem: "Permission denied" error
Solution: File is open in another program.
  • Close PowerPoint before re-running create_presentation.py
  • Close PDF viewer before re-running create_pdfs.py


===============================================================================
FOR YOUR MEETING
===============================================================================

BEFORE THE MEETING:
  1. Run both scripts to generate PowerPoint and PDFs
  2. Review the PowerPoint presentation (18 slides, ~3-4 min per slide)
  3. Print PDFs for distribution:
     - 1 copy per team member + 2 extras
     - ~90 pages total per set
     - Consider: Print Safety_Protocol.pdf separately (signature required)
  4. Test PowerPoint on meeting room equipment

DURING THE MEETING (1 hour):
  • 0-5 min: Introduction (Slides 1-3)
  • 5-20 min: Architecture & Power Budget (Slides 4-7)
  • 20-30 min: Safety Protocols (Slide 8) - Mandatory
  • 30-40 min: Subsystem Assignments (Slides 9-13)
  • 40-50 min: Action Plan (Slides 14-15)
  • 50-55 min: Resources & Q&A (Slides 16-17)
  • 55-60 min: Closing & Next Steps (Slide 18)

AFTER THE MEETING:
  • Collect signed Safety Protocol PDFs
  • Upload PowerPoint to shared drive
  • Order External 5V 6A UBEC within 24 hours


===============================================================================
TECHNICAL NOTES
===============================================================================

PowerPoint Specifications:
  • Dimensions: 10" × 7.5" (standard widescreen)
  • Colors: Navy blue (#003366) headers, Red (#CC0000) alerts
  • Fonts: Helvetica (body), Helvetica-Bold (headers)
  • Slide layouts: Title, Content, Two-Column, Blank

PDF Specifications:
  • Page size: US Letter (8.5" × 11")
  • Margins: 0.75" all sides
  • Fonts: Helvetica (body), Courier (code/diagrams)
  • Header: 0.5" from top with blue line separator
  • Footer: Page numbers 0.5" from bottom

Both scripts are fully self-contained - no external dependencies except
the two Python libraries (python-pptx and reportlab).


===============================================================================
FILE LISTING
===============================================================================

Scripts (Python):
  create_presentation.py    - PowerPoint generator (~500 lines)
  create_pdfs.py           - PDF converter (~400 lines)

Documentation (Text):
  Power_Budget_Analysis.txt
  Electrical_System_Block_Diagram.txt
  Detailed_Wiring_Diagram.txt
  Safety_Protocol.txt
  Meeting_1_Agenda.txt
  Subsystem_Assignment_Detailed.txt
  MEETING_PREPARATION_SUMMARY.txt

Generated (after running scripts):
  NLC_UAV_Electrical_Meeting_Presentation.pptx
  PDFs/
    Power_Budget_Analysis.pdf
    Electrical_System_Block_Diagram.pdf
    Detailed_Wiring_Diagram.pdf
    Safety_Protocol.pdf
    Meeting_1_Agenda.pdf
    Subsystem_Assignment_Detailed.pdf
    MEETING_PREPARATION_SUMMARY.pdf


===============================================================================
QUESTIONS?
===============================================================================

Both scripts include detailed error handling and will show clear error
messages if something goes wrong. Read the error message carefully - it
usually tells you exactly what needs to be fixed.

The scripts are designed to "just work" - no configuration needed.

Good luck with your meeting!

===============================================================================
