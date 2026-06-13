# How to build this project:
## On Linux or macOS:

1. Clone the repository to your local machine.
    ```bash
    git clone <repository-url>
    ```
2. Make sure you have a LaTeX distribution installed (e.g., TeX Live, MiKTeX). Latexmk is required for the optimized building process done through the Makefile. You might need to install additional LaTeX packages, which can usually be done through your distribution's package manager.
3. Navigate to the project directory and create a python virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install the required Python packages:
   ```bash
   pip install .
   ```
5. To build the PDF document, run the following command in the terminal:
   ```bash
   make
   ```
   This will run all the necessary python scripts and compile the LaTeX document into a PDF file.
   You can also run the command:
   ```bash
   make -j
   ```
   to speed up the build process by using multiple CPU cores. To learn more about the Makefile and the available commands, you can look at the comments in the Makefile itself.

## Brute-force method:

If you prefer to build the project without using the Makefile, you can follow the previous guide up to step 4. Then:
1. Run the necessary Python scripts to generate the required data and figures. You can find these scripts in the `scripts` directory. For example:
   ```bash
   python scripts/*.py
   ```
   Make sure to run all the scripts that are needed for the document.
2. Compile the LaTeX document manually using your preferred LaTeX editor or command line targetting the "analisi_statistica_dei_dati.tex" file. For example, you can use:
   ```bash
   pdflatex analisi_statistica_dei_dati.tex
   ```
**Warning**: This method of compiling the document is not optimized, and you may need to run the compilation command multiple times to resolve all references and citations correctly. Also the process may take significantly more time and auxiliary files may be left in the project directory, so it is recommended to use the Makefile for a more efficient and cleaner build process.

# Preface:

These notes are intended to be a comprehensive introduction to the field of statistical data analysis, covering both theoretical foundations and practical applications through examples, exercises, and tests. 

The material is organized into chapters that follow the _Analisi statistica dei dati_ course at the univeristy of Pisa, followed by the authors during the 2024-2026 academic years, and held by professors _Paolo Francavilla_, _Andrea Carlo Marini_ and _Giovanni Punzi_. 

For this reason, the text will follow their lecture notes very closely, and many of the formulations, examples, and concepts are taken directly from those sources, for which we thank the professors. It is by no means an exhaustive treatment, but we hope to leave the readers with a solid understanding of the core concepts and techniques in statistical data analysis, as well as the ability to apply them to exam-style problems. 

As the authors are themselves approaching this complex field, there will surely be some errors and inconsistencies in this text. any errors, typos, or suggestions for improvement are very welcome. Please feel free to add a pull request or reach out to us directly via email. 

These notes will therefore most likely evolve with time, and hopefully will be ever-changing until they converge to something readable. To quote a wise man and a mentor: **"do not print it! :-)"**

We wish you the best of luck in your studies!

---

**Michelangelo and Jacopo**
