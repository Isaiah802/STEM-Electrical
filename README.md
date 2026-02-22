# NLC STEM Club - UAV Electrical Systems

[![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)](https://github.com/Isaiah802/STEM-Electrical)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

## Project Overview

This repository contains all electrical systems design, documentation, and configuration files for the **NLC STEM Club Solar-Powered Environmental Monitoring UAV Project**. This is a high-impact, interdisciplinary effort to design, build, and fly a hybrid solar-powered drone for environmental research.

### Mission Statement

Create a fully-functional, hybrid solar-powered UAV that can collect critical environmental data (air quality, temperature, humidity) while demonstrating extended flight time through solar energy integration.

### Predicted UAV Parameters

| Parameter | Specification |
|-----------|--------------|
| **Weight** | 4-6 lbs (including electronics and payload) |
| **Frame Size** | 250mm quadcopter (motor-to-motor diagonal) |
| **Flight Time** | 15-25 minutes (extended via solar charging) |
| **Battery** | 4S 2200mAh LiPo (14.8V nominal) |
| **Sensors** | VOC, CO₂, Temperature, Humidity, GPS |

## Repository Structure

```
STEM-Electrical/
├── Background_info/          # Project context and planning documents
│   ├── Project_overview.txt
│   ├── Project_parts_list.txt
│   ├── constitution.txt
│   └── recent_design_decisions.txt
├── LaTex_files/              # LaTeX source files (13 documents)
│   ├── Circuit_Fundamentals_Teaching_Guide.tex
│   ├── Component_Quick_Reference_Card.tex
│   ├── Lesson_2_Schematics_and_Troubleshooting.tex
│   ├── Meeting_1_Agenda.tex
│   ├── Power_Budget_Analysis.tex
│   ├── Project_Overview.tex
│   ├── Safety_Protocol.tex
│   ├── TEAM_LEAD_ACTION_CHECKLIST.tex
│   └── [5 more .tex files]
├── PDFs/                     # Compiled PDF documentation (13 files)
│   ├── Circuit_Fundamentals_Teaching_Guide.pdf
│   ├── Component_Quick_Reference_Card.pdf
│   ├── Lesson_2_Schematics_and_Troubleshooting.pdf
│   ├── Meeting_1_Agenda.pdf
│   ├── Power_Budget_Analysis.pdf
│   ├── Safety_Protocol.pdf
│   └── [7 more PDFs]
├── txt_files/                # Plain text working documents
│   ├── Component_Quick_Reference_Card.txt
│   ├── Lesson_2_Schematics_and_Practical_Troubleshooting.txt
│   ├── Power_Budget_Analysis.txt
│   ├── Safety_Protocol.txt
│   └── [6 more .txt files]
├── compile_latex.py          # Automated LaTeX compilation script
├── create_latex_documents.py # Document generation automation
└── create_parts_checklist.py # Parts inventory management

```

## Key Documentation

### For Team Members

- **[Safety Protocol PDF](PDFs/Safety_Protocol.pdf)** - **MANDATORY READ** before handling any components
- **[Team Lead Action Checklist PDF](PDFs/TEAM_LEAD_ACTION_CHECKLIST.pdf)** - Timeline and task breakdown
- **[Subsystem Assignment Detailed PDF](PDFs/Subsystem_Assignment_Detailed.pdf)** - Individual team assignments
- **[Technical Terminology Definitions PDF](PDFs/Technical_Terminology_Definitions.pdf)** - Reference guide
- **[Component Quick Reference Card PDF](PDFs/Component_Quick_Reference_Card.pdf)** - Fill-in template for tracking all component specifications, testing, and configurations

### Educational Resources

- **[Lesson 1: Circuit Fundamentals Teaching Guide PDF](PDFs/Circuit_Fundamentals_Teaching_Guide.pdf)** - Complete electrical theory tutorial with UAV examples and practice problems
- **[Lesson 2: Reading Schematics & Troubleshooting PDF](PDFs/Lesson_2_Schematics_and_Troubleshooting.pdf)** - How to read datasheets, use multimeters, understand PWM signals, and systematically debug electrical problems

### For Project Planning

- **[Power Budget Analysis PDF](PDFs/Power_Budget_Analysis.pdf)** - Complete power system calculations
- **[Project Parts List PDF](PDFs/Project_Parts_List.pdf)** - Component inventory and specifications
- **[Recent Design Decisions](Background_info/recent_design_decisions.txt)** - Architecture decisions and rationale

## Project Timeline

### Phase 1: Design & Planning (Weeks 1-3)
- ✅ Finalize component selection
- ✅ Create power budget analysis
- ✅ Establish safety protocols
- ✅ Assign subsystem teams

### Phase 2: Fabrication & Assembly (Weeks 4-6) - **CURRENT PHASE**
- 🔄 Team soldering training (Feb 24-27)
- 🔄 Component wiring and assembly (Feb 28 - Mar 6)
- ⏳ Initial system testing
- ⏳ Power system integration

### Phase 3: Integration & Testing (Weeks 7-9)
- ⏳ Full system integration
- ⏳ Flight controller configuration
- ⏳ Sensor calibration
- ⏳ Ground and flight testing

### Phase 4: Data Collection & Reporting (Week 10)
- ⏳ Environmental data collection flights
- ⏳ Final report compilation
- ⏳ Presentation preparation

**Legend:** ✅ Complete | 🔄 In Progress | ⏳ Upcoming

## Major Subsystems

### 1. Power System
- **Battery**: 4S 2200mAh 30C LiPo
- **ESC**: 30A with integrated 5V/3A BEC (for flight controller)
- **External UBEC**: 5V 6A (for servos and high-draw peripherals)
- **Solar Integration**: 18V solar panels with MPPT charge controller

### 2. Flight Control
- **Flight Controller**: APM 2.8 or compatible
- **GPS Module**: NEO-M8N with compass
- **RC Receiver**: 6+ channel 2.4GHz
- **Telemetry**: Optional 433MHz/915MHz radio

### 3. Research Payload
- **Arduino Nano**: Sensor data collection
- **BME280**: Temperature, humidity, pressure sensor
- **Air Quality**: VOC/CO₂ sensor
- **MicroSD Module**: Local data logging

### 4. Servos & Control Surfaces
- **Servo Type**: 9g micro servos (4x)
- **Control**: Elevator, rudder, ailerons/flaps
- **Power**: Dedicated 5V rail from external UBEC

## Automation Scripts

### compile_latex.py
Compiles all LaTeX documents to PDFs automatically.
```bash
python compile_latex.py
```

### create_latex_documents.py
Generates LaTeX files from text templates.
```bash
python create_latex_documents.py
```

### create_parts_checklist.py
Creates Excel spreadsheet for parts inventory tracking.
```bash
python create_parts_checklist.py
```

### fix_unicode_latex.py
Removes Unicode characters from LaTeX files for compatibility.
```bash
python fix_unicode_latex.py
```

## Safety Guidelines

⚠️ **CRITICAL SAFETY REQUIREMENTS** ⚠️

### LiPo Battery Handling
- Store batteries in LiPo safety bag at ALL times
- Never charge unattended
- Check cell voltages before each use (3.7V ± 0.1V per cell)
- Disconnect battery immediately after use
- Keep fire extinguisher nearby during charging

### Electrical Work
- Always disconnect battery before wiring
- Test for short circuits with multimeter before powering
- Use heat shrink tubing on all solder joints
- Wear safety glasses during soldering

### Propeller Safety
- Remove propeller for ALL bench testing indoors
- Establish 10-meter safety perimeter for motor tests
- Never reach toward spinning propeller
- Shout "PROPELLER TEST" before any outdoor motor test

**📖 Read the complete [Safety Protocol PDF](PDFs/Safety_Protocol.pdf) before starting any work!**

## Team Structure

- **Electronics & Power Team Lead**: [Your Name]
- **Mechanical & Structural Team**: Frame design and 3D printing
- **Software & Data Team**: Flight code and data analysis
- **Documentation & Reporting Team**: Progress tracking and final report

## Getting Started

### For New Team Members

1. **Read Safety Documentation**
   - Review [Safety Protocol PDF](PDFs/Safety_Protocol.pdf)
   - Understand LiPo battery handling procedures
   - Familiarize yourself with emergency procedures

2. **Review Technical Documentation**
   - Read [Project Overview PDF](PDFs/Project_Overview.pdf)
   - Check your assignment in [Subsystem Assignment Detailed PDF](PDFs/Subsystem_Assignment_Detailed.pdf)
   - Review [Technical Terminology Definitions PDF](PDFs/Technical_Terminology_Definitions.pdf)

3. **Complete Training**
   - Attend soldering basics workshop
   - Learn multimeter usage
   - Complete practice exercises before working on real components

4. **Join Communication Channels**
   - Join Discord server (link in team contact info)
   - Subscribe to repository notifications
   - Review meeting schedule

### Prerequisites

- Python 3.7+ (for automation scripts)
- LaTeX distribution (TeX Live, MikTeX, or MacTeX) for document compilation
- Basic electronics knowledge (will be taught)
- Soldering skills (training provided)

## Contributing

### Team Members

1. Create a feature branch for your work: `git checkout -b feature/your-subsystem`
2. Document all design decisions and changes
3. Take photos of completed work for progress tracking
4. Submit pull request with clear description
5. Get review from team lead before merging

### External Contributors

This is a student club project. External contributions are welcome but please open an issue first to discuss proposed changes.

## Project Milestones

- **Week 1 (Feb 21-27, 2026)**: Team training, parts inventory, soldering practice
- **Week 2 (Feb 28 - Mar 6, 2026)**: Component assembly, power system wiring, initial testing
- **March 6 Deadline**: Progress report to club president
- **Week 10**: Final flight testing and data collection

## Resources

### Datasheets & Technical References
- Flight Controller: [APM 2.8 Documentation](https://ardupilot.org/copter/)
- GPS Module: NEO-M8N datasheet (in Background_info/)
- Battery: 4S LiPo charging and care guide
- Sensors: BME280, Air Quality sensor specifications

### Learning Materials
- [Circuit Fundamentals Teaching Guide PDF](PDFs/Circuit_Fundamentals_Teaching_Guide.pdf)
- [Circuit Fundamentals Teaching Guide (Text)](Circuit_Fundamentals_Teaching_Guide.txt)
- Soldering tutorial videos (links in team Discord)
- Multimeter usage guide (in Learning Modules)

### Vendor Links
- Amazon: Primary parts sourcing
- HobbyKing: RC components
- Adafruit: Sensors and Arduino components

## Troubleshooting

### Common Issues

**LaTeX Compilation Errors**
```bash
# Run the Unicode fix script first
python fix_unicode_latex.py

# Then compile
python compile_latex.py
```

**Parts Tracking**
- Update `UAV_Parts_Checklist.xlsx` as items arrive
- Mark items as "Received" with date
- Report any damaged/missing items immediately

**Technical Questions**
- Check [Technical Terminology Definitions PDF](PDFs/Technical_Terminology_Definitions.pdf)
- Ask in Discord #electrical channel
- Schedule 1-on-1 with team lead

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

**Project Lead**: [Your Name]
**Email**: [Your Email]
**Discord**: NLC STEM Club Server
**Meeting Times**: Tuesday & Thursday (check team schedule)

## Acknowledgments

- NLC STEM Club leadership for project support
- Club members for dedication and teamwork
- Faculty advisors for technical guidance

---

**Last Updated**: February 21, 2026  
**Next Milestone**: March 6, 2026 - Progress Report Due
