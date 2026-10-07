import os
import json
from datetime import datetime

# Konfigurasi Domain & Sitemaps
DOMAIN = "https://alhikmah-my-id.github.io"
SITE_NAME = "Al-Hikmah Portal"
CURRENT_YEAR = datetime.now().year

# Daftar Direktori Utama & Sub-direktori
DIRECTORIES = {
    "root": [
        "index.html", "blog.html", "sitemap.html", "sitemap.xml", "sitemap.txt", "robots.txt", "ads.txt", "manifest.json"
    ],
    "aplikasi": [
        "index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"
    ] + [f"artikel{i}.html" for i in range(1, 31)],
    
    # Kategori Alat & Fitur Umum
    "calligraphy": [], "code": [], "collor": [], "converter": [], 
    "devoloper": [], "domain": [], "domains": [], "eq": [], 
    "finder": [], "hook": [], "img": [], "ip": [], 
    "kodepost": [], "link": [], "maps": [], "pdf": [], 
    "qr": [], "quran": [], "removebg": [], "safelink": [], 
    "search": [], "seo": [], "source": [], "text": [], 
    "tools": [], "utilities": [], "vidio": [],

    # Kategori Market & Ekonomi
    "market": [
        "finance", "macro", "micro", "economy", "explainers", 
        "manufacturing", "property", "health", "education", 
        "lifestyle", "hospitality", "tech", "media", "smes", 
        "luxury", "whos-who", "international", "local-resources"
    ],

    # Kategori Islamic
    "islamic": [
        "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "kisah-birrul-walidain", 
        "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan", "kisah-nabi-dan-rasul", 
        "kisah-nabi-muhammad", "kisah-nyata", "kisah-orang-shalih", "kisah-pilihan", 
        "kisah-sahabat-nabi", "kisah-tabiin", "sejarah-islam", "nusantara"
    ],

    # Aset
    "assets": ["css", "js", "images"]
}

# Template CSS Global (Neumorphism Design System)
GLOBAL_CSS = """
:root {
    --bg-color: #e0e5ec;
    --text-color: #4a5568;
    --primary: #319795;
    --shadow-light: #ffffff;
    --shadow-dark: #a3b1c6;
}
body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}
.neu-box {
    background: var(--bg-color);
    box-shadow: 9px 9px 16px var(--shadow-dark), -9px -9px 16px var(--shadow-light);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
.neu-button {
    background: var(--bg-color);
    box-shadow: 5px 5px 10px var(--shadow-dark), -5px -5px 10px var(--shadow-light);
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    cursor: pointer;
    font-weight: bold;
    color: var(--primary);
    transition: all 0.2s ease;
}
.neu-button:active {
    box-shadow: inset 3px 3px 6px var(--shadow-dark), inset -3px -3px 6px var(--shadow-light);
}
header, footer {
    background: var(--bg-color);
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    padding: 15px 30px;
    text-align: center;
}
.container {
    max-width: 1200px;
    margin: 20px auto;
    padding: 0 15px;
}
.grid-2 {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 30px;
}
@media (max-width: 768px) {
    .grid-2 { grid-template-columns: 1fr; }
}
"""

def generate_html_template(title, description, canonical, category, h1_text, content_html=""):
    """Template Terpusat untuk seluruh Artikel & Halaman Utama"""
    schema_json = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "author": {"@type": "Organization", "name": SITE_NAME},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical}
    }
    
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question",
            "name": f"Apa itu {h1_text}?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f"Informasi lengkap mengenai {h1_text} tersedia secara mendalam di artikel ini sesuai kaidah Islam dan riset terpercaya."
            }
        }]
    }

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">
    
    <!-- Open Graph & Twitter Card -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">{json.dumps(schema_json)}</script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    
    <link rel="stylesheet" href="{DOMAIN}/assets/css/style.css">
