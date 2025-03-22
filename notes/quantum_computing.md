# Quantum Computing

Explain how a quantum computer works, presenting all the passages with the appropriate mathematical formalism. Outline the differences with classical computing.

---

### **How a Quantum Computer Works: A Formal Approach**

Quantum computing operates on principles from quantum mechanics, utilizing **qubits** instead of classical bits. The fundamental differences arise from **superposition**, **entanglement**, and **quantum interference**, which enable quantum computers to solve certain problems exponentially faster than classical computers.

## **1. Classical vs. Quantum Computing**

### **1.1 Classical Computing**

A classical computer uses **bits** ($0$ or $1$) as the basic unit of information. Computation is performed using logic gates that manipulate these bits deterministically.

A classical bit can be represented as:

$$
\mathbf{b} \in \{0,1\}
$$

A classical state of an $n$-bit register is a vector in $\{0,1\}^n$.

### **1.2 Quantum Computing**

A quantum computer uses **qubits**, which can exist in **superposition** states. A single qubit is described as:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad \text{where } \alpha, \beta \in \mathbb{C} \text{ and } |\alpha|^2 + |\beta|^2 = 1.
$$

The vector $|\psi\rangle$ belongs to a two-dimensional Hilbert space $\mathbb{C}^2$, where $|0\rangle = (1,0)^T$ and $|1\rangle = (0,1)^T$.

## **2. Quantum Registers and Superposition**

For an $n$-qubit quantum system, the state is a superposition of all $2^n$ computational basis states:

$$
|\Psi\rangle = \sum\_{x=0}^{2^n - 1} c_x |x\rangle, \quad \text{where } c_x \in \mathbb{C} \text{ and } \sum |c_x|^2 = 1.
$$

This ability to represent all possible states simultaneously is called **quantum parallelism**.

## **3. Quantum Gates and Quantum Circuits**

Unlike classical logic gates, quantum gates are **unitary transformations** that preserve norm:

$$
U^\dagger U = I.
$$

### **3.1 Single-Qubit Gates**

#### **Pauli Matrices**:

$$
X =
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix},\quad
Y =
\begin{bmatrix}
0 & -i \\
i & 0
\end{bmatrix},\quad
Z =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}.
$$

#### **Hadamard Gate $H$**: Creates superposition.

$$
H = \frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}.
$$

Applying $H$ to $|0\rangle$ gives:

$$
H|0\rangle = \frac{1}{\sqrt{2}} \left(|0\rangle + |1\rangle\right).
$$

### **3.2 Multi-Qubit Gates**

**CNOT (Controlled-NOT) Gate**:

$$
\text{CNOT} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}.
$$

It entangles two qubits.

## **4. Quantum Entanglement**

Entanglement occurs when a multi-qubit state cannot be written as a product of individual qubit states.

Example: The **Bell state**:

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$

has non-factorizable correlations, enabling quantum teleportation and superdense coding.

## **5. Quantum Measurement**

A measurement collapses a quantum state into a classical outcome:

$$
\mathbb{P}(\text{measuring } |x\rangle) = |c_x|^2.
$$

Measurement is represented by projection operators $P_x = |x\rangle \langle x|$.

## **6. Differences Between Quantum and Classical Computing**

| Feature              | Classical Computing               | Quantum Computing                                      |
| -------------------- | --------------------------------- | ------------------------------------------------------ |
| **Information unit** | Bit: $0$ or $1$                   | Qubit: $\alpha\mid 0\rangle + \beta \mid 1\rangle$     |
| **Storage**          | $n$-bit register stores one value | $n$-qubit system stores $2^n$ coefficients             |
| **Computation**      | Deterministic, sequential         | Superposition allows parallelism                       |
| **Logic Gates**      | AND, OR, NOT, XOR, NAND, NOR      | Unitary transformations (e.g., Hadamard, CNOT, T-gate) |
| **Entanglement**     | No classical equivalent           | Nonlocal correlations exist                            |
| **Measurement**      | Reads exact value                 | Collapses wavefunction                                 |

