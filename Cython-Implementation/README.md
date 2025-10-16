# <u> **Cython Optimizations**
## **Objective**
The goal of this assignment is to implement and optimize the trapezoidal rule integration method using Python and Cython, and compare it with NumPy’s implementation.
## **Tasks**
1. Implement a pure Python function py_trapz(f, a, b, n) that calculates the definiteintegral of a function f from a to b using n trapezoids.
2. Create a Cython implementation cy_trapz(f, a, b, n) that performs the same calculation but utilizes Cython’s static typing and C-level optimizations for improved performance.
3. Use the NumPy function numpy.trapz() as a reference implementation.
4. Compare the performance and accuracy of all three implementations (Python, Cython, andNumPy) for the following test cases:
   
    a. f(x) = $$x^2$$ from 0 to 1   
    b. f(x) = $$sin(x)$$ from 0 to π   
    c. f(x) = $$e^x$$ from 0 to 1    
    d. f(x) = $$1/x$$ from 1 to 2     
   
5. Conduct a performance test by integrating f(x) = $$x^2$$ from 0 to 10 with 10 million trapezoids. Compare the execution times of all three implementations.
6. This repo contains Report- the documentation of my implementations, including:
    - The implementation details of my Python and Cython functions
    - The accuracy of each method compared to the known analytical solutions
    - The performance improvements achieved by my Cython implementation
    - A comparison of my implementations against the NumPy version
    - Challenges encountered during the Cython implementation and optimization process  


