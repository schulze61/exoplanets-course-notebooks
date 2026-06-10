"""
nb_toc.py Jupyter notebook TOC utilities.

Usage
-----
from nb_toc import toc, back_to_toc

# In your TOC cell (code cell):
toc([
    "Introduction",
    "Data and Methods",
    "Results",
    "Discussion",
    "Conclusion",
])

# At the bottom of each section (code cell):
back_to_toc()
"""

from IPython.display import HTML


def _heading_id(text: str) -> str:
    """Match JupyterLab's createHeaderId: spaces -> hyphens, everything else literal."""
    return text.replace(" ", "-")


def toc(
    sections: list[str],
    title: str = "Table of Contents",
    toc_heading: str = "Table of Contents",
) -> HTML:
    """
    Render a clickable Table of Contents.

    Parameters
    ----------
    sections : list of str
        Heading text for each section, exactly as written in the ## cells.
    title : str
        Display title shown above the TOC list.
    toc_heading : str
        The heading text of the TOC cell itself (used by back_to_toc to scroll
        back up). Defaults to "Table of Contents".

    Returns
    -------
    IPython.display.HTML
        Display by calling toc(...) as the last expression in a code cell.

    Notes
    -----
    Each section must be a plain markdown heading cell, e.g.:
        ## Introduction
    The heading text must match the corresponding entry in `sections` exactly.
    JupyterLab derives the element id as: spaces -> hyphens, case preserved.
    """
    items_html = "\n".join(
        f'<li>'
        f'<button class="jptoc-btn" data-target="{_heading_id(s)}" '
        f'style="background:none;border:none;padding:0;color:#0066cc;'
        f'cursor:pointer;font-size:1em;text-align:left;">'
        f'{s}'
        f'</button></li>'
        for s in sections
    )

    html = f"""\
<div style="background:#f8f8f8;border:1px solid #ddd;border-radius:6px;
            padding:14px 18px;display:inline-block;min-width:220px">
  <div style="font-weight:bold;font-size:1.05em;margin-bottom:8px">{title}</div>
  <ol style="margin:0;padding-left:18px;line-height:1.9">
{items_html}
  </ol>
</div>
<script>
(function() {{
  document.querySelectorAll('.jptoc-btn').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var el = document.getElementById(this.getAttribute('data-target'));
      el.scrollIntoView({{behavior: 'instant'}}); 
    }});
  }});
}})();
</script>"""

    return HTML(html)


def back_to_toc(toc_heading: str = "Table of Contents") -> HTML:
    """
    Render a 'Back to TOC' button that scrolls up to the TOC heading.

    Parameters
    ----------
    toc_heading : str
        The heading text of the TOC cell. Must match the ## heading exactly.
        Defaults to "Table of Contents".

    Returns
    -------
    IPython.display.HTML
        Display by calling back_to_toc() as the last expression in a code cell.
    """
    target = _heading_id(toc_heading)
    print(target)

    html = f"""\
<button class="jptoc-back" data-target="{target}"
  style="background:none;border:none;padding:0;color:#555;
         cursor:pointer;font-size:0.9em;">&#8593; Back to TOC</button>
<script>
(function() {{
  document.querySelectorAll('.jptoc-back').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var el = document.getElementById(this.getAttribute('data-target'));
      if (el) {{ el.scrollIntoView({{behavior: 'smooth'}}); }}
    }});
  }});
}})();
</script>"""

    return HTML(html)