## **7. Quantum Speedups and Applications**

Quantum computers offer exponential speedups in:

- **Shor’s Algorithm** ($\mathcal{O}(\log^3 N)$ for integer factorization)
- **Grover’s Algorithm** ($\mathcal{O}(\sqrt{N})$ for search problems)

These outperform classical algorithms, demonstrating quantum advantage.

### **Conclusion**

Quantum computers leverage **superposition, entanglement, and interference** to process information in fundamentally new ways. Their potential to revolutionize cryptography, optimization, and material science makes them a powerful frontier in computing.

---

Make an example of a simple quantum computing algorithm, explaining all the passages with the appropriate mathematical formalism.

---

Below is an example of the **Deutsch algorithm**—one of the simplest quantum algorithms that illustrates quantum parallelism and interference. This algorithm determines whether a Boolean function

$$
f:\{ 0,1\} \to \{ 0,1 \}
$$

is constant (same output for both inputs) or balanced (different outputs for the two inputs) with a single evaluation (query) of the function, compared to two queries classically.

---

## 1. The Problem Setting

We have a function $f$ with the promise that it is either constant or balanced. Classically, one must evaluate $f(0)$ and $f(1)$ to decide. The Deutsch algorithm uses quantum superposition and interference to decide with one oracle call.

The function is implemented by an oracle (or black box) represented as a unitary operator $U_f$ defined by:

$$
U_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle,
$$

where $\oplus$ denotes addition modulo 2.

---

## 2. The Quantum Circuit and Initial State

The algorithm uses two qubits:

- The **first qubit** holds the input $x$.
- The **second qubit** is an auxiliary qubit (also called the ancilla).

The initial state is chosen as:

$$
|\psi_0\rangle = |0\rangle \otimes |1\rangle = |0\rangle|1\rangle.
$$

---

## 3. Applying the Hadamard Transform

Next, we apply the Hadamard gate $H$ to both qubits. The Hadamard gate acts as:

$$
H|0\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right), \quad H|1\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right).
$$

After applying $H$ to each qubit, the state becomes:

$$
|\psi_1\rangle = (H\otimes H)|0\rangle|1\rangle = \left(\frac{|0\rangle+|1\rangle}{\sqrt{2}}\right) \otimes \left(\frac{|0\rangle-|1\rangle}{\sqrt{2}}\right).
$$

Expanding this tensor product:

$$
|\psi_1\rangle = \frac{1}{2}\Big[ |0\rangle(|0\rangle-|1\rangle) + |1\rangle(|0\rangle-|1\rangle) \Big] = \frac{1}{2}\Big[|0\rangle|0\rangle - |0\rangle|1\rangle + |1\rangle|0\rangle - |1\rangle|1\rangle \Big].
$$

---

## 4. Oracle Operation $U_f$

We now apply the oracle $U_f$. Its action is defined by:

$$
U_f|x\rangle\Big(|0\rangle-|1\rangle\Big) = (-1)^{f(x)}|x\rangle\Big(|0\rangle-|1\rangle\Big).
$$

This works because, for the ancilla in the state \(\frac{|0\rangle - |1\rangle}{\sqrt{2}}\), we have:

$$
U_f|x\rangle\frac{|0\rangle - |1\rangle}{\sqrt{2}} = \frac{|x\rangle(|0\oplus f(x)\rangle - |1\oplus f(x)\rangle)}{\sqrt{2}} = (-1)^{f(x)}|x\rangle\frac{|0\rangle-|1\rangle}{\sqrt{2}}.
$$

Thus, applying $U_f$ to $|\psi_1\rangle$ gives:

$$
|\psi_2\rangle = \frac{1}{2}\Big[ (-1)^{f(0)}|0\rangle(|0\rangle-|1\rangle) + (-1)^{f(1)}|1\rangle(|0\rangle-|1\rangle)\Big].
$$

Factor out the common ancilla state:

