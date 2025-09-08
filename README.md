# De Novo Nanobody Design Workshop

This repository contains the computational workflow for the *de novo* redesign of a nanobody to target a specific protein of interest.

This material is used for the **Nanobody Workshop (22-26 Sep 2025)**.
*   **Event Link:** [https://indico.ijs.si/event/2966/](https://indico.ijs.si/event/2966/)

## Overview

The workshop starts from the 3D structure of an input PDB target and a scaffold nanobody. Most of the steps are performed using Google Colab notebooks, which are provided in this repository.

## Target and Scaffold Files

*   **Target:** You can use an arbitrary protein structure (in PDB format) of your choice.
    *   **Example Target:** The catalytic domain of CDKL5, provided as `[PATH/TO/CDKL5_target.pdb]`.
*   **Scaffold:** A pre-selected nanobody structure is provided to serve as the starting point for the design.
    *   **Scaffold File:** `[PATH/TO/nanobody_scaffold.pdb]`

## Design Pipeline

The following pipeline will be used to design and evaluate new nanobody variants.

### 1. Epitope Prediction

*   **Tool:** [SEPPA 3.0](http://www.badd-cao.net/seppa3/) (Web Server)
*   **Purpose:** To predict potential epitopes on the surface of the target protein. These regions are likely to be involved in protein-protein interactions and are therefore good candidates for targeting.
*   **Instructions:** Upload your target PDB file (`[PATH/TO/CDKL5_target.pdb]` or your own) and provide the chain ID letter (i.e., A) of your target to the SEPPA 3.0 web server to get the predictions.

### 2. Nanobody CDRs Design

*   **Tool:** RFAntibody
*   **Colab Notebook:** [`[1_RFAntibody_Design.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_1])
*   **Purpose:** To design alternative nanobody structures by modifying the Complementarity-Determining Regions (CDRs). The CDRs are the most variable parts of the nanobody and are primarily responsible for binding to the target.

### 3. Side-Chain Reconstruction

*   **Tool:** PIPPack
*   **Colab Notebook:** [`[2_PIPPack_Sidechain.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_2])
*   **Purpose:** To reconstruct the side-chain atoms of the newly designed nanobody structures. This step is necessary to create a complete and realistic 3D model.

### 4. Interface Sequence Reconstruction

*   **Tool:** AntiFold
*   **Colab Notebook:** [`[3_AntiFold_Sequence.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_3])
*   **Purpose:** To reconstruct the amino acid sequence at the target-nanobody interface. Using the side-chain reconstructed model as input, AntiFold predicts a sequence compatible with the designed structure and the target interface.

### 5. Complex Reprediction and Quality Assessment

*   **Tool:** gapTrick
*   **Colab Notebook:** [`[4_gapTrick_Analysis.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_4])
*   **Purpose:** To re-predict the protein-protein complex using the designed nanobody model as input. This step assesses the quality of the designed interfacial residues and identifies key interactions (e.g., hydrogen bonds, salt bridges).

## Screening and Further Validation

The computational design and screening process may require evaluating hundreds of nanobody designs. The best candidates, selected based on gapTrick metrics, should undergo further validation using more rigorous methods. These can include:

*   **Physics-based approaches:**
    *   Protein-protein docking scores (e.g., HADDOCK, ROSETTA-DDG).
    *   Geometric scores (e.g., ROSETTA SUITE).
*   **Stability Assessment:**
    *   Molecular Dynamics (MD) simulations (> 100 ns) to assess complex stability (e.g., using GROMACS, AMBER).
    *   Enhanced sampling methods to explore the conformational landscape (e.g., using the Prody package).

This multi-step validation process is crucial for increasing the likelihood of success in experimental settings.
