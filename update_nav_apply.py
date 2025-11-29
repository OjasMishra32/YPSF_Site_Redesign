#!/usr/bin/env python3
"""
Update navigation on all pages to make Apply button stand out
"""

import re

files = ['testimonials.html', 'resources.html', 'partners.html', 'faq.html', 'events.html', 'news.html', 'apply.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add Apply button styling if not present
    if '.nav-apply-btn' not in content:
        apply_btn_css = '''
        /* Make Apply button stand out in navbar */
        .nav-apply-btn {
            background: rgba(255, 255, 255, 0.25) !important;
            border: 2px solid rgba(255, 255, 255, 0.5) !important;
            border-radius: var(--radius-md) !important;
            padding: var(--spacing-xs) var(--spacing-md) !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
            transition: all var(--transition-base) !important;
        }
        
        .nav-apply-btn:hover {
            background: rgba(255, 255, 255, 0.35) !important;
            border-color: rgba(255, 255, 255, 0.8) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
        }
        
        .nav-apply-btn.active {
            background: rgba(255, 255, 255, 0.3) !important;
            border-color: white !important;
        }
        '''
        # Insert before </style>
        content = re.sub(
            r'(</style>)',
            apply_btn_css + r'\1',
            content
        )
    
    # Update navigation - find Apply link and add nav-apply-btn class
    content = re.sub(
        r'<a href="[^"]*apply[^"]*"[^>]*>Apply</a>',
        '<a href="apply.html" class="nav-apply-btn">Apply</a>',
        content
    )
    
    # Update all #apply links to apply.html
    content = re.sub(r'href="#apply"', 'href="apply.html"', content)
    content = re.sub(r'href="index\.html#apply"', 'href="apply.html"', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ Updated {filename}')

print('✅ All pages updated!')

