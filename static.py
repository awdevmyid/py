import os
import json
from datetime import datetime

# Konfigurasi Domain & Sifat Dasar
DOMAIN = "https://awdev.eu.org"
SITE_NAME = "Awdev Platform"
CURRENT_YEAR = datetime.now().year

# Daftar direktori utama & sub-direktori sesuai struktur Anda
DIRECTORIES = {
    "root": [
        "index.html", "blog.html", "sitemap.html", "sitemap.xml", "sitemap.txt",
        "robots.txt", "ads.txt", "manifest.json"
    ],
    "aplikasi": [
        "index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"
    ] + [f"artikel{i}.html" for i in range(1, 31)],
    
    "kategori_utama": [
        "calligraphy", "code", "collor", "converter", "devoloper", "domain", "domains",
        "eq", "finder", "hook", "img", "ip", "kodepost", "link", "maps", "pdf",
        "qr", "quran", "removebg", "safelink", "search", "seo", "source", "text",
        "tools", "utilities", "vidio"
    ],
    
    "market": [
        "finance", "macro", "micro", "economy", "explainers", "manufacturing",
        "property", "health", "education", "lifestyle", "hospitality", "tech",
        "media", "smes", "luxury", "whos-who", "international", "local-resources"
    ],
    
    "islamic": [
        "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "kisah-birrul-walidain",
        "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan",
        "kisah-nabi-dan-rasul", "kisah-nabi-muhammad", "kisah-nyata",
        "kisah-orang-shalih", "kisah-pilihan", "kisah-sahabat-nabi",
        "kisah-tabiin", "sejarah-islam", "nusantara"
    ],
    
    "assets": [
        "assets/css", "assets/js", "assets/images"
    ]
}

# Template CSS Terpusat (Neumorphism Design System)
BASE_CSS = """
:root {
    --bg-color: #e0e5ec;
    --text-color: #4a5568;
    --primary: #3182ce;
    --shadow-light: #ffffff;
    --shadow-dark: #a3b1c6;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
body { background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; padding-bottom: 50px; }
header, footer { background: var(--bg-color); padding: 20px; text-align: center; box-shadow: 8px 8px 16px var(--shadow-dark), -8px -8px 16px var(--shadow-light); margin-bottom: 20px; }
nav a { margin: 0 10px; text-decoration: none; color: var(--primary); font-weight: 600; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.neu-card { background: var(--bg-color); border-radius: 15px; padding: 25px; box-shadow: 9px 9px 16px var(--shadow-dark), -9px -9px 16px var(--shadow-light); margin-bottom: 25px; }
.neu-button { border: none; outline: none; background: var(--bg-color); padding: 10px 20px; border-radius: 10px; box-shadow: 5px 5px 10px var(--shadow-dark), -5px -5px 10px var(--shadow-light); cursor: pointer; color: var(--primary); font-weight: bold; transition: 0.2s; }
.neu-button:active { box-shadow: inset 3px 3px 6px var(--shadow-dark), inset -3px -3px 6px var(--shadow-light); }
h1, h2, h3 { color: #2d3748; margin-bottom: 15px; }
p { margin-bottom: 15px; }
.toc, .info-table, .faq-section { background: var(--bg-color); border-radius: 12px; padding: 20px; box-shadow: inset 4px 4px 8px var(--shadow-dark), inset -4px -4px 8px var(--shadow-light); margin: 20px 0; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px; border-bottom: 1px solid #cbd5e0; text-align: left; }
"""

