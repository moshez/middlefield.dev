# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Middlefield'
copyright = '2025, Middlefield Contributors'
author = 'Middlefield Contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

# MyST configuration
myst_enable_extensions = [
    'dollarmath',
    'colon_fence',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git', 'README.md']

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Furo theme options with gentle, warm colors
html_theme_options = {
    "light_css_variables": {
        # Soft sage green accent
        "color-brand-primary": "#5a8a6e",
        "color-brand-content": "#4a7a5e",
        # Warm, gentle background
        "color-background-primary": "#fdfcfa",
        "color-background-secondary": "#f5f3ef",
        "color-background-border": "#e8e4dd",
        # Soft text colors
        "color-foreground-primary": "#3d3d3d",
        "color-foreground-secondary": "#5a5a5a",
        "color-foreground-muted": "#7a7a7a",
        # Gentle sidebar
        "color-sidebar-background": "#f9f7f4",
        "color-sidebar-background-border": "#e8e4dd",
        # Softer admonitions
        "color-admonition-background": "#f5f3ef",
    },
    "dark_css_variables": {
        # Lighter sage for dark mode
        "color-brand-primary": "#7ab08e",
        "color-brand-content": "#8ac09e",
        # Warm dark backgrounds
        "color-background-primary": "#1a1a1a",
        "color-background-secondary": "#242420",
        "color-background-border": "#3a3a36",
        # Gentle light text
        "color-foreground-primary": "#e8e4dd",
        "color-foreground-secondary": "#c8c4bd",
        "color-foreground-muted": "#9a9690",
        # Dark sidebar
        "color-sidebar-background": "#1e1e1c",
        "color-sidebar-background-border": "#3a3a36",
    },
}
