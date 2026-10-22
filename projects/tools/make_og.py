"""Link-preview (Open Graph) image for a project page: 1200 x 630 px.

    python projects/tools/make_og.py <out.png> "<venue>" "<short name>" "<title>" "<authors>" <figure.png>
"""
import sys
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

out, venue, short, title, authors, figure = sys.argv[1:7]
fig = plt.figure(figsize=(12, 6.3), dpi=100)
fig.patch.set_facecolor("#fbfbf9")
ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off"); ax.set_xlim(0, 1200); ax.set_ylim(0, 630)
ax.add_patch(plt.Rectangle((0, 0), 1200, 10, color="#2a6fd1"))
ax.text(60, 560, venue.upper(), fontsize=17, color="#1d5bb3", family="monospace", weight="bold")
ax.text(60, 490, short, fontsize=46, color="#111418", family="serif", weight="bold")
ax.text(60, 445, "\n".join(textwrap.wrap(title, 34)), fontsize=19, color="#111418", family="serif", va="top", linespacing=1.35)
ax.text(60, 95, "\n".join(textwrap.wrap(authors, 64)), fontsize=14, color="#454b54", va="bottom", linespacing=1.4)
ax.text(60, 45, "mahyar333.github.io/projects", fontsize=13, color="#6b717a", family="monospace")
img = mpimg.imread(figure)
fx = fig.add_axes([0.53, 0.12, 0.44, 0.78]); fx.imshow(img); fx.axis("off")
fig.savefig(out, dpi=100, facecolor=fig.get_facecolor())
print("saved", out)
