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
        
        Current interests include:
        - Unsupervised ML for (static/dynamic) (structural/functional) (human/porcine) brain (activity/connectivity).
        - Applying advanced and appropriate statistical (mixture) distributions, e.g., directional statistics.
        - Low-rank models of high-resolution brain connectivity networks.
        - Multimodal modeling, e.g., joint modeling of fMRI, EEG, and PET data.
        - Shift- and stretch-invariant unsupervised modeling. 
        - Preprocessing and denoising of fMRI and EEG data.
        - Reducing the need for heuristics in neurocomputational modeling. 

        Specific ML methods I have experience with:
        - K-means/mixture modeling/Hidden Markov models for uni/multi/matrix-variate clustering
        - Matrix and tensor factorizations e.g., (sparse) PCA, ICA, Archetypal analysis, Tucker, CP
        - Riemannian statistical distributions: Watson, Angular central Gaussian, Wishart etc.
        - Geometry-aware statistical modeling on the (complex) (hyper-) sphere, Grassmann, torus, SPD manifold
        - Graph analyses and graph signal processing
        - Multi-subject and multi-modal data fusion (e.g., simultaneous modeling of fMRI, EEG, and MEG data)
        - Statistical methods: Mixed effects models, survival analysis
        - Unnormalized mixture models
        - Stochastic block models
        - Low-rank model reparametrization
        - Shift- and stretch-invariant non-negative matrix factorization / sparse coding
        - Phase coherence analysis, including the Hilbert transform
        - Empirical/Variational mode decompositions
        - Procrustes analysis
        - Generalized eigendecompositions
        - Spectral analysis, e.g., multitaper spectral estimation
    design:
      columns: '1'
  - block: markdown
    id: student_projects
    content:
      title: 'Potential student projects'
      subtitle: ''
      text: |-
        - Pulse detection in fast fMRI during sleep data using, e.g., ICA or sparse coding with a potential temporal shift invariance. **Significance**: To show the existence of norepinephrine spikes in the sleeping brain, signifying a potential important working mechanism of the *glymphatic system*, which is thought to cleanse the brain during sleep by propagating cerebrospinal fluid through the brain parenchyma. **Suggested prerequisites**: Coding experience in python/pytorch, interest in unsupervised machine learning and the brain. 
        - Interregional brain phase coherence alterations as a function of psychedelic drugs. Two datasets: One on the acute effects of psilocybin (n=28) and one on the long-term effects of psilocybin (n~80 ish) (possible to include even more datasets). We have previously shown that a certain network of frontoparietal and default mode regions appear to be reduced in activity acutely following psilocybin. We now have improved methods and access to further datasets, allowing us to conduct a confirmatory study on the previously shown effects. **Significance**: The subjective effect of psychedelics are clear but previous analyses on fMRI data have shown differing results between analysis method and research groups. With the phase coherence analysis, we believe to be able to show consistent effects across datasets. **Suggested prerequisites**: Interest in psychedelic drugs and the brain, some coding experience (less method development, more analysis and data handling).
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
  - block: cta-card
    demo: true # Only display this section in the HugoBlox Kit demo site
    content:
      title: 👉 Build your own academic website like this
      text: |-
        This site is generated by HugoBlox Kit - the FREE, Hugo-based open source website builder trusted by 250,000+ academics like you.

        <a class="github-button" href="https://github.com/HugoBlox/kit" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star HugoBlox/kit on GitHub">Star</a>

        Easily build anything with blocks - no-code required!

        From landing pages, second brains, and courses to academic resumés, conferences, and tech blogs.
      button:
        text: Get Started
        url: https://hugoblox.com/templates/
    design:
      card:
        # Card background color (CSS class)
        css_class: 'bg-primary-300 dark:bg-primary-700'
        css_style: ''
---
