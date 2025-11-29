#!/usr/bin/env python3
"""
Generate multi-page YPSF website with shared CSS and enhanced content
"""

import re

# Read the main index.html to extract CSS and header/footer
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS (everything between <style> and </style>)
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css = css_match.group(1) if css_match else ''

# Extract header HTML
header_match = re.search(r'(<!-- Header -->.*?</header>)', content, re.DOTALL)
header = header_match.group(1) if header_match else ''

# Extract footer HTML  
footer_match = re.search(r'(<!-- Footer -->.*?</footer>)', content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

# Extract JavaScript (everything between <script> and </script>)
js_match = re.search(r'(<script>.*?</script>)', content, re.DOTALL)
js = js_match.group(1) if js_match else ''

# Function to create a page
def create_page(title, description, page_content, current_page=''):
    # Update header navigation
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
        active = ' class="active"' if link == current_page else ''
        nav_html += f'                    <li><a href="{link}"{active}>{label}</a></li>\n'
    nav_html += '                </ul>'
    
    # Update header with navigation
    page_header = header.replace(
        '<ul class="nav-links" id="navLinks">',
        nav_html.split('<ul class="nav-links" id="navLinks">')[0] + nav_html
    ) if '<ul class="nav-links" id="navLinks">' in header else header
    
    # Update footer links
    footer_links = footer.replace('href="#', 'href="')
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="keywords" content="YPSF, youth advocacy, education, SDG 4, SDG 8, youth publications, socioeconomic forum, youth empowerment, policy advocacy">
    <meta name="author" content="YPSF">
    <title>{title} | YPSF - Youth Publications & Socioeconomic Forum</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
{css}
    </style>
</head>
<body>
    <!-- Skip to Main Content (Accessibility) -->
    <a href="#main-content" class="skip-link">Skip to main content</a>
    
    <!-- Loading Screen -->
    <div class="loader" id="loader">
        <div class="loader-spinner"></div>
    </div>
    
    <!-- Animated Background -->
    <div class="aurora-background"></div>
    <div class="particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
    </div>
    
{page_header}
    
    <main id="main-content">
{page_content}
    </main>

{footer_links}

{js}
</body>
</html>"""

# Create Testimonials page
testimonials_content = """    <!-- Testimonials Page -->
    <section class="section" style="padding-top: 8rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">Testimonials</span>
                <h1 class="section-title">What Our Community Says</h1>
                <p class="section-subtitle">Hear from fellows, partners, and participants about their transformative YPSF experience</p>
            </div>
            
            <div class="grid grid-3" style="margin-bottom: 4rem;">
                <div class="card fade-in-scroll">
                    <div style="font-size: 1.25rem; line-height: 1.9; color: var(--ink); margin-bottom: 2rem; font-style: italic; position: relative; padding-left: 1.5rem;">
                        <span style="position: absolute; left: 0; top: -0.5rem; font-size: 3rem; color: var(--red-pale); line-height: 1;">"</span>
                        YPSF provided me with the platform and support I needed to turn my research into actionable policy recommendations. The mentorship and network I gained are invaluable. Through the fellowship, I connected with policymakers and created real change in my community.
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; padding-top: 1.5rem; border-top: 1px solid var(--glass-border);">
                        <img src="team13.jpg" alt="Sarah Johnson" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 3px solid var(--red-pale);">
                        <div>
                            <div style="font-weight: 700; color: var(--ink); margin-bottom: 0.25rem; font-size: 1.1rem;">Sarah Johnson</div>
                            <div style="font-size: 0.95rem; color: var(--muted);">YPSF Fellow 2023</div>
                            <div style="font-size: 0.85rem; color: var(--red-medium); margin-top: 0.25rem;">Education Policy Researcher</div>
                        </div>
                    </div>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="font-size: 1.25rem; line-height: 1.9; color: var(--ink); margin-bottom: 2rem; font-style: italic; position: relative; padding-left: 1.5rem;">
                        <span style="position: absolute; left: 0; top: -0.5rem; font-size: 3rem; color: var(--red-pale); line-height: 1;">"</span>
                        The workshops and publications lab helped me develop skills I now use daily in my advocacy work. YPSF truly empowers young voices. I've published three policy briefs and presented at international conferences thanks to this experience.
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; padding-top: 1.5rem; border-top: 1px solid var(--glass-border);">
                        <img src="team14.jpg" alt="Michael Chen" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 3px solid var(--red-pale);">
                        <div>
                            <div style="font-weight: 700; color: var(--ink); margin-bottom: 0.25rem; font-size: 1.1rem;">Michael Chen</div>
                            <div style="font-size: 0.95rem; color: var(--muted);">Workshop Participant 2023</div>
                            <div style="font-size: 0.85rem; color: var(--red-medium); margin-top: 0.25rem;">Youth Advocate</div>
                        </div>
                    </div>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="font-size: 1.25rem; line-height: 1.9; color: var(--ink); margin-bottom: 2rem; font-style: italic; position: relative; padding-left: 1.5rem;">
                        <span style="position: absolute; left: 0; top: -0.5rem; font-size: 3rem; color: var(--red-pale); line-height: 1;">"</span>
                        Partnering with YPSF has been transformative. Their evidence-based approach and youth-centered methodology create real impact. We've co-authored research that influenced national education policy, and their fellows bring fresh perspectives to our work.
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; padding-top: 1.5rem; border-top: 1px solid var(--glass-border);">
                        <img src="team15.jpg" alt="Dr. Aisha Patel" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 3px solid var(--red-pale);">
                        <div>
                            <div style="font-weight: 700; color: var(--ink); margin-bottom: 0.25rem; font-size: 1.1rem;">Dr. Aisha Patel</div>
                            <div style="font-size: 0.95rem; color: var(--muted);">Partner Organization</div>
                            <div style="font-size: 0.85rem; color: var(--red-medium); margin-top: 0.25rem;">Education Director</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Additional Testimonials -->
            <div class="section-header" style="margin-top: 4rem;">
                <h2 class="section-title">More Stories from Our Community</h2>
            </div>
            
            <div class="grid grid-2" style="margin-top: 3rem;">
                <div class="card fade-in-scroll">
                    <div style="font-size: 1.1rem; line-height: 1.8; color: var(--ink); margin-bottom: 1.5rem; font-style: italic;">
                        "As a volunteer, I've gained incredible experience in research and advocacy. YPSF's commitment to youth empowerment is evident in everything they do."
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <img src="team16.jpg" alt="Alex Rivera" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
                        <div>
                            <div style="font-weight: 700; color: var(--ink);">Alex Rivera</div>
                            <div style="font-size: 0.9rem; color: var(--muted);">Volunteer & Research Assistant</div>
                        </div>
                    </div>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="font-size: 1.1rem; line-height: 1.8; color: var(--ink); margin-bottom: 1.5rem; font-style: italic;">
                        "The networking opportunities through YPSF opened doors I never imagined. I'm now working with a major NGO thanks to connections I made here."
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <img src="team17.jpg" alt="Priya Sharma" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
                        <div>
                            <div style="font-weight: 700; color: var(--ink);">Priya Sharma</div>
                            <div style="font-size: 0.9rem; color: var(--muted);">Former Fellow, Now NGO Program Manager</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 4rem;">
                <a href="apply.html" class="btn btn-primary">Join Our Community</a>
            </div>
        </div>
    </section>"""

# Write testimonials page
with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(create_page(
        'Testimonials',
        'Read testimonials from YPSF fellows, partners, and participants about their transformative experiences',
        testimonials_content,
        'testimonials.html'
    ))

print("✓ Created testimonials.html")