$$
|\psi_2\rangle = \frac{1}{2}\left[ (-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle \right] \otimes \Big(|0\rangle-|1\rangle\Big).
$$

---

## 5. Final Hadamard on the First Qubit

Since the ancilla does not affect the decision, we now focus on the first qubit. We apply a Hadamard gate to the first qubit:

$$
H\left[ (-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle \right].
$$

Using the Hadamard transform:

$$
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle+|1\rangle), \quad H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle-|1\rangle),
$$

the state transforms as follows:

$$
|\psi_3\rangle = \frac{1}{2} \Big[ (-1)^{f(0)}\frac{|0\rangle+|1\rangle}{\sqrt{2}} + (-1)^{f(1)}\frac{|0\rangle-|1\rangle}{\sqrt{2}} \Big].
$$

Combine the terms:

$$
|\psi_3\rangle = \frac{1}{2\sqrt{2}} \Big[ \big((-1)^{f(0)}+(-1)^{f(1)}\big)|0\rangle + \big((-1)^{f(0)}-(-1)^{f(1)}\big)|1\rangle \Big].
$$

---

## 6. Measurement and Outcome

When we measure the first qubit, the outcome probabilities are determined by the coefficients:

**For outcome $|0\rangle$:**

$$
A_0 = \frac{(-1)^{f(0)} + (-1)^{f(1)}}{2\sqrt{2}}.
$$

**For outcome $|1\rangle$:**

$$
A_1 = \frac{(-1)^{f(0)} - (-1)^{f(1)}}{2\sqrt{2}}.
$$

There are two cases:

### **$f$ is constant:**

Then $f(0) = f(1)$ so that:

$$
(-1)^{f(0)} = (-1)^{f(1)}.
$$

Thus,

$$
A_0 = \frac{2(-1)^{f(0)}}{2\sqrt{2}} = \frac{(-1)^{f(0)}}{\sqrt{2}}, \quad A_1 = 0.
$$

Measurement will yield $|0\rangle$ with certainty.

### **$f$ is balanced:**

Then $f(0) \neq f(1)$, implying:

$$
(-1)^{f(0)} = -(-1)^{f(1)}.
$$

Thus,

$$
A_0 = 0, \quad A_1 = \frac{2(-1)^{f(0)}}{2\sqrt{2}} = \frac{(-1)^{f(0)}}{\sqrt{2}}.
$$

Measurement will yield $|1\rangle$ with certainty.

---

## 7. Summary of the Algorithm

- **Initialization:** Start with $|0\rangle|1\rangle$.
- **Superposition:** Apply Hadamard gates to create a superposition of states.
- **Oracle Query:** Use the oracle $U_f$ to imprint the function information as phase factors.
- **Interference:** Apply a final Hadamard to the first qubit to cause constructive or destructive interference.
- **Measurement:** The measurement of the first qubit directly reveals whether $f$ is constant ($|0\rangle$) or balanced ($|1\rangle$).

This example illustrates the power of quantum parallelism and interference: by querying the oracle once on a superposition state, we effectively evaluate the function on both inputs simultaneously.

---

This detailed walk-through combines the appropriate mathematical formalism with an explanation of each step, providing insight into how quantum algorithms can outperform classical ones in specific tasks.

---

Go into the details. Explain in depth, with technical details, how a three qubits system works.

---

## **Understanding a Three-Qubit Quantum System in Depth**

A **three-qubit quantum system** is a fundamental building block for larger quantum computations. It extends the principles of **superposition, entanglement, and quantum gate operations** to a higher-dimensional space. Below, we will explore the **mathematical formalism** governing the behavior of three qubits, their state representation, transformations, and entanglement properties.

---

## **1. Hilbert Space Representation for Three Qubits**

Each qubit exists in a two-dimensional **Hilbert space** $\mathcal{H}_2$. A system of **three qubits** resides in the tensor product space:

$$
\mathcal{H}\_8 = \mathcal{H}\_2 \otimes \mathcal{H}\_2 \otimes \mathcal{H}\_2
$$