# Template HTML Utama / Artikel dengan SEO, Adsense, Schema, dll.
def get_article_template(title, description, canonical, url_path):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{DOMAIN}/{url_path}">
    
    <!-- Open Graph / Social Sharing -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{DOMAIN}/{url_path}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{DOMAIN}/assets/images/featured.jpg">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{DOMAIN}/assets/images/featured.jpg">
    
    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXX" crossorigin="anonymous"></script>
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{description}",
      "image": "{DOMAIN}/assets/images/featured.jpg",
      "author": {{ "@type": "Organization", "name": "{SITE_NAME}" }},
      "publisher": {{ "@type": "Organization", "name": "{SITE_NAME}", "logo": {{ "@type": "ImageObject", "url": "{DOMAIN}/assets/images/logo.png" }} }},
      "mainEntityOfPage": "{DOMAIN}/{url_path}"
    }}
    </script>
    
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>{SITE_NAME}</h1>
            <nav>
                <a href="/">Home</a>
                <a href="/blog.html">Blog</a>
                <a href="/aplikasi/">Aplikasi</a>
                <a href="/islamic/sejarah-islam/">Islamic</a>
                <a href="/tools/">Tools</a>
            </nav>
        </div>
    </header>

    <main class="container">
        <!-- Breadcrumb -->
        <nav style="font-size: 0.9rem; margin-bottom: 15px;">
            <a href="/">Home</a> &gt; <a href="/blog.html">Artikel</a> &gt; <span>{title}</span>
        </nav>

        <article class="neu-card">
            <h1>{title}</h1>
            <p><em>Dipublikasikan oleh Tim Redaksi {SITE_NAME} | Kategori: Umum</em></p>
            
            <div style="margin: 20px 0;">
                <img src="/assets/images/featured.jpg" alt="{title}" style="width: 100%; height: auto; border-radius: 10px;">
            </div>

            <!-- Table of Contents -->
            <div class="toc">
                <h3>Daftar Isi</h3>
                <ul>
                    <li><a href="#pendahuluan">1. Pendahuluan</a></li>
                    <li><a href="#informasi-utama">2. Informasi Utama & Analisis</a></li>
                    <li><a href="#faq">3. Pertanyaan Umum (FAQ)</a></li>
                    <li><a href="#kesimpulan">4. Kesimpulan</a></li>
                </ul>
            </div>

            <h2 id="pendahuluan">1. Pendahuluan</h2>
            <p>Selamat datang di pembahasaan mendalam mengenai {title}. Artikel ini dirancang khusus untuk memberikan panduan komprehensif, informasi akurat, serta solusi terbaik yang relevan dengan kebutuhan Anda saat ini.</p>
            
            <!-- Adsense Slot -->
            <div style="margin: 20px 0; text-align: center;">
                <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-XXXXXXXXX" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
                <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
            </div>

            <h2 id="informasi-utama">2. Informasi Utama & Analisis</h2>
            <p>Berikut adalah tabel informasi penting yang merangkum poin-poin utama dari topik ini:</p>
            
            <div class="info-table">
                <table>
                    <tr><th>Parameter</th><th>Detail Keterangan</th></tr>
                    <tr><td>Topik Utama</td><td>{title}</td></tr>
                    <tr><td>Platform</td><td>Awdev Ecosystem</td></tr>
                    <tr><td>Pembaruan</td><td>{CURRENT_YEAR}</td></tr>
                </table>
            </div>

            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

            <h2 id="faq">3. Pertanyaan Umum (FAQ)</h2>
            <div class="faq-section">
                <h3>Apa itu {title}?</h3>
                <p>{title} adalah solusi optimal yang disediakan melalui platform {SITE_NAME} untuk mempermudah pekerjaan Anda.</p>
                <h3>Bagaimana cara menggunakannya?</h3>
                <p>Anda dapat mengikuti panduan langkah demi langkah yang tersedia di dalam artikel atau memanfaatkan tools terkait.</p>
            </div>

            <h2 id="kesimpulan">4. Kesimpulan</h2>
            <p id="kesimpulan">Dengan memahami {title}, Anda dapat meningkatkan efisiensi dan produktivitas secara signifikan. Jangan lupa untuk membagikan artikel ini kepada rekan atau kolega Anda.</p>
        </article>

        <!-- Social Sharing & Widgets -->
        <div class="neu-card">
            <h3>Bagikan Artikel Ini</h3>
            <button class="neu-button" onclick="alert('Link disalin!')">Bagikan ke Facebook</button>
            <button class="neu-button" onclick="alert('Link disalin!')">Bagikan ke Twitter</button>
            <button class="neu-button" onclick="alert('Link disalin!')">Bagikan ke WhatsApp</button>
        </div>

        <!-- Internal Links & Archive -->
        <div class="neu-card">
            <h3>Artikel Populer & Terkait</h3>
            <ul>
                <li><a href="/aplikasi/artikel1.html">7 Internal Link Penting untuk SEO On-Page</a></li>
                <li><a href="/aplikasi/artikel2.html">Optimasi Kecepatan Website Statis Modern</a></li>
                <li><a href="/aplikasi/artikel3.html">Panduan Lengkap Menggunakan Neumorphism CSS</a></li>
                <li><a href="/aplikasi/artikel4.html">Integrasi Google AdSense pada Web Statis</a></li>
                <li><a href="/aplikasi/artikel5.html">Membuat Peta Situs XML Otomatis</a></li>
                <li><a href="/aplikasi/artikel6.html">Strategi Konten Market dan Finansial</a></li>
                <li><a href="/aplikasi/artikel7.html">Arsitektur Direktori Website yang Ramah SEO</a></li>
            </ul>
        </div>

        <!-- External References -->
        <div class="neu-card">
            <h3>Referensi Eksternal</h3>
            <ul>
                <li><a href="https://developer.mozilla.org" target="_blank" rel="nofollow">MDN Web Docs</a></li>
                <li><a href="https://schema.org" target="_blank" rel="nofollow">Schema.org Specifications</a></li>
                <li><a href="https://developers.google.com/search" target="_blank" rel="nofollow">Google Search Central</a></li>
                <li><a href="https://w3.org" target="_blank" rel="nofollow">W3C Web Standards</a></li>
                <li><a href="https://github.com" target="_blank" rel="nofollow">GitHub Open Source Repositories</a></li>
                <li><a href="https://stackoverflow.com" target="_blank" rel="nofollow">Stack Overflow Community</a></li>
                <li><a href="https://caniuse.com" target="_blank" rel="nofollow">Can I Use Support Tables</a></li>
            </ul>
        </div>

        <!-- Contact Form -->
        <div class="neu-card">
            <h3>Hubungi Kami</h3>
            <form onsubmit="event.preventDefault(); alert('Pesan berhasil terkirim!');">
                <p><input type="text" placeholder="Nama Anda" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e0; background:var(--bg-color);" required></p>
                <p><input type="email" placeholder="Email Anda" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e0; background:var(--bg-color);" required></p>
                <p><textarea placeholder="Pesan atau Komentar..." rows="4" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e0; background:var(--bg-color);" required></textarea></p>
                <button type="submit" class="neu-button">Kirim Pesan</button>
            </form>
        </div>

        <!-- Disqus / Comment Section -->
        <div class="neu-card">
            <h3>Komentar</h3>
            <div id="disqus_thread"></div>
            <script>
                var disqus_config = function () {{
                    this.page.url = '{DOMAIN}/{url_path}';
                    this.page.identifier = '{url_path}';
                }};
                (function() {{
                    var d = document.createElement('script'); d.src = 'https://awdev.disqus.com/embed.js';
                    d.setAttribute('data-timestamp', +new Date());
                    (document.head || document.body).appendChild(d);
                }})();
            </script>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; {CURRENT_YEAR} {SITE_NAME} - All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