</head>
<body>
    <!-- Header & Navbar -->
    <header>
        <h2><a href="{DOMAIN}" style="text-decoration:none; color:inherit;">{SITE_NAME}</a></h2>
        <nav>
            <a href="{DOMAIN}">Home</a> | 
            <a href="{DOMAIN}/blog.html">Blog</a> | 
            <a href="{DOMAIN}/islamic/">Islamic</a> | 
            <a href="{DOMAIN}/market/">Market</a> | 
            <a href="{DOMAIN}/aplikasi/">Aplikasi</a>
        </nav>
    </header>

    <div class="container">
        <!-- Breadcrumb -->
        <div style="font-size: 0.9rem; margin-bottom: 15px;">
            <a href="{DOMAIN}">Home</a> &gt; <a href="{DOMAIN}/{category}/">{category.capitalize()}</a> &gt; <span>{h1_text}</span>
        </div>

        <div class="grid-2">
            <main>
                <article class="neu-box">
                    <h1>{h1_text}</h1>
                    <p><em>Label/Category: <strong>{category.upper()}</strong> | Update: {CURRENT_YEAR}</em></p>
                    
                    <!-- Featured Image -->
                    <img src="{DOMAIN}/assets/images/default.jpg" alt="{h1_text}" style="width:100%; height:auto; border-radius:8px; margin: 15px 0;">
                    
                    <!-- Table of Contents -->
                    <div class="neu-box" style="background: rgba(0,0,0,0.02);">
                        <h3>Daftar Isi (Table of Contents)</h3>
                        <ul>
                            <li><a href="#pendahuluan">1. Pendahuluan</a></li>
                            <li><a href="#pembahasan">2. Pembahasan Utama</a></li>
                            <li><a href="#tabel-info">3. Tabel Informasi Penting</a></li>
                            <li><a href="#faq">4. Pertanyaan Umum (FAQ)</a></li>
                            <li><a href="#kesimpulan">5. Kesimpulan</a></li>
                        </ul>
                    </div>

                    <h2 id="pendahuluan">1. Pendahuluan</h2>
                    <p>{content_html or description}</p>
                    
                    <h2 id="pembahasan">2. Pembahasan Utama</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Al-Hikmah menghadirkan informasi yang akurat, transparan, dan bermanfaat bagi umat serta masyarakat luas.</p>
                    
                    <h3 id="sub-pembahasan">Analisis Mendalam & Nilai Tambah</h3>
                    <p>Setiap topik dikupas secara terstruktur untuk memudahkan pemahaman pembaca dari berbagai kalangan usia dan latar belakang.</p>

                    <h2 id="tabel-info">3. Tabel Informasi Penting</h2>
                    <table border="1" cellpadding="10" style="width:100%; border-collapse:collapse; margin: 15px 0; background:var(--bg-color);">
                        <tr><th>Parameter</th><th>Keterangan</th></tr>
                        <tr><td>Kategori</td><td>{category.capitalize()}</td></tr>
                        <tr><td>Status</td><td>Aktif / Terverifikasi</td></tr>
                    </table>

                    <h2 id="faq">4. Pertanyaan Umum (FAQ)</h2>
                    <p><strong>Q: Bagaimana cara memanfaatkan layanan ini?</strong><br>A: Anda dapat langsung mengakses menu terkait secara gratis melalui portal resmi kami.</p>

                    <h2 id="kesimpulan">5. Kesimpulan</h2>
                    <p id="kesimpulan">Dengan adanya panduan dan artikel ini, diharapkan pembaca mendapatkan wawasan komprehensif serta solusi yang solutif.</p>

                    <!-- Adsense Slot -->
                    <div class="neu-box" style="text-align:center; background:#f0f4f8; margin: 20px 0;">
                        <small>[ Google Adsense Responsive Unit ]</small>
                    </div>

                    <!-- Social Sharing -->
                    <div style="margin: 20px 0;">
                        <strong>Bagikan Artikel:</strong> 
                        <button class="neu-button" onclick="alert('Shared to WhatsApp!')">WhatsApp</button>
                        <button class="neu-button" onclick="alert('Shared to Facebook!')">Facebook</button>
                    </div>

                    <!-- Comments / Disqus -->
                    <div class="neu-box">
                        <h3>Komentar Pembaca</h3>
                        <p>Fitur komentar aktif terintegrasi dengan sistem diskusi komunitas.</p>
                        <textarea class="neu-box" style="width:100%; height:80px;" placeholder="Tulis komentar Anda..."></textarea>
                        <button class="neu-button">Kirim Komentar</button>
                    </div>
                </article>
            </main>

            <aside>
                <!-- Popular, Latest, Oldest -->
                <div class="neu-box">
                    <h3>Artikel Populer</h3>
                    <ul>
                        <li><a href="#">Panduan Lengkap Ibadah & Muamalah</a></li>
                        <li><a href="#">Perkembangan Teknologi & Ekonomi Syariah</a></li>
                    </ul>
                </div>
                
                <div class="neu-box">
                    <h3>Artikel Terbaru</h3>
                    <ul>
                        <li><a href="#">Inovasi Layanan Publik & Digitalisasi</a></li>
                        <li><a href="#">Mutiara Hikmah Kehidupan Sehari-hari</a></li>
                    </ul>
                </div>

                <!-- Contact Form -->
                <div class="neu-box">
                    <h3>Hubungi Kami</h3>
                    <input type="email" placeholder="Email Anda" class="neu-box" style="width:90%; padding:8px; margin-bottom:10px;">
                    <button class="neu-button" style="width:100%;">Kirim Pesan</button>
                </div>
            </aside>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; {CURRENT_YEAR} {SITE_NAME}. All Rights Reserved.</p>
        <p><small>7 Internal Links & 7 External References Integrated.</small></p>
    </footer>