which is an **8-dimensional complex vector space** $\mathbb{C}^8$ spanned by the **computational basis states**:

$$
\{ |000\rangle, |001\rangle, |010\rangle, |011\rangle, |100\rangle, |101\rangle, |110\rangle, |111\rangle \}
$$

### **General State of a Three-Qubit System**

A general quantum state for three qubits is given by a **linear superposition**:

$$
|\Psi\rangle = \sum\_{x=0}^{7} c_x |x\rangle = c_0 |000\rangle + c_1 |001\rangle + c_2 |010\rangle + c_3 |011\rangle + c_4 |100\rangle + c_5 |101\rangle + c_6 |110\rangle + c_7 |111\rangle
$$

where $c_i \in \mathbb{C}$ are complex probability amplitudes satisfying the **normalization condition**:

$$
\sum\_{i=0}^{7} |c_i|^2 = 1
$$

---

## **2. Representation Using Tensor Products**

Each **basis state** is formed by the **tensor product** of individual qubits:

$$
|q_1 q_2 q_3\rangle = |q_1\rangle \otimes |q_2\rangle \otimes |q_3\rangle
$$

For example:

- $|000\rangle = |0\rangle \otimes |0\rangle \otimes |0\rangle$
- $|101\rangle = |1\rangle \otimes |0\rangle \otimes |1\rangle$

Using **vector notation**, we write:

$$
|0\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad |1\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

The tensor product of three qubits follows:

$$
|000\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \otimes \begin{bmatrix} 1 \\ 0 \end{bmatrix} \otimes \begin{bmatrix} 1 \\ 0 \end{bmatrix} =
\begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}
$$

Similarly, for $|101\rangle$:

$$
|101\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \otimes \begin{bmatrix} 1 \\ 0 \end{bmatrix} \otimes \begin{bmatrix} 0 \\ 1 \end{bmatrix} =
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}
$$

---

## **3. Quantum Operations on Three-Qubit Systems**

### **3.1 Single-Qubit Gates in Three-Qubit Systems**

A **single-qubit gate** acting on a specific qubit extends to the full three-qubit system using the **Kronecker product**.

For a **Hadamard gate** ($H$) acting on the first qubit:

$$
H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

The full transformation matrix in three-qubit space is:

$$
H \otimes I \otimes I =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & -1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & -1
\end{bmatrix}
$$

Applying $H$ to $|000\rangle$ gives:

$$
H |000\rangle = \frac{1}{\sqrt{2}} (|000\rangle + |100\rangle)
$$

---

### **3.2 Multi-Qubit Gates**

The **CNOT (Controlled-NOT) gate** is a two-qubit gate that flips the target qubit if the control qubit is $|1\rangle$. Its matrix form in three-qubit space (control: first qubit, target: second qubit) is:

$$
\text{CNOT}\_{1,2} =
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

If we apply **CNOT** to $|110\rangle$, the result is:

$$
\text{CNOT}\_{1,2} |110\rangle = |100\rangle
$$

---

## **4. Entanglement in a Three-Qubit System**

A crucial entangled state in three-qubit systems is the **GHZ (Greenberger–Horne–Zeilinger) state**:

$$
|\text{GHZ}\rangle = \frac{1}{\sqrt{2}} (|000\rangle + |111\rangle)
$$

This state exhibits **global** entanglement: **measuring one qubit determines the states of all others**.

Another important state is the **W state**:

$$
|\text{W}\rangle = \frac{1}{\sqrt{3}} (|001\rangle + |010\rangle + |100\rangle)
$$

The **W state** is **robust** against measurement on a single qubit, unlike the **GHZ state**.

---

## **5. Measurement and Collapsing of States**

Measuring a three-qubit system collapses it into one of the eight computational basis states $|000\rangle, ..., |111\rangle$ with probability $|c_i|^2$.

For example, in the GHZ state:

$$
P(|000\rangle) = P(|111\rangle) = \frac{1}{2}
$$

