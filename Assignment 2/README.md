# <u>**Assigment 2 - SPICE SIMULATION**<\u>
[SPICE](https://ngspice.sourceforge.io/) is a circuit simulator primarily designed for IC Design.  There are many different variants of SPICE that are used in Electrical and Electronics, and there are many commercial variants as well.  

# Circuit Solving

A circuit can be represented as a *graph* - a structure that has *nodes* and *edges*.  Each node in the graph is a point where two or more elements meet.

![Simple circuit](circ1.png){ width=50% }

The circuit above shows a very simple example of a circuit.  Here there are 3 *nodes*: they are labeled `1`, `2` and `GND`, but the labels could be any string in general.  The node labeled `GND` is special - since voltages are relative, we need to select exactly one node in the circuit as the *ground* potential, and this is usually given the special label name `GND`. 

The circuit has a fixed independent voltage source $V_s$, and two known resistances $R_1$ and $R_2$.  We want to find the voltages at the nodes `1` and `2`, and also the current through the voltage source.

### Unknown values

To simplify the discussion, we can therefore assume that when we have *N* nodes in the circuit, there are *N* unknown voltages that we need to solve for.  In practice the `GND` node is known to be 0 V, so this is not really an unknown, but we can add it to the list of equations anyway.

This means that we can write Kirchhoff's current law (KCL) equations at each of the nodes, and will get *N* equations.  However, there are some problems:

- KCL equations at all *N* nodes will end up being redundant: they can only solve for *N-1* variables.  For instance, as long as the KCL equations at nodes `1` to `N-1` are satisfied, it will automatically imply that the `GND` node equation is also satisfied.  So this actually only gives us *N-1* equations.
- The current through a voltage source is not a direct function of the voltage, so in effect that current ($I_s$ in the example circuit above) is also unknown.  So we need some more equations to solve for these currents.

We can therefore add a few *auxiliary* equations here: for each independent voltage source, there is an equation relating the voltages at each of the end nodes.

In the example above, the relevant equations would be as follows:

#### Current balance
$$
\begin{aligned}
I_s               & + & \frac{V_1-V_2}{R_1}     & = & 0 \\
\frac{V_2-0}{R_2} & + & \frac{V_2-V_1}{R_1}     & = & 0 
\end{aligned}
$$

#### Voltage
$$
\begin{aligned}
V_1 & - & 0 & = & V_s
\end{aligned}
$$

which can be written in Matrix form as:

$$
\begin{bmatrix}
\frac{1}{R_1} & \frac{-1}{R_1} & 1 \\
\frac{-1}{R_1} & \frac{1}{R_1} + \frac{1}{R_2} & 0 \\
1 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
V_1 \\
V_2 \\
I_s
\end{bmatrix}
= \begin{bmatrix}
0 \\
0 \\
V_s
\end{bmatrix}
$$

## Circuit representation

We use a text based format to represent circuits.  For the example above, we can represent it as follows (the whitespace here is just for formatting, it does not have significance):

```spice
.circuit
Vs   1 GND  dc 2
R1   1   2     1    
R2   2 GND     1  
.end
```

Similarly, we could also have another circuit as follows:

![Voltage and Current sources](circ2.png){ width=50% }

```spice
.circuit
Vsource n1 GND dc 10
Isource n3 GND dc 1
R1 n1 n2 2
R2 n2 n3 5
R3 n2 GND 3
.end
```
The goal of this assignment is to **develop a Python function** that performs complete circuit simulation based on the text input format described above.

Your implementation should:

1. **Parse the circuit description**
   - Accept a **filename** as input.
   - Read the file, process each line, and extract components such as:
     - **Voltage sources (V)**
     - **Current sources (I)**
     - **Resistors (R)**  
   - Store them either as:
     - Separate lists (for each component type), or  
     - A unified list/dictionary containing:
       - Component name  
       - Connected node names  
       - Electrical value (resistance, voltage, or current magnitude)

2. **Identify and map circuit nodes**
   - Generate a list of all node names.  
   - Assign a unique integer index to each node.  
   - The **ground node (`GND`)** must always be assigned index `0`.  
   - Other nodes can be numbered arbitrarily (for example, `$n1$` does not necessarily have to correspond to index `1`).

3. **Formulate circuit equations**
   - Using the node mappings, construct the **system matrix** that represents the circuit equations.  
   - Implement the **Modified Nodal Analysis (MNA)** framework using `numpy` arrays.  
   - Each equation should represent Kirchhoff’s laws for the corresponding circuit nodes and branches.

4. **Solve the system**
   - Use any appropriate numerical solver (for instance, `numpy.linalg.solve`) to compute:
     - Node voltages (**V**)  
     - Branch currents (**I**)

---

## <u>**Return Values**</u>

Your function should return two Python objects:

```python
(V, I)
```

where:
- `V` → a dictionary mapping **node names** to their **computed voltages** (floats)  
- `I` → a dictionary mapping **voltage source names** to their **computed currents** (floats)

### Current Types:
- **Current through a constant current source**: fixed by input and need not be recomputed.  
- **Current through resistors**: can be determined directly from node voltages (Ohm’s Law).  
- **Current through voltage sources**: must be obtained from your computed solution and returned as part of the `I` dictionary.

---

## <u>**Error Handling and Validation**</u>

Your implementation must include **robust error handling** to detect and report invalid or inconsistent circuit definitions.  
Common issues to catch include:
- Missing `.circuit` or `.end` delimiters  
- Undefined nodes or floating nodes  
- Duplicate component names  
- Invalid numerical parameters or formatting errors  

Additional edge cases and validation checks are encouraged to ensure the reliability of your simulation code.

---

## <u>**Expected Output**</u>

After successful execution, the program should:
- Print or return the voltage at each node  
- Report the computed current through each voltage source  
- Confirm successful parsing and matrix construction steps  

This exercise emphasizes **algorithmic thinking**, **matrix formulation**, and **structured data handling** to simulate the behavior of electronic circuits in a SPICE-like environment.