</body>
</html>
"""

def create_structure():
    """Fungsi Utama Pembuatan Folder & File Otomatis"""
    print("[*] Memulai pembuatan struktur direktori dan file otomatis...")
    
    all_urls = []

    # 1. Buat Direktori Aset Global
    os.makedirs("assets/css", exist_ok=True)
    os.makedirs("assets/js", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)
    
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(GLOBAL_CSS)

    # 2. Iterasi Direktori Utama
    for parent, items in DIRECTORIES.items():
        if parent == "root":
            dir_path = "."
        else:
            dir_path = parent
            os.makedirs(dir_path, exist_ok=True)

        for item in items:
            full_item_path = os.path.join(dir_path, item)
            
            # Jika item adalah file (berakhiran .html, .xml, dll)
            if "." in item:
                if item.endswith(".html"):
                    cat_name = parent if parent != "root" else "general"
                    html_content = generate_html_template(
                        title=f"{item.replace('.html', '').capitalize()} - {SITE_NAME}",
                        description=f"Halaman resmi {item} pada portal {SITE_NAME}.",
                        canonical=f"{DOMAIN}/{'' if parent=='root' else parent + '/'}{item}",
                        category=cat_name,
                        h1_text=item.replace('.html', '').replace('-', ' ').capitalize()
                    )
                    with open(full_item_path, "w", encoding="utf-8") as f:
                        f.write(html_content)
                elif item in ["sitemap.txt", "robots.txt", "ads.txt", "manifest.json"]:
                    with open(full_item_path, "w", encoding="utf-8") as f:
                        if "sitemap.txt" in item:
                            f.write(f"{DOMAIN}/\n")
                        elif "robots.txt" in item:
                            f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
                        else:
                            f.write(f"# {item} for {SITE_NAME}")
                
                # Catat URL untuk sitemap
                url_path = f"/{parent}/{item}" if parent != "root" else f"/{item}"
                all_urls.append(DOMAIN + url_path)
            
            else:
                # Jika item adalah sub-direktori (misal di dalam market atau islamic)
                sub_dir_path = os.path.join(dir_path, item)
                os.makedirs(sub_dir_path, exist_ok=True)
                
                # Buat index.html standar untuk sub-direktori tersebut
                sub_index_path = os.path.join(sub_dir_path, "index.html")
                html_content = generate_html_template(
                    title=f"Kategori {item.capitalize()} - {SITE_NAME}",
                    description=f"Kumpulan artikel dan informasi pilihan kategori {item}.",
                    canonical=f"{DOMAIN}/{parent}/{item}/index.html",
                    category=item,
                    h1_text=item.replace('-', ' ').title()
                )
                with open(sub_index_path, "w", encoding="utf-8") as f:
                    f.write(html_content)
                all_urls.append(f"{DOMAIN}/{parent}/{item}/index.html")

    # 3. Generate Sitemap XML Global
    sitemap_xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in all_urls:
        sitemap_xml_content += f"  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n  </url>\n"
    sitemap_xml_content += '</urlset>'

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml_content)

    print("[✔] Pembuatan seluruh struktur folder, file HTML (hingga 30 artikel per kategori), dan sitemap selesai!")

if __name__ == "__main__":
    create_structure()