def generate_structure():
    print("Mulai membuat struktur direktori dan file untuk awdev.eu.org...")

    # 1. Buat direktori dasar CSS di assets
    os.makedirs("assets/css", exist_ok=True)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(BASE_CSS)

    # 2. Buat file Root
    for filename in DIRECTORIES["root"]:
        filepath = filename
        if filename.endswith(".html"):
            content = get_article_template(
                f"Halaman Utama {filename.split('.')[0].upper()}",
                "Pusat informasi, tools, dan artikel terbaik di awdev.eu.org",
                filename,
                filename
            )
        elif filename == "sitemap.xml":
            content = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{DOMAIN}/</loc></url>\n</urlset>'
        elif filename == "robots.txt":
            content = f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml"
        elif filename == "ads.txt":
            content = "google.com, pub-XXXXXXXXX, DIRECT, f08c47fec0942fa0"
        elif filename == "manifest.json":
            content = json.dumps({"name": SITE_NAME, "short_name": "Awdev", "start_url": "/", "display": "standalone"}, indent=4)
        else:
            content = f"Konten untuk {filename}"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # 3. Buat direktori Aplikasi & 30 Artikel
    os.makedirs("aplikasi", exist_ok=True)
    for filename in DIRECTORIES["aplikasi"]:
        filepath = os.path.join("aplikasi", filename)
        if filename.endswith(".html"):
            title = "Aplikasi dan Panduan Lengkap" if filename == "index.html" else f"Artikel Aplikasi Bagian {filename.replace('artikel','').replace('.html','')}"
            content = get_article_template(title, f"Pembahasan mendalam seputar {title} di {SITE_NAME}", f"aplikasi/{filename}", f"aplikasi/{filename}")
        else:
            content = f"Sitemap aplikasi {filename}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # 4. Buat kategori utama, market, dan islamic
    all_categories = DIRECTORIES["kategori_utama"] + DIRECTORIES["market"] + DIRECTORIES["islamic"]
    
    for cat in all_categories:
        # Tentukan parent folder
        if cat in DIRECTORIES["market"]:
            dir_path = os.path.join("market", cat)
        elif cat in DIRECTORIES["islamic"]:
            dir_path = os.path.join("islamic", cat)
        else:
            dir_path = cat
            
        os.makedirs(dir_path, exist_ok=True)
        
        # Buat index.html dan beberapa file pendukung di setiap kategori
        for subfile in ["index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"]:
            filepath = os.path.join(dir_path, subfile)
            if subfile.endswith(".html"):
                title = f"Kategori {cat.replace('-', ' ').title()}"
                content = get_article_template(title, f"Kumpulan artikel dan informasi terkait {cat} di {SITE_NAME}", f"{dir_path}/{subfile}", f"{dir_path}/{subfile}")
            else:
                content = f"Sitemap {cat}"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

    print("Struktur website awdev.eu.org berhasil dibuat secara otomatis!")

if __name__ == "__main__":
    generate_structure()
