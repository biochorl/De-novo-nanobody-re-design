<img src="Images/Background.png" alt="background" width="100%"/>
[Background image source](https://www.independent.co.uk/travel/europe/slovenia/nova-gorica-slovenia-italy-capital-of-culture-b2712344.html)

# *De Novo* Nanobody Design Workshop

This repository contains the computational workflow for the *de novo* (re)design of a nanobody to specific target protein of interest.
The pipeline is developed to use Google Colab resources and it is adequate for people with little knowledge on protein *de novo* design tools and limited structural biology background.
It is actually made for demonstration and teaching, while being not adequate to scale for a production-level *in silico* screening 

This material has been used during the **Nanobody Workshop (22-26 Sep 2025)**.
*   **Event Link:** [https://indico.ijs.si/event/2966/](https://indico.ijs.si/event/2966/)

## Overview

The workshop starts from the 3D structure of two input PDBs, one of the target and one of the scaffold nanobody. Most of the steps are performed using Google Colab notebooks, provided in this repository.

## Target and Scaffold Files

*   **Target:** An arbitrary protein structure (in PDB format) of your choice.
    *   **Example Target File:** [7z1b.pdb](./Example_input/7z1b.pdb)
*   **Scaffold:** A pre-selected nanobody structure to serve as the starting point for the (re)design.
    *   **Example nanobody scaffold File:** [nanobody_scaffold.pdb](./Example_input/nanobody_scaffold.pdb)
---

## Design Pipeline

### 1. Candidate epitopes Prediction and nanobody CDRs identification

<table>
  <tr>
    <td align="center">
      <img src="Images/Image_target_patches_detection.png" alt="Fetching target antigen patches" width="400"/>
      <br>
      <em>Fetching target antigen patches</em>
    </td>
    <td align="center">
      <img src="Images/Image_CDRs_detection.png" alt="Fetching nanobody complementary determining regions (CDRs)" width="400"/>
      <br>
      <em>Fetching nanobody complementary determining regions (CDRs)</em>
    </td>
  </tr>
</table>

*   **Tools:** [Quilt](https://github.com/plijnzaad/quilt) and [Nanocdr-x](https://github.com/lescailab/nanocdr-x)
*   **Purpose:** This analysis serves two main purposes:
    *   To predict potential epitopes on the surface of the target protein. These regions must have a sufficient area to be involved in protein-protein interactions and with hydrophobic propensity, as these features are ideal for *de novo* targeting.
    *   To identify and extract the complementary-determining regions (CDRs) from nanobody sequences.
*   **Colab Notebook:** [![1_Preparation_colab.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/margio91/De-novo-nanobody-re-design/blob/main/1_Preparation_colab.ipynb)

### 2. *Nanobody de novo* CDRs Design

*   **Tool:** RFantibody [paper link](https://www.biorxiv.org/content/10.1101/2024.03.14.585103v2)
*   **Purpose:** To design alternative complete CDR conformations. The CDRs are the most variable parts of the nanobody and are primarily responsible for binding to the target. The output is the backbone structure of the complex between the (re)designed nanobody interacting with the target protein antigen at a specific point (selected epitope patch from step 1). You have the possibility also to annotate nanobody residues potentially involved in contacts with the epitope.
*   **Colab Notebook:** [![1_Preparation_colab.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/margio91/De-novo-nanobody-re-design/blob/main/2_RFDiffusionAntibody_colab.ipynb)

### 3. Sequence Reconstruction of nanobody interfacial residues

*   **Tool:** ProteinMPNN [paper link](https://www.science.org/doi/10.1126/science.add2187)
*   **Purpose:** To reconstruct the sequence of CDRs and FWs regions at the nanobody-target interface. This step is necessary to rebuild a 3D model, as RFantibody masks interfacial residues as glycines (it is focused on backbone reconstruction, it did not generate full atoms models!).
*   **Colab Notebook:** [![1_Preparation_colab.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/margio91/De-novo-nanobody-re-design/blob/main/3_ProteinMPNN_colab.ipynb)

### 4. Complex prediction of ProteinMPNN optimized sequence

*   **Tool:** SwissModel (webserver) [paper link](https://academic.oup.com/nar/article/46/W1/W296/5000024)
*   **Purpose:** A 3D model of the designed nanobody needs to be created, replacing the original nanobody sequence with the top scoring ProteinMPNN design. THis step can be accomplished with any structure predictor that can leverage 3D template information stored in the PDB file of the RFantibody design (downloaded at step 2); SwissModel is used through a webserver, as free Colab GPU resources do not fit with the time required for this task, especially if the target has more than 300 AA.
*   **Instructions:** access SwissModel website for template-based structure prediction at this [link](https://swissmodel.expasy.org/interactive#structure). Please copy-paste the nanobody sequence of the best ProteinMPNN design, than toggle "Add Hetero target" and add the sequence of the target protein. After that, please toggle "Add template FIle..." and upload the PDB structure given as input to the previous step 3. The final generated model will be used as input in the next step 5.


### 5. CDRs Sequence Reconstruction

*   **Tool:** AntiFold [paper link](https://academic.oup.com/bioinformaticsadvances/article/5/1/vbae202/8090019)
*   **Purpose:** To reconstruct the sequence of CDRs regions with a CDR-specialized model. This step is necessary to get the final nanobody design sequence to build a final 3D model with optimized CDRs.
*   **Colab Notebook:** [![1_Preparation_colab.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/margio91/De-novo-nanobody-re-design/blob/main/5_Antifold_colab.ipynb)

### 6. Complex Reprediction for Quality Assessment

*   **Tool:** gapTrick [paper link](https://www.biorxiv.org/content/10.1101/2025.01.31.635911v2)
*   **Purpose:** To use the top scoring AntiFold nanobody sequence for getting the full-atom 3D model of the *de novo* designed nanobody-target complex. This step assesses the quality of the designed interfacial residues and identifies key non-covalent contacts (e.g., hydrophobic contacts, hydrogen bonds, salt bridges).
*   **Colab Notebook:** [![1_Preparation_colab.ipynb](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/margio91/De-novo-nanobody-re-design/blob/main/6_gapTrick_colab.ipynb)

---
## Screening and Further Validation of *de novo* designed nanobody binders

Further steps of validation are crucial for increasing the likelihood of success in experimental settings, both *in vitro* and *in vivo*.
In order to have a sufficient n° of designs for a successful experimental screening, it is advisable to generate at least **≈1000** *in silico* designs (full-atom structure) and use them as input to pass further validation and filtering steps.
These steps may use one or more of the following (the list is not comprehensive, just for giving some examples):

*   **Interaction confidence from deep learning approaches**
    *   AlphaFold-Multimer Local Interaction Score (AFM-LIS) (https://github.com/flyark/AFM-LIS)
*   **Empirical-physics scores:**
    *   Protein-protein docking scores (e.g., HADDOCK, Rosetta-ddG, Fold-X)
    *   Geometric scores on surface and non-covalent interactions at interface (e.g., Rosetta interface analysis tools, dG/dSASA, packstat or n° unsaturated H-bonds)
*   **Physics-based Assessment:**
    *   Molecular Dynamics simulations (> 100 ns) to assess complex stability (e.g., RMSD metric using GROMACS, AMBER, etc...)
    *   Enhanced sampling methods, to generate the conformational free-energy landscape (e.g., metadynamics with PLUMED or coarse-grained/all-atom hybrid simulations with Prody)
*   **Developability Assessment (To be compared with the initial Nb scaffold if it is known it has a good developability):**
    *   Solubility prediction
    *   Stability Prediction 
    *   Aggregation propensity
    *   Propension for off-target antigenic interactions

---
## Acknowledgements

Most of the Google colaboratories were developed by customizing other colabs, referenced in the corresponding file. I linked the paper or the original source describing all the different methods. This repo was written with help of [Google Gemini-CLI](https://github.com/google-gemini/gemini-cli).

## Contact

For any questions, suggestions, or issues, please open an issue in this GitHub repository or contact me at [marco.orlando1991@live.it](mailto:marco.orlando1991@live.it) or [marco.orlando1991@ung.si](mailto:marco.orlando1991@ung.si).
