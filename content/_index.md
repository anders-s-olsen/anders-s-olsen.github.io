---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: large # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: rounded # Options: circle (default), square, rounded
  - block: markdown
    id: experience
    content:
      title: 'Current and past interests'
      subtitle: ''
      text: |-
        
        My methodological experience includes:

        - Unsupervised and probabilistic modeling: K-means, mixture models, Hidden Markov models, and stochastic block models for univariate, multivariate, and matrix-variate data.
        - Matrix, tensor, and low-rank modeling: PCA and sparse PCA, ICA, NMF, sparse coding, archetypal analysis, coupled generator (i.e., multisubject or multimodality) decompositions, Tucker and CP decompositions, generalized eigendecompositions, low-rank reparameterization.
        - Directional and manifold-valued statistics on spaces including the real and complex (projective) hyperspheres, Grassmann manifold, torus, SPD/SPSD manifolds. Estimation methods: score matching, noise-contrastive estimation. 
        - Time-series and time–frequency analysis: Phase-coherence analysis, multitaper spectral and cross-spectral estimation, empirical and variational mode decomposition, time-shift- and time-stretch-invariant modeling.
        - Graph and spatial analysis: Graph analysis, graph signal processing, structural-connectome and cortical-geometric eigenmodes, Procrustes alignment.
        - Multisubject and multimodal data fusion: Joint modeling across subjects and functional neuroimaging modalities, particularly fMRI and combined EEG/MEG data.
        - Entropy and complexity measures: LZ complexity, sample entropy, spectral entropy, and many more. 
        - Tracer kinetics: compartment modelling of dynamic SPECT data. 
        - Statistical inference: Linear mixed effects models with max-T permutation-based FWER control, survival analysis. 
        - Neuroimaging analysis software: fMRIPrep, ASLPrep, MRIQC, TEDANA, SPM, FSL, MNE-Python, EEGLAB, and Connectome Workbench.
        - Programming in Python/PyTorch (primary language since 2021), Matlab (since 2015), R (only minor experience)


    design:
      columns: '1'
  - block: markdown
    id: student_projects
    content:
      title: 'Potential student projects'
      subtitle: ''
      text: |-
        - *General*: I continuously supervise MSc theses on computational modeling of functional brain imaging. While the methods are most interesting for me, the projects always have an application to, e.g., consciousness (sleep, psychedelics, anesthesia) or glymphatic physiology. Ongoing student projects include the physics behind "brain spirals", toroidal models of dynamic functional connectivity, and modeling temporal smoothness in brain phase coherence states. If you are an MSc student looking for a project, feel free to reach out. 
        - Pulse detection in fast fMRI during sleep data using, e.g., ICA or sparse coding with temporal shift invariance and possibly stretch invariance. **Significance**: To show the existence of norepinephrine spikes and other physiological movers in the sleeping brain, signifying a potential important working mechanism of the *glymphatic system*, which is thought to cleanse the brain during sleep by propagating cerebrospinal fluid through the brain parenchyma. **Suggested prerequisites**: Coding experience in python/pytorch, interest in unsupervised machine learning and the brain. 
        - Requirements for the Hilbert transform in fMRI data. The Hilbert transform is used to assess phase coherence between regional brain signals, but generally requires data to be "monocomponent", i.e., contains only one "type" of oscillation. Real data, both M/EEG and fMRI do not generally uphold this but nevertheless the Hilbert transform is still used to assess phase coherence. In this project we want to figure out the implications of this, i.e., 1. how much signal do we capture with existing methods and 2. what can we do to capture more (artefact removal, filtering etc). **Significance**: This study will enable a more correct characterization of brain networks by reducing the heuristics needed to model such. **Suggested prerequisites**: An interest in math and/or signal processing and coding in matlab or python. The project will mainly be theoretical / use synthetic data but application to brain networks is a possibility. 

    design:
      columns: '1'
  - block: collection
    id: publications
    content:
      title: Publications
      text: ''
      count: 0
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - events
  #   design:
  #     view: card
  #- block: collection
  #  id: news
  #  content:
  #    title: Recent News
  #    subtitle: ''
  #    text: ''
  #    # Page type to display. E.g. post, talk, publication...
  #    page_type: blog
  #    # Choose how many pages you would like to display (0 = all pages)
  #    count: 10
  #    # Filter on criteria
  #    filters:
  #      author: ''
  #      category: ''
  #      tag: ''
  #      exclude_featured: false
  #      exclude_future: false
  #      exclude_past: false
  #      publication_type: ''
  #    # Choose how many pages you would like to offset by
  #    offset: 0
  #    # Page order: descending (desc) or ascending (asc) date.
  #    order: desc
  #  design:
  #    # Choose a layout view
  #    view: card
  #    # Reduce spacing
  #    spacing:
  #      padding: [0, 0, 0, 0]
  # - block: cta-card
  #   demo: true # Only display this section in the HugoBlox Kit demo site
  #   content:
  #     title: 👉 Build your own academic website like this
  #     text: |-
  #       This site is generated by HugoBlox Kit - the FREE, Hugo-based open source website builder trusted by 250,000+ academics like you.

  #       <a class="github-button" href="https://github.com/HugoBlox/kit" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star HugoBlox/kit on GitHub">Star</a>

  #       Easily build anything with blocks - no-code required!

  #       From landing pages, second brains, and courses to academic resumés, conferences, and tech blogs.
  #     button:
  #       text: Get Started
  #       url: https://hugoblox.com/templates/
  #   design:
  #     card:
  #       # Card background color (CSS class)
  #       css_class: 'bg-primary-300 dark:bg-primary-700'
  #       css_style: ''
---