If we measure the first qubit and obtain $|0\rangle$, the system collapses to $|000\rangle$.

---

### **Conclusion**

A three-qubit system allows for **quantum parallelism, entanglement, and non-classical correlations**, making it a core element of quantum computation. These properties enable **quantum algorithms, teleportation, and error correction techniques**.

---

Explain the latter phrase.

---

### **Explaining the Role of a Three-Qubit System in Quantum Algorithms, Teleportation, and Error Correction**

A **three-qubit quantum system** is a fundamental unit for several key quantum computing tasks. Below, we explore how it enables **quantum algorithms**, **quantum teleportation**, and **quantum error correction** through its properties of **superposition, entanglement, and measurement**.

---

## **1. Three-Qubit System in Quantum Algorithms**

Quantum algorithms exploit **superposition and entanglement** to perform computations more efficiently than classical methods. Here’s how a three-qubit system is relevant:

### **1.1 Quantum Parallelism**

A classical 3-bit register can store only **one** of the $2^3 = 8$ possible states at a time. However, a **three-qubit** quantum register can store a **superposition** of all eight states:

$$
|\Psi\rangle = \frac{1}{\sqrt{8}} (|000\rangle + |001\rangle + |010\rangle + |011\rangle + |100\rangle + |101\rangle + |110\rangle + |111\rangle)
$$

This enables quantum parallelism, where an operation applied to $|\Psi\rangle$ affects all states simultaneously.

### **1.2 Quantum Fourier Transform (QFT)**

The **Quantum Fourier Transform (QFT)** is a crucial subroutine in quantum algorithms like **Shor's algorithm** (for factoring large numbers efficiently). The QFT maps a computational basis state $|j\rangle$ to a **superposition**:

$$
QFT |j\rangle = \frac{1}{\sqrt{N}} \sum\_{k=0}^{N-1} e^{2\pi i jk/N} |k\rangle
$$

For a three-qubit system ($N = 2^3 = 8$), this transformation enables efficient **period-finding**, which is central to breaking RSA encryption.

---

## **2. Three-Qubit System in Quantum Teleportation**

### **2.1 The Quantum Teleportation Protocol**

**Quantum teleportation** allows the transmission of an **unknown quantum state** using **entanglement** and **classical communication**. A three-qubit system is **necessary** because:

- **Two qubits** are used to share an **entangled Bell pair** between two parties (Alice and Bob).
- **One qubit** carries the **unknown state** to be teleported.

#### **Step-by-Step Process**

##### **Initial State**

Suppose Alice wants to send a qubit state:

$$
|\phi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

She and Bob share an entangled **Bell state**:

$$
|\beta*{00}\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)
$$

