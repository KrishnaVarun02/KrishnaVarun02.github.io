---
layout: single
title: Research
permalink: /research/
excerpt: Undergraduate research-oriented work in machine learning, cooperative decision-making, forecasting, and reliable evaluation.
---

My undergraduate research-oriented work at **IIT (BHU) Varanasi** spans machine learning systems, intelligent decision-making, time-series forecasting, and reliable evaluation. Across these projects, I have studied how computational methods behave under controlled experimental settings, implemented learning and evaluation pipelines, and used quantitative comparisons to understand both their strengths and limitations.

The projects cover **multi-agent reinforcement learning and reward decomposition, neural time-series forecasting, cooperative decision-quality diagnostics, and budgeted software verification**. Together, they reflect an early research foundation built around formulating technical questions, implementing computational methods, designing experiments, analyzing results, and making reproducible evidence available for inspection.

{% assign research_entries = site.research | where_exp: 'entry', 'entry.published == true' | sort: 'order' %}
{% for entry in research_entries %}
<section class="content-entry">
  <h2><a href="{{ entry.url | relative_url }}">{{ entry.title | escape }}</a></h2>
  {% if entry.title == "Local Credit Diagnostics" or entry.title == "PatchBudget" %}<p class="entry-meta">Research-oriented project</p>{% elsif entry.supervisors.size > 0 %}<p class="entry-meta">Undergraduate research project{% if entry.supervisors.size > 0 %}; guided by {{ entry.supervisors | join: ' and ' | escape }}{% endif %}</p>{% else %}<p class="entry-meta">Undergraduate research-oriented project</p>{% endif %}
  <p>{{ entry.excerpt | escape }}</p>
  {% if entry.tags.size > 0 %}<p class="entry-technologies">{{ entry.tags | join: ' · ' | escape }}</p>{% endif %}
  <p class="project-entry__links"><a href="{{ entry.url | relative_url }}">Research details<span class="visually-hidden">: {{ entry.title | escape }}</span></a>{% if entry.repository_url and entry.repository_url != '' %}<a href="{{ entry.repository_url | escape }}">Repository{% if entry.repository_name and entry.repository_name != '' %}: {{ entry.repository_name | escape }}{% endif %}</a>{% endif %}</p>
</section>
{% endfor %}

{% include more-repositories.html %}
