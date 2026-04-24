---
title: Shift- and Stretch-Invariant Non-Negative Matrix Factorization with an Application
  to Brain Tissue Delineation in Emission Tomography Data
authors:
- Anders S. Olsen
- Miriam L. Navarro
- Claus Svarer
- Jesper L. Hinrich
- Morten Mørup
- Gitte M. Knudsen
date: '2026-04-01'
publishDate: '2026-04-24T12:22:38.720609Z'
publication_types:
- manuscript
publication: '*arXiv*'
doi: 10.48550/arXiv.2604.08161
abstract: Dynamic neuroimaging data, such as emission tomography measurements of radiotracer
  transport in blood or cerebrospinal fluid, often exhibit diffusion-like properties.
  These introduce distance-dependent temporal delays, scale-differences, and stretching
  effects that limit the effectiveness of conventional linear modeling and decomposition
  methods. To address this, we present the shift- and stretch-invariant non-negative
  matrix factorization framework. Our approach estimates both integer and non-integer
  temporal shifts as well as temporal stretching, all implemented in the frequency
  domain, where shifts correspond to phase modifications, and where stretching is
  handled via zero-padding or truncation. The model is implemented in PyTorch (https://github.com/anders-s-olsen/shiftstretchNMF).
  We demonstrate on synthetic data and brain emission tomography data that the model
  is able to account for stretching to provide more detailed characterization of brain
  tissue structure.
tags:
- Computer Science - Machine Learning
links:
- name: arXiv
  url: https://arxiv.org/abs/2604.08161
---
