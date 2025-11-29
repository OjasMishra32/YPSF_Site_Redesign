#!/usr/bin/env python3
import re

files = ['testimonials.html', 'resources.html', 'partners.html', 'faq.html', 'events.html', 'news.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update logo CSS
    content = re.sub(
        r'\.logo \{[^}]*\}',
        '''.logo {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            color: white;
            text-decoration: none;
            transition: transform var(--transition-base);
            gap: 0.25rem;
        }''',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'\.logo:hover \{[^}]*\}',
        '''.logo:hover {
            transform: scale(1.02);
        }''',
        content,
        flags=re.DOTALL
    )
    
    # Remove old logo-image and logo-text styles
    content = re.sub(r'\.logo-image \{[^}]*\}', '', content)
    content = re.sub(r'\.logo-text \{[^}]*\}', '', content)
    
    # Add new logo styles after .logo:hover
    if '.logo-acronym' not in content:
        logo_styles = '''
        .logo-acronym {
            font-family: 'Inter', sans-serif;
            font-weight: 900;
            font-size: 2rem;
            letter-spacing: -0.05em;
            color: #e04a59;
            text-shadow: 
                2px 2px 0px #7a0e23,
                1px 1px 0px #7a0e23,
                0px 0px 0px #7a0e23;
            line-height: 1;
            margin: 0;
        }
        
        .logo-full-name {
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            font-weight: 400;
            color: white;
            line-height: 1.2;
            margin: 0;
            white-space: nowrap;
        }
        '''
        # Insert after .logo:hover
        content = re.sub(
            r'(\.logo:hover \{[^}]*\})',
            r'\1' + logo_styles,
            content,
            flags=re.DOTALL
        )
    
    # Update logo HTML - handle both href="index.html" and href="#home"
    content = re.sub(
        r'<a href="[^"]*" class="logo">\s*<img[^>]*>\s*<span[^>]*>YPSF</span>\s*</a>',
        '''<a href="index.html" class="logo">
                <div class="logo-acronym">YPSF</div>
                <div class="logo-full-name">Youth Publications &<br>Socioeconomic Forum</div>
            </a>''',
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ Updated {filename}')

print('✅ All pages updated!')

