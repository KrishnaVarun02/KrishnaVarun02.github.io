---
layout: single
title: Contact
permalink: /contact/
excerpt: Get in touch by email or connect on GitHub and LinkedIn.
---

{% assign contact_location = site.author.location | default: '' | strip %}
{% assign contact_email = site.author.email | default: '' | strip %}
{% assign contact_github = site.author.github | default: '' | strip %}
{% assign contact_linkedin = site.author.linkedin | default: '' | strip %}
{% assign contact_phone = site.author.phone | default: '' | strip %}

{% if contact_location != '' %}I'm based in {{ contact_location | escape }}. {% endif %}I welcome conversations about software engineering, AI agents, data systems, and research.{% if contact_email != '' %} Email is the best way to reach me.{% endif %}

<ul class="contact-list">
{% if contact_email != '' %}<li><strong>Email:</strong> <a href="mailto:{{ contact_email | escape }}">{{ contact_email | escape }}</a></li>{% endif %}
{% if contact_github != '' %}<li><strong>GitHub:</strong> <a href="{{ contact_github | escape }}">{{ contact_github | remove: 'https://' | escape }}</a></li>{% endif %}
{% if contact_linkedin != '' %}<li><strong>LinkedIn:</strong> <a href="{{ contact_linkedin | escape }}">{{ site.author.name | escape }} on LinkedIn</a></li>{% endif %}
{% if site.author.show_phone == true and contact_phone != '' %}<li><strong>Phone:</strong> <a href="tel:{{ contact_phone | remove: ' ' | escape }}">{{ contact_phone | escape }}</a></li>{% endif %}
</ul>
