---
title: Coupled Generator Decomposition for Fusion of Electro- and Magnetoencephalography
  Data
authors:
- Anders S. Olsen
- Jesper D. Nielsen
- Morten Mørup
date: '2024-08-01'
publishDate: '2026-04-24T14:21:33.096780Z'
publication_types:
- paper-conference
publication: '*2024 32nd European Signal Processing Conference (EUSIPCO)*'
doi: 10.23919/EUSIPCO63174.2024.10715032
abstract: Data fusion modeling can identify common features across diverse data sources
  while accounting for source-specific variability. Here we introduce the concept
  of a coupled generator decomposition and demonstrate how it generalizes sparse principal
  component analysis (SPCA) for data fusion. Leveraging data from a multisubject,
  multimodal (electro- and magnetoencephalography (EEG and MEG)) neuroimaging experiment,
  we demonstrate the efficacy of the framework in identifying common features in response
  to face perception stimuli, while accommodating modality- and subject-specific variability.
  Through split-half cross-validation of EEG/MEG trials, we investigate the optimal
  model order and regularization strengths for models of varying complexity, comparing
  these to a group-level model assuming shared brain responses to stimuli. Our findings
  reveal altered 170ms fusiform face area activation for scrambled faces, as opposed
  to real faces, particularly evident in the multimodal, multisubject model. Model
  parameters were inferred using stochastic optimization in PyTorch, demonstrating
  comparable performance to conventional quadratic programming inference for SPCA
  but with considerably faster execution. We provide an easily accessible toolbox
  for coupled generator decomposition that includes data fusion for SPCA, archetypal
  analysis and directional archetypal analysis. Overall, our approach offers a promising
  new avenue for data fusion.
tags:
- Brain modeling
- Data fusion
- Data integration
- Electroencephalography
- Faces
- Generators
- Magnetoencephalography
- Optimization
- Principal component analysis
- Quadratic programming
- Soft sensors
- Sparse matrices
- Sparse principal component analysis
- Spatiotemporal variability
- Stochastic processes
---
