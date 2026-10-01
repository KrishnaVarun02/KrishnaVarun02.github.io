---
layout: single
title: About me
permalink: /
excerpt: Software engineer at Oracle and IIT (BHU) CSE alumnus working across AI agents, cloud infrastructure, data engineering, and machine learning research.
---

Hi, I'm {{ site.author.name }}, a software engineer at Oracle in Bengaluru and a Computer Science and Engineering graduate of IIT (BHU), Varanasi. My work spans AI-assisted engineering, cloud and blockchain infrastructure, and real-time data systems.

My projects explore multi-agent developer tools, reinforcement learning, and deep learning for energy forecasting. Outside engineering, I enjoy competitive programming, mentoring, boxing, and running.

## Selected work

{% assign selected_projects = site.projects | where: 'published', true | where: 'featured', true | sort: 'order' %}
{% for project in selected_projects %}
- [{{ project.title }}]({{ project.url | relative_url }}) — {{ project.excerpt }}
{% endfor %}
{% assign selected_research = site.research | where: 'published', true | where: 'featured', true | sort: 'order' %}
{% for research in selected_research %}
- [{{ research.title }}]({{ research.url | relative_url }}) — {{ research.excerpt }}
{% endfor %}

[All projects]({{ '/projects/' | relative_url }}) · [Research]({{ '/research/' | relative_url }}) · [Experience]({{ '/experience/' | relative_url }})

## Highlights

- B.Tech in Computer Science and Engineering, IIT (BHU), with a CPI of 8.46/10.
- Led the five-member Think Tank team to the [Oracle FY26 Global Tech Program championship]({{ '/community/#oracle-global-tech-program' | relative_url }}), February 2026.
- Codeforces Expert, CodeChef 4 Star, and LeetCode Knight, as reported in my resume. [More achievements]({{ '/achievements/' | relative_url }}).

You can find both resumes on my [CV page]({{ '/cv/' | relative_url }}) or [get in touch]({{ '/contact/' | relative_url }}).
