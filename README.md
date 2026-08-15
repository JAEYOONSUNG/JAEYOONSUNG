<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
  <img src="./assets/header-light.svg" width="100%"
       alt="Jae-Yoon Sung — Ph.D., Research Professor, Dept. of Biotechnology, Yonsei University. Computational tools for domesticating non-model bacteria.">
</picture>

Most of biotechnology runs on a handful of domesticated organisms. I work on the
rest — thermophiles and other extremophiles that carry chemistry worth having but
arrive with annotation nobody has checked, no genetic parts, and no pipeline built
for them. Nearly everything below began as a step in that problem with no tool
attached to it, so I wrote one.

**Research Professor** · Dept. of Biotechnology, Yonsei University · Seoul, Korea<br>
**Working on** — synthetic and systems biology of non-model thermophiles, genome editors beyond Cas9, protein engineering through orthogonal replication<br>
**Mostly with** — *Geobacillus*, *Fervidobacterium*, and their thermophilic neighbours

<p>
  <a href="https://scholar.google.co.uk/citations?user=pSxoyuEAAAAJ"><img alt="Google Scholar" src="https://img.shields.io/badge/Google_Scholar-31414F?style=flat-square&logo=googlescholar&logoColor=white"></a>
  <a href="https://orcid.org/0000-0002-2475-8743"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-31414F?style=flat-square&logo=orcid&logoColor=white"></a>
  <a href="https://jaeyoonsung.github.io"><img alt="Curriculum Vitae" src="https://img.shields.io/badge/Curriculum_Vitae-31414F?style=flat-square&logo=readdotcv&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/jaeyoonsung"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-31414F?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="mailto:o3wodbs@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-31414F?style=flat-square&logo=gmail&logoColor=white"></a>
</p>

## Selected work

### Genome analysis & domestication

- **[DNMB](https://github.com/JAEYOONSUNG/DNMB)** — One GenBank in, a domestication-ready picture out: functional annotation in a readable table, codon usage, and ribosome-binding-site preference and spacing.
- **[DNMBsuite](https://github.com/JAEYOONSUNG/DNMBsuite)** — The same pipeline as a Docker image. You supply GenBank files; it fetches and caches the module databases itself.
- **[DNMBcluster](https://github.com/JAEYOONSUNG/DNMBcluster)** — Pan-genome clustering with the comparative figures already drawn.
- **[GenomeDrawer](https://github.com/JAEYOONSUNG/GenomeDrawer)** — Circos-style circular genome maps from an annotated genome.
- **[BPGAconverter](https://github.com/JAEYOONSUNG/BPGAconverter)** — Turns BPGA pan-genome output into tables you can actually analyse.

### Editors, mobile elements, and the primers to test them

- **[DNMBeditor](https://github.com/JAEYOONSUNG/DNMBeditor)** — Editor evidence and guide design from a single GenBank: CRISPR–Cas (Cas9/12/13 plus multi-subunit Type I, III and IV), TnpB, and IS110 bridge recombinases, in one namespace.
- **[TnpBfinder](https://github.com/JAEYOONSUNG/TnpBfinder)** — ωRNA discovery for TnpB in IS200/IS605-family transposons.
- **[BridgeRNAscan](https://github.com/JAEYOONSUNG/BridgeRNAscan)** — Bridge RNA discovery for IS110/IS1111 recombinases.
- **[MethREfinder](https://github.com/JAEYOONSUNG/MethREfinder)** — Methylation-sensitive restriction sites checked against REBASE — the barrier that quietly kills transformation.
- **[FINDER](https://github.com/JAEYOONSUNG/FINDER)** — Degenerate primers designed from conserved sequence, for pulling homologues out of a metagenome.
- **[mRNAcal](https://github.com/JAEYOONSUNG/mRNAcal)** — mRNA region extraction and RNA secondary structure through ViennaRNA.

### Software with a front door

- **[Gene Studio](https://github.com/JAEYOONSUNG/GeneStudio-releases)** — A plasmid workbench that runs from one HTML file: circular and linear maps, digests with a simulated gel, PCR, Gibson and Golden Gate, guide design, and `.ab1` review. Builds are public; the source is not.
- **[PostGrabbit](https://github.com/JAEYOONSUNG/PostGrabbit)** — A desktop app that finds academic job postings, scores them against your CV, and tracks the PIs behind them. Everything stays on your own machine.

## Built with

<p>
  <img alt="R" src="https://img.shields.io/badge/R-31414F?style=flat-square&logo=r&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-31414F?style=flat-square&logo=python&logoColor=white">
  <img alt="Bash" src="https://img.shields.io/badge/Bash-31414F?style=flat-square&logo=gnubash&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-31414F?style=flat-square&logo=docker&logoColor=white">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-31414F?style=flat-square&logo=typescript&logoColor=white">
  <img alt="Swift" src="https://img.shields.io/badge/Swift-31414F?style=flat-square&logo=swift&logoColor=white">
</p>

Leaning on BLAST+, HMMER, MMseqs2, MAFFT, IQ-TREE 2, Infernal, ViennaRNA,
InterProScan, eggNOG-mapper and ChimeraX — and on REBASE, MEROPS and dbCAN for
the reference data.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/rule-dark.svg">
  <img src="./assets/rule-light.svg" width="100%" alt="">
</picture>

<sub>Happy to talk about thermophile engineering, editor discovery, or anything that makes a non-model organism tractable — <a href="mailto:o3wodbs@gmail.com">o3wodbs@gmail.com</a> · <a href="https://open.kakao.com/o/sDSWN5Xg">KakaoTalk</a></sub>
