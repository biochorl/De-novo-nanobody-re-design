# De-novo-nanobody-re-design
This repo contains the worflow for the computational *de novo* (re)design of a nanobody to target a specific protein of interestused in the Nanobody Workshop (22-26 Sep 2025), https://indico.ijs.si/event/2966/
      The workshop starts from the 3D structure of an input PDB target and a scaffold nanobody.
    4 
    5 Most of the steps are performed using Google Colab notebooks, which you can find in this repository.
    6 
    7 ## Target and Scaffold Files
    8 
    9 *   **Target:** You can use an arbitrary protein structure (in PDB format) of your choice.
   10     *   **Example Target:** The catalytic domain of CDKL5, provided as `[PATH/TO/CDKL5_target.pdb]`.
   11 *   **Scaffold:** A pre-selected nanobody structure is provided to serve as the starting point for the design.
   12     *   **Scaffold File:** `[PATH/TO/nanobody_scaffold.pdb]`
   13 
   14 ## Design Pipeline
   15 
   16 The following pipeline will be used to design and evaluate new nanobody variants.
   17 
   18 ### 1. Epitope Prediction
   19 
   20 *   **Tool:** [SEPPA 3.0](http://www.badd-cao.net/seppa3/) (Web Server)
   21 *   **Purpose:** To predict potential epitopes on the surface of the target protein. These predicted regions are likely to be involved
      in protein-protein interactions and are therefore good candidates for targeting with a nanobody.
   22 *   **Instructions:** Upload your target PDB file (`[PATH/TO/CDKL5_target.pdb]` or your own) to the SEPPA 3.0 web server to get the
      predictions.
   23 
   24 ### 2. Nanobody CDRs Design
   25 
   26 *   **Tool:** RFAntibody
   27 *   **Colab Notebook:** [`[1_RFAntibody_Design.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_1])
   28 *   **Purpose:** To design alternative nanobody structures by modifying the Complementarity-Determining Regions (CDRs). The CDRs are
      the most variable parts of the nanobody and are primarily responsible for binding to the target.
   29 
   30 ### 3. Side-Chain Reconstruction
   31 
   32 *   **Tool:** PIPPack
   33 *   **Colab Notebook:** [`[2_PIPPack_Sidechain.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_2])
   34 *   **Purpose:** To reconstruct the side-chain atoms of the newly designed nanobody structures. This step is necessary to create a
      complete and realistic 3D model of the nanobody.
   35 
   36 ### 4. Interface Sequence Reconstruction
   37 
   38 *   **Tool:** AntiFold
   39 *   **Colab Notebook:** [`[3_AntiFold_Sequence.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_3])
   40 *   **Purpose:** To reconstruct the amino acid sequence at the target-nanobody interface. Using the side-chain reconstructed model as
      input, AntiFold will predict a sequence that is compatible with the designed structure and the target interface.
   41 
   42 ### 5. Complex Reprediction and Quality Assessment
   43 
   44 *   **Tool:** gapTrick
   45 *   **Colab Notebook:** [`[4_gapTrick_Analysis.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_4])
   46 *   **Purpose:** To repredict the protein-protein complex using the designed nanobody model as input. This step allows for the
      assessment of the quality of the designed interfacial residues, the identification of key interactions (e.g., hydrogen bonds, salt
      bridges), and the characterization of the binding interface.
   47 
   48 ## Screening and Further Validation
   49 
   50 The computational design and screening process may require the generation and evaluation of hundreds of nanobody designs. The best
      candidates, selected based on the gapTrick metrics, should undergo further validation using more rigorous and computationally
      expensive methods. These can include:
   51 
   52 *   **Physics-based approaches:**
   53     *   Protein-protein docking scores (e.g., HADDOCK, ROSETTA-DDG).
   54     *   Geometric scores (e.g., ROSETTA SUITE).
   55 *   **Stability Assessment:**
   56     *   Molecular Dynamics (MD) simulations (> 100 ns) to assess the stability of the complex (e.g., using GROMACS, AMBER).
   57     *   Enhanced sampling methods to explore the conformational landscape of the complex (e.g., using the Prody package).
   58 
   59 This multi-step validation process is crucial for increasing the likelihood of success in experimental settings.
