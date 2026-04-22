import os
import re

def get_content(filepath, start_marker, end_marker):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        return content[start_idx:end_idx]
    return ''

os.chdir(r'c:\Users\baldy\Documents\Project\_Website_\GTI')

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

nav_regex = re.compile(r'<nav class="nav-menu">.*?</nav>', re.DOTALL)
new_nav = '''<nav class="nav-menu">
        <a href="#home" class="nav-link active" data-lang-id="Beranda" data-lang-en="Home">Beranda</a>
        <a href="#about" class="nav-link" data-lang-id="Tentang Kami" data-lang-en="About Us">Tentang Kami</a>
        <a href="#why-us" class="nav-link" data-lang-id="Mengapa Kami" data-lang-en="Why Choose Us">Mengapa Kami</a>
        <a href="#contact" class="nav-link" data-lang-id="Hubungi Kami" data-lang-en="Contact Us">Hubungi Kami</a>
      </nav>'''
idx_content = nav_regex.sub(new_nav, idx_content)

idx_content = idx_content.replace('<section class="hero-slider" id="heroSlider">', '<section class="hero-slider" id="home">')

footer_idx = idx_content.find('<!-- Footer -->')
head_and_body = idx_content[:footer_idx]
footer_and_tail = idx_content[footer_idx:]

about_content = get_content('about.html', '<!-- Page Title -->', '<!-- Footer -->')
why_us_content = get_content('why-us.html', '<!-- Page Title -->', '<!-- Footer -->')
contact_content = get_content('contact.html', '<!-- Page Title -->', '<!-- Footer -->')

final_html = head_and_body + '\n  <div id="about">\n' + about_content + '  </div>\n\n  <div id="why-us">\n' + why_us_content + '  </div>\n\n  <div id="contact">\n' + contact_content + '  </div>\n\n  ' + footer_and_tail

# Fix links in the footer as well!
footer_nav_regex = re.compile(r'<div class="footer-links">.*?</ul>', re.DOTALL)
new_footer_nav = '''<div class="footer-links">
          <h4 data-lang-id="Tautan Cepat" data-lang-en="Quick Links">Tautan Cepat</h4>
          <ul>
            <li><a href="#about" data-lang-id="Tentang Kami" data-lang-en="About Us">Tentang Kami</a></li>
            <li><a href="#why-us" data-lang-id="Mengapa Memilih Kami" data-lang-en="Why Choose Us">Mengapa Memilih Kami</a></li>
            <li><a href="#contact" data-lang-id="Kontak & Mitra" data-lang-en="Contact & Partnership">Kontak & Mitra</a></li>
          </ul>'''
final_html = footer_nav_regex.sub(new_footer_nav, final_html)

# Also fix the "Jelajahi Solusi Kami ->", "Hubungi Kami" etc links to use anchor links.
final_html = final_html.replace('href="contact.html"', 'href="#contact"')
final_html = final_html.replace('href="about.html"', 'href="#about"')
final_html = final_html.replace('href="why-us.html"', 'href="#why-us"')
final_html = final_html.replace('href="index.html"', 'href="#home"')

with open(r'GTI_1pages\index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Done')
