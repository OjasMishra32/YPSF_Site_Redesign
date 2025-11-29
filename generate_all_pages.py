#!/usr/bin/env python3
"""
Generate all multi-page YPSF website pages with enhanced content
"""

import re

# Read the main index.html to extract CSS and header/footer
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

# Function to create a page
def create_page(title, description, page_content, current_page=''):
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
{page_content}
    </main>
{footer_updated}
{js}
</body>
</html>"""

# Testimonials Page
testimonials = """    <section class="section" style="padding-top: 8rem;">
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

# Resources Page
resources = """    <section class="section" style="padding-top: 8rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">Resources</span>
                <h1 class="section-title">Publications & Resources</h1>
                <p class="section-subtitle">Access our latest research, policy briefs, toolkits, and educational materials to advance your work in education and employment</p>
            </div>
            
            <div class="feature-grid" style="margin-bottom: 4rem;">
                <div class="card fade-in-scroll">
                    <div style="width: 60px; height: 60px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 2rem;">📄</div>
                    <h3>Policy Briefs</h3>
                    <p style="margin-bottom: 1.5rem;">Evidence-based policy recommendations on education and employment issues affecting youth globally. Our briefs synthesize research findings into actionable recommendations for policymakers, educators, and advocates.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Youth Employment in Post-Pandemic Economies</li>
                        <li>Inclusive Education Access Strategies</li>
                        <li>Digital Skills for Decent Work</li>
                        <li>Youth Entrepreneurship Support Policies</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline">View All Publications</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 60px; height: 60px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 2rem;">📊</div>
                    <h3>Research Reports</h3>
                    <p style="margin-bottom: 1.5rem;">Comprehensive research studies on youth employment, education access, and socioeconomic challenges. Our reports combine quantitative data with qualitative insights from youth voices worldwide.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Global Youth Employment Trends 2024</li>
                        <li>Education Quality Assessment Framework</li>
                        <li>Youth-Led Policy Change Case Studies</li>
                        <li>Digital Divide Impact Analysis</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline">Download Reports</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 60px; height: 60px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 2rem;">🛠️</div>
                    <h3>Toolkits & Guides</h3>
                    <p style="margin-bottom: 1.5rem;">Practical toolkits and guides for youth advocates, researchers, and educators. Step-by-step resources to help you conduct research, create policy briefs, and organize advocacy campaigns.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Youth Advocacy Toolkit</li>
                        <li>Research Methodology Guide</li>
                        <li>Policy Brief Writing Handbook</li>
                        <li>Community Engagement Strategies</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline">Access Toolkits</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 60px; height: 60px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 2rem;">📚</div>
                    <h3>Case Studies</h3>
                    <p style="margin-bottom: 1.5rem;">Real-world case studies showcasing successful youth-led initiatives and partnerships. Learn from examples of how young people are creating change in their communities.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Fellowship Project Success Stories</li>
                        <li>Partnership Impact Examples</li>
                        <li>Community-Led Education Programs</li>
                        <li>Youth Employment Initiatives</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline">Read Case Studies</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 60px; height: 60px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 2rem;">🎥</div>
                    <h3>Multimedia</h3>
                    <p style="margin-bottom: 1.5rem;">Videos, podcasts, and interactive content exploring key issues and featuring youth voices. Engaging multimedia resources that bring our research and stories to life.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Youth Voices Podcast Series</li>
                        <li>Policy Brief Video Summaries</li>
                        <li>Workshop Recordings</li>
                        <li>Interactive Data Visualizations</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline">Watch Videos</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 60px; height: 60px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 2rem;">📧</div>
                    <h3>Newsletter</h3>
                    <p style="margin-bottom: 1.5rem;">Stay updated with our monthly newsletter featuring updates, opportunities, and insights. Get the latest research findings, event announcements, and success stories delivered to your inbox.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Monthly Research Highlights</li>
                        <li>Upcoming Event Announcements</li>
                        <li>Fellow Spotlights</li>
                        <li>Partnership Opportunities</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline">Subscribe Now</a>
                </div>
            </div>
            
            <div class="card card-accent" style="margin-top: 4rem; text-align: center; padding: 3rem;">
                <h2 style="margin-bottom: 1rem;">Request Access to Resources</h2>
                <p style="margin-bottom: 2rem; font-size: 1.1rem;">Many of our resources are available upon request. Contact us to access full reports, toolkits, and exclusive content.</p>
                <a href="contact.html" class="btn btn-primary">Contact Us</a>
            </div>
        </div>
    </section>"""