The total three-qubit system (Alice's qubit + Bell pair) is:

$$
|\Psi\rangle = |\phi\rangle \otimes |\beta*{00}\rangle
$$

**Bell Measurement on Alice’s Qubits**
Alice applies a **CNOT gate** followed by a **Hadamard gate** and measures her two qubits. This collapses Bob’s qubit into one of four possible states.

**Classical Communication**
Alice sends her **two classical measurement results** to Bob.

**Bob’s Recovery Operation**
Depending on Alice’s measurement result, Bob applies an appropriate quantum gate (Identity, $X$, $Z$, or $XZ$) to recover $|\phi\rangle$.

Thus, **Alice’s original quantum state is transferred to Bob without physical movement** of the qubit.

---

## **3. Three-Qubit System in Quantum Error Correction**

Quantum computers are prone to **errors** due to decoherence and imperfect gate operations. **Quantum Error Correction (QEC)** protects quantum information by **encoding one logical qubit into multiple physical qubits**.

### **3.1 The Three-Qubit Bit-Flip Code**

The **simplest quantum error-correcting code** uses three physical qubits to encode a **single logical qubit**:

$$
|0_L\rangle = |000\rangle, \quad |1_L\rangle = |111\rangle
$$

If a single qubit undergoes a **bit-flip error** ($|0\rangle \leftrightarrow |1\rangle$), the error state might be:

$$
|010\rangle \quad \text{or} \quad |100\rangle \quad \text{or} \quad |001\rangle
$$

A **majority vote** allows the correction of the error:

- If two qubits are $|0\rangle$ and one is $|1\rangle$, assume the error affected the **single $|1\rangle$** and flip it back.
- Similarly, if two are $|1\rangle$ and one is $|0\rangle$, flip the erroneous **$|0\rangle$**.

Thus, the logical state remains intact.

### **3.2 Detecting and Correcting Errors**

To detect errors without measuring the quantum state directly, we use **syndrome measurement**. This involves **ancilla qubits** and **parity-check operators**:

$$
Z_1 Z_2, \quad Z_2 Z_3
$$

Each parity check detects whether adjacent qubits differ, allowing correction without disturbing the quantum information.

### **3.3 Protection Against Phase-Flip Errors**

The bit-flip code does not protect against **phase errors** ($|+\rangle \leftrightarrow |-\rangle$). The **Shor Code** (using 9 qubits) extends error correction to phase-flip errors by encoding each qubit into a **three-qubit phase code**.

---

### **Conclusion**

A **three-qubit quantum system** is essential in quantum computing because:

- **Quantum algorithms** (like QFT and Grover's search) leverage three-qubit **superposition** for speedups.
- **Quantum teleportation** requires **three qubits** to send an unknown quantum state using **entanglement and classical communication**.
- **Quantum error correction** (bit-flip code) uses **three physical qubits** to protect a **single logical qubit** against errors.

These properties make three-qubit systems a **core foundation** of practical quantum computing.

---

Explain in detail QFT.

---

## **Quantum Fourier Transform (QFT) in Detail**

The **Quantum Fourier Transform (QFT)** is the quantum analog of the **Discrete Fourier Transform (DFT)**. It plays a crucial role in **quantum algorithms** such as **Shor’s algorithm** for integer factorization and quantum phase estimation.

---

# **1. Discrete Fourier Transform (DFT)**

In classical computation, the **Discrete Fourier Transform (DFT)** maps a vector

$$
x_0, x_1, \dots, x_{N-1}
$$

to another vector

$$
y_0, y_1, \dots, y_{N-1}
$$

using the formula:

$$
y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi i jk / N}, \quad k = 0, 1, ..., N-1
$$

where $e^{2\pi i / N}$ is the **primitive $N$-th root of unity**.

### **Key Features of the DFT**

- Converts a function from the **time domain** to the **frequency domain**.
- Used for signal processing and solving differential equations.

The **Quantum Fourier Transform (QFT)** applies the same transformation but in a quantum-mechanical setting.

---

# **2. Definition of Quantum Fourier Transform**

The **Quantum Fourier Transform** acts on a quantum state:

$$
|\psi\rangle = \sum_{j=0}^{N-1} x_j |j\rangle
$$

and transforms it into:

$$
QFT |\psi\rangle = \sum_{k=0}^{N-1} y_k |k\rangle
$$

where the amplitudes $y_k$ are given by:

$$
y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi i jk / N}
$$

For an **N-qubit system**, where $N = 2^n$, QFT can be efficiently implemented using **quantum gates**.

---

# **3. QFT on a Three-Qubit System ($N = 2^3 = 8$)**

In a **three-qubit system**, we have **8 basis states**:

$$
|0\rangle, |1\rangle, |2\rangle, ..., |7\rangle
$$

### **3.1 Matrix Representation of QFT for $N = 8$**

The QFT transformation for $N = 8$ is represented by the unitary matrix:

