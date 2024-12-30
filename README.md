# Main Clock and PAL Carrier Simulation for Atari 8-bit PAL Computers

This project provides a simulation of the main clock and PAL carrier signals for Atari 8-bit PAL computers. The simulation is based on a schematic developed and tested in a circuit simulation environment.

## Overview

The goal of this project is to simulate the generation of a PAL carrier signal and verify the integrity of clock signals for Atari 8-bit PAL computers. The design utilizes common components like flip-flops (74LS74) and a crystal oscillator, as well as discrete components such as resistors, capacitors, and transistors.

## Files in the Repository

- **`schematic.png`**: A schematic diagram of the circuit.
- **`simulation.png`**: Transient analysis of the simulated circuit, showing key signals like `OSC`, `PALCARRIER`, and other test points.
- **`README.md`**: This documentation file explaining the project.
- **`microcap/`**: MicroCap simulation files.

## Circuit Details

The circuit includes:

1. **Crystal Oscillator**:
   - A 3.546894 MHz crystal (`Y1`) is used for generating the primary clock signal (`OSC`).
   - A second 4.433618 MHz crystal (`Y2`) is used for generating the PAL carrier signal.

2. **Flip-Flops (74LS74)**:
   - Two flip-flops are configured to divide the frequency and produce stable clock signals at different phases.

3. **Passive Filters**:
   - RC and LC filters are used to shape the signals and reduce high-frequency noise.

4. **Discrete Transistor Amplifiers**:
   - Transistors (`Q6`, `Q8`) are used to amplify and buffer the signals for stability and drive capability.

5. **Test Points**:
   - Several test points (`TP1`, `PALCARRIER`) are defined to observe and verify signal behavior.

## Simulation Results

The simulation demonstrates the following:

- The primary oscillator (`OSC`) generates a clean signal with minimal jitter.
- The PAL carrier signal (`PALCARRIER`) is stable and aligns with the expected frequency (4.433618 MHz).
- The output signals have the desired waveform shapes, suitable for further use in Atari 8-bit PAL systems.

### Screenshots

- **`schematic.png`**: A detailed view of the circuit schematic.
- **`simulation.png`**: A transient analysis output showing signal behavior over time.

## How to Use

1. Load the schematic into a circuit simulator MicroCap.
2. Run the transient analysis to observe the signal waveforms.

## Author

Peter D. Kaczorowski

## License

This project is released under the MIT License. See the LICENSE file for more details.

---

If you have any questions or suggestions, feel free to open an issue or submit a pull request!