# Partners Page
partners = """    <section class="section" style="padding-top: 8rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">Partners</span>
                <h1 class="section-title">Our Network & Partners</h1>
                <p class="section-subtitle">Collaborating with organizations, institutions, and networks worldwide to advance youth empowerment and policy change</p>
            </div>
            
            <div class="grid grid-4" style="margin-bottom: 4rem;">
                <div class="card fade-in-scroll" style="text-align: center; padding: 2.5rem;">
                    <img src="MGCY.png" alt="MGCY Partner" style="max-width: 180px; height: auto; margin: 0 auto 1.5rem; display: block; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));">
                    <h3 style="margin-bottom: 0.5rem;">MGCY</h3>
                    <p style="color: var(--muted); margin-bottom: 1rem;">Major Group for Children and Youth</p>
                    <p style="font-size: 0.95rem; line-height: 1.6;">Official UN constituency representing children and youth in sustainable development processes.</p>
                </div>
                
                <div class="card fade-in-scroll" style="text-align: center; padding: 2.5rem;">
                    <div style="width: 180px; height: 120px; background: linear-gradient(135deg, var(--red-pale), var(--red-light)); border-radius: 12px; margin: 0 auto 1.5rem; display: flex; align-items: center; justify-content: center; box-shadow: var(--shadow-md);">
                        <span style="color: var(--red-medium); font-weight: 700; font-size: 1.1rem;">Educational<br>Institutions</span>
                    </div>
                    <h3 style="margin-bottom: 0.5rem;">Educational Institutions</h3>
                    <p style="color: var(--muted); margin-bottom: 1rem;">Universities and Research Centers</p>
                    <p style="font-size: 0.95rem; line-height: 1.6;">Partnering with leading universities and research institutions to advance evidence-based policy and practice.</p>
                </div>
                
                <div class="card fade-in-scroll" style="text-align: center; padding: 2.5rem;">
                    <div style="width: 180px; height: 120px; background: linear-gradient(135deg, var(--red-pale), var(--red-light)); border-radius: 12px; margin: 0 auto 1.5rem; display: flex; align-items: center; justify-content: center; box-shadow: var(--shadow-md);">
                        <span style="color: var(--red-medium); font-weight: 700; font-size: 1.1rem;">NGO<br>Partners</span>
                    </div>
                    <h3 style="margin-bottom: 0.5rem;">NGO Partners</h3>
                    <p style="color: var(--muted); margin-bottom: 1rem;">Non-Governmental Organizations</p>
                    <p style="font-size: 0.95rem; line-height: 1.6;">Collaborating with NGOs worldwide to amplify youth voices and create sustainable impact in communities.</p>
                </div>
                
                <div class="card fade-in-scroll" style="text-align: center; padding: 2.5rem;">
                    <div style="width: 180px; height: 120px; background: linear-gradient(135deg, var(--red-pale), var(--red-light)); border-radius: 12px; margin: 0 auto 1.5rem; display: flex; align-items: center; justify-content: center; box-shadow: var(--shadow-md);">
                        <span style="color: var(--red-medium); font-weight: 700; font-size: 1.1rem;">Private<br>Sector</span>
                    </div>
                    <h3 style="margin-bottom: 0.5rem;">Private Sector</h3>
                    <p style="color: var(--muted); margin-bottom: 1rem;">Corporate Partners and Employers</p>
                    <p style="font-size: 0.95rem; line-height: 1.6;">Working with forward-thinking companies to create employment opportunities and support youth development.</p>
                </div>
            </div>
            
            <div class="section-header" style="margin-top: 4rem;">
                <h2 class="section-title">Partnership Opportunities</h2>
                <p class="section-subtitle">We welcome partnerships with organizations that share our commitment to youth empowerment</p>
            </div>
            
            <div class="grid grid-2" style="margin-top: 3rem;">
                <div class="card fade-in-scroll">
                    <h3>Co-Host Workshops & Events</h3>
                    <p>Partner with us to organize workshops, webinars, and conferences that advance education and employment goals. We bring youth perspectives and research expertise to collaborative events.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; line-height: 2; margin-top: 1rem;">
                        <li>Joint workshop development and facilitation</li>
                        <li>Co-branded event marketing and promotion</li>
                        <li>Shared resources and expertise</li>
                        <li>Expanded participant networks</li>
                    </ul>
                </div>
                
                <div class="card fade-in-scroll">
                    <h3>Co-Author Research & Publications</h3>
                    <p>Collaborate on research projects and policy briefs that combine your institutional knowledge with our youth-centered methodology and global network.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; line-height: 2; margin-top: 1rem;">
                        <li>Joint research initiatives</li>
                        <li>Co-authored policy briefs and reports</li>
                        <li>Shared publication platforms</li>
                        <li>Cross-institutional learning</li>
                    </ul>
                </div>
                
                <div class="card fade-in-scroll">
                    <h3>Support Fellowship Program</h3>
                    <p>Sponsor fellows, provide mentorship, or offer resources to support our flagship fellowship program. Help us empower the next generation of youth leaders.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; line-height: 2; margin-top: 1rem;">
                        <li>Fellowship sponsorship opportunities</li>
                        <li>Mentorship program participation</li>
                        <li>Resource and funding support</li>
                        <li>Access to talented youth leaders</li>
                    </ul>
                </div>
                
                <div class="card fade-in-scroll">
                    <h3>Pilot Projects & Initiatives</h3>
                    <p>Launch pilot projects together that test innovative approaches to education and employment challenges. Combine resources and expertise for greater impact.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; line-height: 2; margin-top: 1rem;">
                        <li>Innovative program development</li>
                        <li>Pilot testing and evaluation</li>
                        <li>Scalable solution design</li>
                        <li>Impact measurement and reporting</li>
                    </ul>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 4rem;">
                <div class="card card-accent" style="max-width: 800px; margin: 0 auto; padding: 3rem;">
                    <h2 style="margin-bottom: 1rem;">Interested in Partnering?</h2>
                    <p style="margin-bottom: 2rem; font-size: 1.1rem;">We're always looking for organizations that share our vision. Contact us to discuss partnership opportunities.</p>
                    <a href="contact.html" class="btn btn-primary">Contact Us</a>
                </div>
            </div>
        </div>
    </section>"""

