---
layout: single
title: Research
permalink: /research/
excerpt: Research projects in cooperative multi-agent reinforcement learning and short-term residential load forecasting.
---

My research projects explore learning and coordination in multi-agent systems, and deep learning for energy forecasting.

{% assign research_entries = site.research | where: 'published', true | sort: 'order' %}
{% for entry in research_entries %}
<section class="content-entry">
  <h2><a href="{{ entry.url | relative_url }}">{{ entry.title | escape }}</a></h2>
  {% if entry.supervisors.size > 0 %}<p class="entry-meta">Supervised by {{ entry.supervisors | join: ' and ' | escape }}</p>{% endif %}
  <p>{{ entry.excerpt | escape }}</p>
  {% if entry.tags.size > 0 %}<p class="entry-technologies">{{ entry.tags | join: ' · ' | escape }}</p>{% endif %}
  <p><a href="{{ entry.url | relative_url }}">Read about this research project <span aria-hidden="true">→</span></a></p>
</section>
{% endfor %}

{% assign publications = site.publications | where: 'published', true | sort: 'order' %}
{% if publications.size > 0 %}
<h2>Publications</h2>
{% for publication in publications %}
<section class="content-entry">
  <h3><a href="{{ publication.url | relative_url }}">{{ publication.title | escape }}</a></h3>
  {% if publication.excerpt and publication.excerpt != '' %}<p>{{ publication.excerpt | strip_html | escape }}</p>{% endif %}
</section>
{% endfor %}
{% endif %}
