# *De Novo* Nanobody Design Workshop

This repository contains the computational workflow for the *de novo* (re)design of a nanobody to specific target protein of interest.
The pipeline is developed to use Google Colab resources and adequate for people with little knowledge on protein *de novo* design tools and limited structural biology background.
It is actually made for demonstraction and teaching, and not adequate to scale for a production-level *in silico* screening 

This material has been used for the **Nanobody Workshop (22-26 Sep 2025)**.
*   **Event Link:** [https://indico.ijs.si/event/2966/](https://indico.ijs.si/event/2966/)

## Overview

The workshop starts from the 3D structure of two input PDBs, one of the target and one of the scaffold nanobody. Most of the steps are performed using Google Colab notebooks, provided in this repository.

## Target and Scaffold Files

*   **Target:** You can use an arbitrary protein structure (in PDB format) of your choice.
    *   **Example Target:** The catalytic domain of CDKL5, provided in `[./Example_input/Target.pdb]`.
*   **Scaffold:** A pre-selected nanobody structure is provided to serve as the starting point for the design.
    *   **Scaffold File:** `[./Example_input/nanobody_scaffold.pdb]`

## Design Pipeline

### 1. Candidate epitopes Prediction and nanobody CDRs identification

*   **Tools:** [Quilt](https://github.com/plijnzaad/quilt) and [Nanocdr-x](https://github.com/lescailab/nanocdr-x)
*   **Purpose:** This analysis serves two main purposes:
    *   To predict potential epitopes on the surface of the target protein. These regions must have a sufficient area to be involved in protein-protein interactions and with hydrophobic propensity, as these features are ideal for *de novo* targeting.
    *   To identify and extract the complementary-determining regions (CDRs) from nanobody sequences.
*   **Instructions:** Run [![1_Preparation_colab.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/margio91/De-novo-nanobody-re-design/blob/main/1_Preparation_colab.ipynb) to start with 1_Preparation_colab.ipynb. You need the **Target** and **Scaffold** PDB files 

### 2. Nanobody CDRs Design

*   **Tool:** RFAntibody
*   **Colab Notebook:** [`[1_RFAntibody_Design.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_1])
*   **Purpose:** To design alternative nanobody structures by modifying the Complementarity-Determining Regions (CDRs). The CDRs are the most variable parts of the nanobody and are primarily responsible for binding to the target.

### 3. Side-Chain Reconstruction

*   **Tool:** PIPPack
*   **Colab Notebook:** [`[2_PIPPack_Sidechain.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_2])
*   **Purpose:** To reconstruct the side-chain atoms of the newly designed nanobody structures. This step is necessary to create a complete and realistic 3D model.

### 4. CDRs Sequence Reconstruction

*   **Tool:** AntiFold
*   **Colab Notebook:** [`[3_AntiFold.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_3])
*   **Purpose:** To reconstruct the amino acid sequence at the target-nanobody interface. Using the side-chain reconstructed model as input, AntiFold predicts a sequence compatible with the designed structure and the target interface.

### 5. Complex Reprediction for Quality Assessment

*   **Tool:** gapTrick
*   **Colab Notebook:** [`[4_gapTrick.ipynb]`]([LINK_TO_YOUR_COLAB_NOTEBOOK_4])
*   **Purpose:** To re-predict the protein-protein complex using the designed nanobody model as input. This step assesses the quality of the designed interfacial residues and identifies key interactions (e.g., hydrogen bonds, salt bridges).

## Screening and Further Validation


Further steps of validation are crucial for increasing the likelihood of success in experimental settings, both *in vitro* and *in vivo*.
In order to have a sufficient n° of designs for a successful experimental screening, it is advisable to generate **>1000** in silico designs and pass further validation and filtering steps.
These steps may use one or more of the following:

*   **Interaction confidence from deep learning approaches**
    *   AlphaFold-Multimer Local Interaction Score (AFM-LIS) (https://github.com/flyark/AFM-LIS)
*   **Empirical-physics scores:**
    *   Protein-protein docking scores (e.g., HADDOCK, Rosetta-ddG, Fold-X)
    *   Geometric scores on surface and non-covalent interactions at interface (e.g., Rosetta interface analysis tools, dG_separated/dSASAx100, packstat or unsaturated H-bonds)
*   **Physics-based Assessment:**
    *   Molecular Dynamics (MD) simulations (> 100 ns) to assess complex stability (e.g., RMSD metric using GROMACS or AMBER MD engines)
    *   Enhanced sampling methods to explore the conformational free-energy landscape (e.g., metadynamics with PLUMED or coarse-grained/all-atom hybrid simulations with Prody)
*   **Developability Assessment (Delta to Nb scaffold):**
    *   Solubility prediction
    *   Stability Prediction 
    *   Aggregation propensity
    *   Off-target antigenic effects