$$
QFT_8 =
\frac{1}{\sqrt{8}}
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & e^{2\pi i /8} & e^{4\pi i /8} & e^{6\pi i /8} & e^{8\pi i /8} & e^{10\pi i /8} & e^{12\pi i /8} & e^{14\pi i /8} \\
1 & e^{4\pi i /8} & e^{8\pi i /8} & e^{12\pi i /8} & e^{16\pi i /8} & e^{20\pi i /8} & e^{24\pi i /8} & e^{28\pi i /8} \\
1 & e^{6\pi i /8} & e^{12\pi i /8} & e^{18\pi i /8} & e^{24\pi i /8} & e^{30\pi i /8} & e^{36\pi i /8} & e^{42\pi i /8} \\
1 & e^{8\pi i /8} & e^{16\pi i /8} & e^{24\pi i /8} & e^{32\pi i /8} & e^{40\pi i /8} & e^{48\pi i /8} & e^{56\pi i /8} \\
1 & e^{10\pi i /8} & e^{20\pi i /8} & e^{30\pi i /8} & e^{40\pi i /8} & e^{50\pi i /8} & e^{60\pi i /8} & e^{70\pi i /8} \\
1 & e^{12\pi i /8} & e^{24\pi i /8} & e^{36\pi i /8} & e^{48\pi i /8} & e^{60\pi i /8} & e^{72\pi i /8} & e^{84\pi i /8} \\
1 & e^{14\pi i /8} & e^{28\pi i /8} & e^{42\pi i /8} & e^{56\pi i /8} & e^{70\pi i /8} & e^{84\pi i /8} & e^{98\pi i /8}
\end{bmatrix}
$$

This unitary matrix performs the QFT by **mixing all amplitudes** while preserving the inner product structure.

---

# **4. Quantum Circuit for QFT**

The QFT can be implemented efficiently using **Hadamard gates** and **controlled phase shift gates**.

### **4.1 Decomposition into Quantum Gates**

For an $n$-qubit system, the QFT can be implemented using the following steps:

1. **Apply a Hadamard gate ($H$)** to the first qubit.
2. **Apply controlled-phase gates** $R_k$ to introduce phase shifts based on other qubits.
3. **Repeat for remaining qubits**.

For a **three-qubit QFT**, the circuit consists of:

**Hadamard gates**: $H$
**Controlled phase gates** $R_k$ defined as:

$$
R_k =
\begin{bmatrix}
1 & 0 \\
0 & e^{2\pi i / 2^k}
\end{bmatrix}
$$

### **4.2 QFT Circuit for Three Qubits**

```
       ┌───┐       ┌───────────┐
q0 ────┤ H ├───────┤ R₂ (q1)  ├───────┐───────┐
       ├───┤       ├───────────┤       │       │
q1 ────┤ H ├───────┤ R₃ (q2)  ├───┐───┤ R₂  ├───┐
       ├───┤       ├───────────┤   │   ├───┐ │
q2 ────┤ H ├───────┤ R₄       ├───┘   ├───┘ │
       └───┘       └───────────┘       └───┘
```

Where:

- $R_2$ applies a phase shift of $e^{2\pi i / 4}$.
- $R_3$ applies a phase shift of $e^{2\pi i / 8}$.
- $R_4$ applies a phase shift of $e^{2\pi i / 16}$.

---

# **5. Complexity and Applications**

### **5.1 Complexity of QFT**

A naive implementation of the DFT requires **$O(N^2)$ operations**. However, QFT can be implemented in **$O(n^2)$**, which is exponentially faster.

### **5.2 Applications of QFT**

- **Shor’s Algorithm**: Finds the period of a function, which is crucial for integer factorization.
- **Quantum Phase Estimation**: Estimates the eigenvalues of unitary operators, important for quantum simulations.
- **Quantum Speedup**: Enables exponential acceleration in problems involving Fourier analysis.

---

# **Conclusion**

The **Quantum Fourier Transform (QFT)** is a core component of quantum computing, enabling efficient transformations in **logarithmic time**. Its ability to encode periodicity makes it fundamental to **Shor’s algorithm** and **quantum phase estimation**. Using a **Hadamard gate** and **controlled-phase shifts**, QFT efficiently transforms quantum states, achieving **exponential speedup over classical Fourier transforms**.
