---
layout: single
title: Contact
permalink: /contact/
excerpt: Get in touch by email or connect on GitHub and LinkedIn.
---

I'm based in {{ site.author.location }}. For conversations about software engineering, AI agents, data systems, or research, email is the best way to reach me.

<ul class="contact-list">
{% if site.author.email and site.author.email != '' %}<li><strong>Email:</strong> <a href="mailto:{{ site.author.email | escape }}">{{ site.author.email | escape }}</a></li>{% endif %}
{% if site.author.github and site.author.github != '' %}<li><strong>GitHub:</strong> <a href="{{ site.author.github | escape }}">{{ site.author.github | remove: 'https://' | escape }}</a></li>{% endif %}
{% if site.author.linkedin and site.author.linkedin != '' %}<li><strong>LinkedIn:</strong> <a href="{{ site.author.linkedin | escape }}">{{ site.author.name | escape }} on LinkedIn</a></li>{% endif %}
{% if site.author.show_phone and site.author.phone and site.author.phone != '' %}<li><strong>Phone:</strong> <a href="tel:{{ site.author.phone | remove: ' ' | escape }}">{{ site.author.phone | escape }}</a></li>{% endif %}
</ul>
