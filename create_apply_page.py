#!/usr/bin/env python3
"""
Create apply.html page from index.html structure
"""

import re

# Read index.html to extract CSS, header, footer, and application form
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
apply_section_match = re.search(r'(<!-- Application Section -->.*?</section>)', content, re.DOTALL)
apply_section = apply_section_match.group(1) if apply_section_match else ''

# Function to create apply page
def create_apply_page():
    nav_links = {
        'index.html': 'Home',
        'about.html': 'About',
        'programs.html': 'Programs',
        'team.html': 'Team',
        'gallery.html': 'Gallery',
        'testimonials.html': 'Testimonials',
        'resources.html': 'Resources',
        'events.html': 'Events',
        'faq.html': 'FAQ',
        'apply.html': 'Apply',
        'contact.html': 'Contact'
    }
    
    nav_html = '<ul class="nav-links" id="navLinks">\n'
    for link, label in nav_links.items():
        if link == 'apply.html':
            # Make Apply button stand out
            nav_html += f'                    <li><a href="{link}" class="active nav-apply-btn">{label}</a></li>\n'
        else:
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
    
    # Update apply section to remove id="apply" since it's now a full page
    apply_content = apply_section.replace('id="apply"', '').replace('href="#apply"', 'href="apply.html"')
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Apply to join YPSF Fellowship Programme, workshops, or become a volunteer. Make a difference in youth education and employment advocacy.">
    <meta name="keywords" content="YPSF, apply, fellowship, volunteer, application, youth advocacy, education, SDG 4, SDG 8">
    <meta name="author" content="YPSF">
    <title>Apply | YPSF - Youth Publications & Socioeconomic Forum</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
{css}
        /* Make Apply button stand out in navbar */
        .nav-apply-btn {{
            background: rgba(255, 255, 255, 0.25) !important;
            border: 2px solid rgba(255, 255, 255, 0.5) !important;
            border-radius: var(--radius-md) !important;
            padding: var(--spacing-xs) var(--spacing-md) !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
            transition: all var(--transition-base) !important;
        }}
        
        .nav-apply-btn:hover {{
            background: rgba(255, 255, 255, 0.35) !important;
            border-color: rgba(255, 255, 255, 0.8) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
        }}
        
        .nav-apply-btn.active {{
            background: rgba(255, 255, 255, 0.3) !important;
            border-color: white !important;
        }}
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