# FAQ Page
faq = """    <section class="section" style="padding-top: 8rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">FAQ</span>
                <h1 class="section-title">Frequently Asked Questions</h1>
                <p class="section-subtitle">Common questions about YPSF, our programs, and how to get involved</p>
            </div>
            
            <div style="max-width: 900px; margin: 0 auto;">
                <div class="accordion-container">
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">What is the YPSF Fellowship Programme?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>The YPSF Fellowship Programme is a hands-on experience designed to empower young leaders through research, storytelling, and public engagement. Fellows work on projects aligned with SDG 4 (Quality Education) and SDG 8 (Decent Work), receiving personalized mentorship, publication opportunities, and access to our global network. The program typically runs for 6-12 months and includes regular cohort sessions, one-on-one mentorship, and public showcase opportunities.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">Who can apply to YPSF?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>YPSF welcomes applications from young people aged 18-35 who are passionate about education and employment issues. We value diversity and encourage applications from all backgrounds, regions, and experiences. No prior experience is required - we're looking for passion, commitment, and a drive to create change. Whether you're a student, recent graduate, young professional, or community organizer, if you're committed to advancing youth rights and opportunities, we want to hear from you.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">Is there a deadline for applications?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>We accept applications on a rolling basis. There is no deadline - you can apply whenever you're ready. We review applications regularly and will get back to you within 2-3 weeks of submission. This flexible approach allows us to welcome new members throughout the year and ensures that opportunities are accessible to all interested youth.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">What support do fellows receive?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>Fellows receive comprehensive support including personalized mentorship from experienced researchers and advocates, participation in peer cohort sessions, monthly opportunities to publish their work, public showcase of their deliverables via our channels, and access to panels, roundtables, and partner events. We also provide guidance on research methodologies, writing, policy advocacy, and professional development. Additionally, fellows gain access to our global network of youth leaders, researchers, and policymakers.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">Can I volunteer with YPSF?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>Yes! We welcome volunteers who can contribute skills in research, writing, facilitation, operations, communications, or other areas. Volunteers play a crucial role in our work and gain valuable experience while making a difference. Use the application form and select "Volunteer" as your program interest. Volunteer opportunities range from short-term projects to ongoing commitments, and we work with volunteers to find roles that match their interests and availability.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">How can organizations partner with YPSF?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>We partner with educational institutions, NGOs, private sector organizations, and government agencies. Partnership opportunities include co-hosting workshops, co-authoring policy briefs, launching pilot projects, and supporting our fellowship program. Please contact us at info@ypsf.org to discuss partnership opportunities. We're particularly interested in partnerships that amplify youth voices, advance evidence-based policy, and create sustainable impact in communities worldwide.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">Where does YPSF operate?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>YPSF is a global network with members and partners across multiple countries. We operate as a remote-first organization, allowing us to work with youth leaders worldwide. Our programs and activities take place both online and in-person, depending on the context and opportunities available. This global reach enables us to address education and employment challenges from diverse perspectives and create solutions that work across different contexts.</p>
                        </div>
                    </div>
                    
                    <div class="accordion fade-in-scroll">
                        <div class="accordion-header">
                            <h3 style="margin: 0; font-size: 1.2rem; font-weight: 700;">How is YPSF funded?</h3>
                            <span class="accordion-icon">▼</span>
                        </div>
                        <div class="accordion-content">
                            <p>YPSF is funded through a combination of grants, partnerships, donations, and in-kind support from individuals, foundations, and organizations that believe in our mission. We are committed to transparency and ethical fundraising practices. If you're interested in supporting our work, please contact us. We ensure that all funding supports our core mission of empowering youth voices and advancing education and employment opportunities.</p>
                        </div>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 4rem;">
                    <div class="card card-accent" style="padding: 3rem;">
                        <h2 style="margin-bottom: 1rem;">Still Have Questions?</h2>
                        <p style="margin-bottom: 2rem; font-size: 1.1rem;">Can't find what you're looking for? We're here to help!</p>
                        <a href="contact.html" class="btn btn-primary">Contact Us</a>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Events Page
events = """    <section class="section" style="padding-top: 8rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">Events</span>
                <h1 class="section-title">Upcoming Events & Opportunities</h1>
                <p class="section-subtitle">Join us for workshops, webinars, conferences, and networking events that advance youth empowerment</p>
            </div>
            
            <div class="grid grid-3" style="margin-bottom: 4rem;">
                <div class="card fade-in-scroll">
                    <div class="badge badge-primary" style="margin-bottom: 1.5rem;">Upcoming</div>
                    <h3 style="margin-bottom: 1rem;">Youth Advocacy Workshop</h3>
                    <div style="margin-bottom: 1rem; padding: 1rem; background: var(--bg-off); border-radius: 8px;">
                        <p style="margin-bottom: 0.5rem;"><strong>Date:</strong> To Be Announced</p>
                        <p style="margin-bottom: 0.5rem;"><strong>Format:</strong> Online</p>
                        <p style="margin-bottom: 0.5rem;"><strong>Duration:</strong> 3 hours</p>
                        <p style="margin-bottom: 0;"><strong>Cost:</strong> Free</p>
                    </div>
                    <p style="margin-bottom: 1.5rem; line-height: 1.8;">Learn essential advocacy skills and strategies for creating policy change. This interactive workshop covers research methods, communication techniques, coalition-building, and how to effectively engage with policymakers. Perfect for youth advocates looking to amplify their impact.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Policy analysis and research</li>
                        <li>Effective communication strategies</li>
                        <li>Coalition building techniques</li>
                        <li>Engaging with decision-makers</li>
                    </ul>
                    <a href="apply.html" class="btn btn-outline" style="width: 100%;">Register Now</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div class="badge badge-primary" style="margin-bottom: 1.5rem;">Upcoming</div>
                    <h3 style="margin-bottom: 1rem;">Research Methodology Training</h3>
                    <div style="margin-bottom: 1rem; padding: 1rem; background: var(--bg-off); border-radius: 8px;">
                        <p style="margin-bottom: 0.5rem;"><strong>Date:</strong> To Be Announced</p>
                        <p style="margin-bottom: 0.5rem;"><strong>Format:</strong> Hybrid (Online + In-Person)</p>
                        <p style="margin-bottom: 0.5rem;"><strong>Duration:</strong> Full Day</p>
                        <p style="margin-bottom: 0;"><strong>Cost:</strong> Free</p>
                    </div>
                    <p style="margin-bottom: 1.5rem; line-height: 1.8;">Develop your research skills with our comprehensive training on qualitative and quantitative research methods, data analysis, and evidence-based reporting. This intensive session is designed for youth researchers and advocates who want to produce high-quality research.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Qualitative research methods</li>
                        <li>Quantitative data analysis</li>
                        <li>Ethical research practices</li>
                        <li>Writing evidence-based reports</li>
                    </ul>
                    <a href="apply.html" class="btn btn-outline" style="width: 100%;">Register Now</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div class="badge badge-secondary" style="margin-bottom: 1.5rem;">Ongoing</div>
                    <h3 style="margin-bottom: 1rem;">Monthly Networking Sessions</h3>
                    <div style="margin-bottom: 1rem; padding: 1rem; background: var(--bg-off); border-radius: 8px;">
                        <p style="margin-bottom: 0.5rem;"><strong>Frequency:</strong> Monthly</p>
                        <p style="margin-bottom: 0.5rem;"><strong>Format:</strong> Online</p>
                        <p style="margin-bottom: 0.5rem;"><strong>Duration:</strong> 1.5 hours</p>
                        <p style="margin-bottom: 0;"><strong>Cost:</strong> Free</p>
                    </div>
                    <p style="margin-bottom: 1.5rem; line-height: 1.8;">Connect with fellow youth leaders, share experiences, and build your network. These informal sessions are open to all YPSF members and partners. Each session features different themes, guest speakers, and networking opportunities.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2;">
                        <li>Peer networking opportunities</li>
                        <li>Guest speaker presentations</li>
                        <li>Project sharing and feedback</li>
                        <li>Collaboration opportunities</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline" style="width: 100%;">Learn More</a>
                </div>
            </div>
            
            <div class="section-header" style="margin-top: 4rem;">
                <h2 class="section-title">Past Events & Recordings</h2>
                <p class="section-subtitle">Missed an event? Access recordings and resources from our previous workshops and conferences</p>
            </div>
            
            <div class="grid grid-2" style="margin-top: 3rem;">
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 200px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">▶</div>
                    <h3>Policy Advocacy Masterclass</h3>
                    <p style="color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem;">Recorded: November 2023</p>
                    <p>Learn from experienced advocates about effective policy change strategies, stakeholder engagement, and coalition building.</p>
                    <a href="contact.html" class="btn btn-outline" style="margin-top: 1rem;">Watch Recording</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 200px; background: linear-gradient(135deg, var(--red-bright), var(--red-light)); border-radius: 12px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">▶</div>
                    <h3>Youth Employment Summit</h3>
                    <p style="color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem;">Recorded: October 2023</p>
                    <p>Explore innovative approaches to youth employment, featuring panel discussions with employers, policymakers, and youth leaders.</p>
                    <a href="contact.html" class="btn btn-outline" style="margin-top: 1rem;">Watch Recording</a>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 4rem;">
                <div class="card card-accent" style="max-width: 800px; margin: 0 auto; padding: 3rem;">
                    <h2 style="margin-bottom: 1rem;">Stay Updated</h2>
                    <p style="margin-bottom: 2rem; font-size: 1.1rem;">Subscribe to our newsletter to receive event announcements and updates directly in your inbox.</p>
                    <a href="contact.html" class="btn btn-primary">Subscribe to Newsletter</a>
                </div>
            </div>
        </div>
    </section>"""

# News Page
news = """    <section class="section" style="padding-top: 8rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">News & Updates</span>
                <h1 class="section-title">Latest News</h1>
                <p class="section-subtitle">Stay informed about our latest activities, publications, achievements, and opportunities</p>
            </div>
            
            <div class="grid grid-3" style="margin-bottom: 4rem;">
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 250px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; color: white; font-size: 4rem; font-weight: 900;">📄</div>
                    <div class="badge badge-outline" style="margin-bottom: 1rem;">Publication</div>
                    <h3 style="margin-bottom: 0.75rem;">New Policy Brief Released</h3>
                    <p style="color: var(--muted); font-size: 0.95rem; margin-bottom: 1rem; font-weight: 600;">Published on January 15, 2024</p>
                    <p style="margin-bottom: 1.5rem; line-height: 1.8;">We've released our latest policy brief on youth employment challenges in post-pandemic economies. The brief includes comprehensive analysis and actionable recommendations for policymakers and employers. Drawing on data from 15 countries, it highlights innovative approaches to creating decent work opportunities for young people.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2; font-size: 0.95rem;">
                        <li>Analysis of post-pandemic employment trends</li>
                        <li>Case studies from 15 countries</li>
                        <li>Policy recommendations for governments</li>
                        <li>Best practices for employers</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline" style="width: 100%;">Read Full Brief</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 250px; background: linear-gradient(135deg, var(--red-bright), var(--red-light)); border-radius: 12px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; color: white; font-size: 4rem; font-weight: 900;">🎓</div>
                    <div class="badge badge-outline" style="margin-bottom: 1rem;">Event</div>
                    <h3 style="margin-bottom: 0.75rem;">Fellowship Cohort 2024 Launched</h3>
                    <p style="color: var(--muted); font-size: 0.95rem; margin-bottom: 1rem; font-weight: 600;">Published on December 20, 2023</p>
                    <p style="margin-bottom: 1.5rem; line-height: 1.8;">We're excited to welcome our 2024 Fellowship cohort! This year's fellows come from 12 countries and will work on diverse projects addressing education and employment challenges. The cohort includes researchers, advocates, and community organizers who will collaborate over the next year to create meaningful impact.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2; font-size: 0.95rem;">
                        <li>12 countries represented</li>
                        <li>25 new fellows selected</li>
                        <li>Diverse project focus areas</li>
                        <li>Comprehensive mentorship program</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline" style="width: 100%;">Meet the Fellows</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 250px; background: linear-gradient(135deg, var(--red-deep), var(--red-medium)); border-radius: 12px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; color: white; font-size: 4rem; font-weight: 900;">🤝</div>
                    <div class="badge badge-outline" style="margin-bottom: 1rem;">Partnership</div>
                    <h3 style="margin-bottom: 0.75rem;">New Partnership Announced</h3>
                    <p style="color: var(--muted); font-size: 0.95rem; margin-bottom: 1rem; font-weight: 600;">Published on December 5, 2023</p>
                    <p style="margin-bottom: 1.5rem; line-height: 1.8;">YPSF has partnered with leading educational institutions to expand our research capacity and reach. This collaboration will enable us to produce more comprehensive studies, access additional resources, and create greater impact through combined expertise and networks.</p>
                    <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 2; font-size: 0.95rem;">
                        <li>Joint research initiatives</li>
                        <li>Shared publication platforms</li>
                        <li>Expanded mentorship network</li>
                        <li>Enhanced program resources</li>
                    </ul>
                    <a href="contact.html" class="btn btn-outline" style="width: 100%;">Learn More</a>
                </div>
            </div>
            
            <div class="section-header" style="margin-top: 4rem;">
                <h2 class="section-title">More News & Updates</h2>
            </div>
            
            <div class="grid grid-2" style="margin-top: 3rem;">
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 200px; background: linear-gradient(135deg, var(--red-pale), var(--red-light)); border-radius: 12px; margin-bottom: 1.5rem;"></div>
                    <div class="badge badge-outline" style="margin-bottom: 1rem;">Achievement</div>
                    <h3>YPSF Research Cited in UN Report</h3>
                    <p style="color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem;">Published on November 18, 2023</p>
                    <p>Our research on youth employment was cited in the latest UN Sustainable Development Goals progress report, highlighting the importance of youth-led research in global policy discussions.</p>
                    <a href="contact.html" class="btn btn-outline" style="margin-top: 1rem;">Read More</a>
                </div>
                
                <div class="card fade-in-scroll">
                    <div style="width: 100%; height: 200px; background: linear-gradient(135deg, var(--red-medium), var(--red-bright)); border-radius: 12px; margin-bottom: 1.5rem;"></div>
                    <div class="badge badge-outline" style="margin-bottom: 1rem;">Opportunity</div>
                    <h3>Call for Research Proposals</h3>
                    <p style="color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem;">Published on November 10, 2023</p>
                    <p>We're seeking research proposals from youth researchers on topics related to education access and employment opportunities. Selected proposals will receive funding and mentorship support.</p>
                    <a href="apply.html" class="btn btn-outline" style="margin-top: 1rem;">Submit Proposal</a>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 4rem;">
                <div class="card card-accent" style="max-width: 800px; margin: 0 auto; padding: 3rem;">
                    <h2 style="margin-bottom: 1rem;">Stay Connected</h2>
                    <p style="margin-bottom: 2rem; font-size: 1.1rem;">Follow us on social media and subscribe to our newsletter to never miss an update.</p>
                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn btn-primary">Subscribe to Newsletter</a>
                        <a href="https://www.linkedin.com/company/ypsf" target="_blank" class="btn btn-secondary">Follow on LinkedIn</a>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Write all pages
pages = [
    ('testimonials.html', 'Testimonials', 'Read testimonials from YPSF fellows, partners, and participants about their transformative experiences', testimonials),
    ('resources.html', 'Resources', 'Access YPSF publications, research reports, toolkits, case studies, and multimedia resources', resources),
    ('partners.html', 'Partners', 'Learn about YPSF partnerships and collaboration opportunities with organizations worldwide', partners),
    ('faq.html', 'FAQ', 'Frequently asked questions about YPSF programs, applications, and how to get involved', faq),
    ('events.html', 'Events', 'Upcoming workshops, webinars, conferences, and networking events from YPSF', events),
    ('news.html', 'News', 'Latest news, updates, publications, and achievements from YPSF', news),
]

for filename, title, desc, content in pages:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(create_page(title, desc, content, filename))
    print(f"✓ Created {filename}")

print("\n✅ All pages generated successfully!")

