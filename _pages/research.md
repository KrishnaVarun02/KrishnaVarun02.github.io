---
layout: single
title: Research
permalink: /research/
excerpt: Research projects in multi-agent learning, energy forecasting, local credit assignment, and budgeted software verification.
---

My research projects explore learning and coordination in multi-agent systems, deep learning for energy forecasting, and reproducible studies of reward decomposition and software verification.

{% assign research_entries = site.research | where_exp: 'entry', 'entry.published == true' | sort: 'order' %}
{% for entry in research_entries %}
<section class="content-entry">
  <h2><a href="{{ entry.url | relative_url }}">{{ entry.title | escape }}</a></h2>
  {% if entry.supervisors.size > 0 %}<p class="entry-meta">Supervised by {{ entry.supervisors | join: ' and ' | escape }}</p>{% endif %}
  <p>{{ entry.excerpt | escape }}</p>
  {% if entry.tags.size > 0 %}<p class="entry-technologies">{{ entry.tags | join: ' · ' | escape }}</p>{% endif %}
  <p class="project-entry__links"><a href="{{ entry.url | relative_url }}">Research details<span class="visually-hidden">: {{ entry.title | escape }}</span></a>{% if entry.repository_url and entry.repository_url != '' %}<a href="{{ entry.repository_url | escape }}">GitHub{% if entry.repository_name and entry.repository_name != '' %}: {{ entry.repository_name | escape }}{% endif %}</a>{% endif %}</p>
</section>
{% endfor %}

{% include more-repositories.html %}

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
