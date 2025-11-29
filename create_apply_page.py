#!/usr/bin/env python3
"""
Create apply.html page from index.html template
"""

import re

# Read index.html to extract CSS, header, footer, and JS
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css = css_match.group(1) if css_match else ''

# Extract header HTML
header_match = re.search(r'(<!-- Header -->.*?</header>)', content, re.DOTALL)
header_template = header_match.group(1) if header_match else ''

# Extract footer HTML  
footer_match = re.search(r'(<!-- Footer -->.*?</footer>)', content, re.DOTALL)
footer_template = footer_match.group(1) if footer_match else ''

# Extract JavaScript
js_matches = re.findall(r'(<script>.*?</script>)', content, re.DOTALL)
js = '\n'.join(js_matches) if js_matches else ''

# Extract application form section
apply_match = re.search(r'(<!-- Application Section -->.*?</section>)', content, re.DOTALL)
apply_content = apply_match.group(1) if apply_match else ''

# Function to create apply page
def create_apply_page():
    nav_links = {
        'index.html': 'Home',
        'index.html#about': 'About',
        'index.html#programs': 'Programs',
        'index.html#team': 'Team',
        'index.html#gallery': 'Gallery',
        'testimonials.html': 'Testimonials',
        'resources.html': 'Resources',
        'events.html': 'Events',
        'faq.html': 'FAQ',
        'apply.html': 'Apply',
        'index.html#contact': 'Contact'
    }
    
    nav_html = '<ul class="nav-links" id="navLinks">\n'
    for link, label in nav_links.items():
        active = ' class="active"' if link == 'apply.html' else ''
        nav_html += f'                    <li><a href="{link}"{active}>{label}</a></li>\n'
    nav_html += '                </ul>'
    
    # Update header
    page_header = header_template.replace(
        re.search(r'<ul class="nav-links" id="navLinks">.*?</ul>', header_template, re.DOTALL).group(0),
        nav_html
    ) if re.search(r'<ul class="nav-links" id="navLinks">', header_template) else header_template
    
    # Update footer links
    footer_updated = footer_template.replace('href="#', 'href="')
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Apply to YPSF - Join our fellowship program, workshops, or become a volunteer. Make a difference in education and employment advocacy.">
    <meta name="keywords" content="YPSF, apply, fellowship, application, volunteer, youth advocacy, education, SDG 4, SDG 8">
    <meta name="author" content="YPSF">
    <title>Apply to YPSF | Youth Publications & Socioeconomic Forum</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
{css}
    </style>
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <div class="loader" id="loader"><div class="loader-spinner"></div></div>
    <div class="aurora-background"></div>
    <div class="particles">
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
    </div>
{page_header}
    <main id="main-content">
{apply_content}
    </main>
{footer_updated}
{js}
</body>
</html>"""

# Write apply.html
with open('apply.html', 'w', encoding='utf-8') as f:
    f.write(create_apply_page())
print('✓ Created apply.html')

