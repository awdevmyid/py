import os
import json
from datetime import datetime

# Konfigurasi Utama
DOMAIN = "https://alhikmah.eu.org"
SITE_NAME = "Al-Hikmah Portal"
CURRENT_YEAR = datetime.now().year

# Daftar Kategori Utama & Sub-kategori
STRUCTURE = {
    "root_files": [
        "index.html", "blog.html", "sitemap.html", "sitemap.xml", 
        "sitemap.txt", "robots.txt", "ads.txt", "manifest.json"
    ],
    "sub_categories": [
        "calligraphy", "code", "collor", "converter", "devoloper", 
        "domain", "domains", "eq", "finder", "hook", "img", "ip", 
        "kodepost", "link", "maps", "pdf", "qr", "quran", "removebg", 
        "safelink", "search", "seo", "source", "text", "tools", 
        "utilities", "vidio"
    ],
    "market": [
        "finance", "macro", "micro", "economy", "explainers", 
        "manufacturing", "property", "health", "education", "lifestyle", 
        "hospitality", "tech", "media", "smes", "luxury", "whos-who", 
        "international", "local-resources"
    ],
    "islamic": [
        "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "kisah-birrul-walidain", 
        "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan", 
        "kisah-nabi-dan-rasul", "kisah-nabi-muhammad", "kisah-nyata", 
        "kisah-orang-shalih", "kisah-pilihan", "kisah-sahabat-nabi", 
        "kisah-tabiin", "sejarah-islam", "nusantara"
    ],
    "assets": ["assets/css", "assets/js", "assets/images"]
}

# Template CSS Terpusat (Neumorphism Design System)
MAIN_CSS = """
:root {
    --bg-color: #e0e5ec;
    --text-color: #4a5568;
    --primary-color: #3182ce;
    --shadow-light: #ffffff;
    --shadow-dark: #a3b1c6;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
body { background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; padding: 20px; }
.neu-card {
    background: var(--bg-color);
    box-shadow: 9px 9px 16px var(--shadow-dark), -9px -9px 16px var(--shadow-light);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
}
.neu-input {
    border: none;
    outline: none;
    background: var(--bg-color);
    box-shadow: inset 4px 4px 8px var(--shadow-dark), inset -4px -4px 8px var(--shadow-light);
    padding: 12px 20px;
    border-radius: 10px;
    width: 100%;
    margin-bottom: 15px;
}
.neu-btn {
    border: none;
    outline: none;
    background: var(--bg-color);
    box-shadow: 6px 6px 12px var(--shadow-dark), -6px -6px 12px var(--shadow-light);
    padding: 10px 20px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    color: var(--primary-color);
    transition: all 0.2s ease;
}
.neu-btn:active {
    box-shadow: inset 4px 4px 8px var(--shadow-dark), inset -4px -4px 8px var(--shadow-light);
}
header, footer { text-align: center; padding: 20px; }
nav a { margin: 0 10px; text-decoration: none; color: var(--text-color); font-weight: 600; }
.container { max-width: 1200px; margin: 0 auto; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
table, th, td { border: 1px solid var(--shadow-dark); padding: 10px; text-align: left; }
.toc { background: rgba(0,0,0,0.02); padding: 15px; border-radius: 10px; margin-bottom: 20px; }
"""

def get_base_html(title, description, canonical, content, category=""):
    """Template Terpusat untuk seluruh halaman artikel dan statis"""
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">
    
    <!-- Open Graph / Social Sharing -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{DOMAIN}/assets/images/featured.jpg">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{description}",
      "author": {{ "@type": "Organization", "name": "{SITE_NAME}" }},
      "publisher": {{ "@type": "Organization", "name": "{SITE_NAME}" }}
    }}
    </script>
    
    <link rel="stylesheet" href="{DOMAIN}/assets/css/style.css">
</head>
<body>
    <div class="container">
        <!-- Header & Navbar Terpusat -->
        <header class="neu-card">
            <h1>{SITE_NAME}</h1>
            <nav>
                <a href="{DOMAIN}/index.html">Home</a>
                <a href="{DOMAIN}/blog.html">Blog</a>
                <a href="{DOMAIN}/islamic/biografi-ulama/index.html">Islamic</a>
                <a href="{DOMAIN}/market/finance/index.html">Market</a>
                <a href="{DOMAIN}/sitemap.html">Sitemap</a>
            </nav>
        </header>

        <!-- Main Content -->
        <main>
            {content}
        </main>

        <!-- Footer Terpusat -->
        <footer class="neu-card">
            <p>&copy; {CURRENT_YEAR} {SITE_NAME}. All rights reserved.</p>
        </footer>
    </div>
    
    <script src="{DOMAIN}/assets/js/main.js"></script>
</body>
</html>
"""

def create_directory_structure():
    print("🚀 Memulai pembuatan struktur direktori dan file...")
    
    # 1. Buat direktori utama dan aset
    os.makedirs("assets/css", exist_ok=True)
    os.makedirs("assets/js", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)
    
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(MAIN_CSS)
        
    with open("assets/js/main.js", "w", encoding="utf-8") as f:
        f.write("// Logika Global & Islamic Tools Client-Side\nconsole.log('System Initialized.');")

    # 2. Generate Root Files
    for file in STRUCTURE["root_files"]:
        if file.endswith(".html"):
            title = f"Beranda - {SITE_NAME}" if file == "index.html" else f"{file.split('.')[0].capitalize()} - {SITE_NAME}"
            content = f"""
            <div class="neu-card">
                <h2>Selamat Datang di {file.split('.')[0].capitalize()}</h2>
                <p>Halaman pusat informasi dan direktori layanan dari {DOMAIN}.</p>
            </div>
            """
            html = get_base_html(title, "Portal informasi terlengkap dan terpercaya.", f"{DOMAIN}/{file}", content)
            with open(file, "w", encoding="utf-8") as f:
                f.write(html)
        elif file == "robots.txt":
            with open(file, "w", encoding="utf-8") as f:
                f.write(f"User-agent: *\nDisallow:\nSitemap: {DOMAIN}/sitemap.xml")
        elif file == "ads.txt":
            with open(file, "w", encoding="utf-8") as f:
                f.write("google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0")
        elif file == "manifest.json":
            manifest = {"name": SITE_NAME, "short_name": "Al-Hikmah", "start_url": "/index.html", "display": "standalone"}
            with open(file, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=4)

    # 3. Generate Kategori Umum & Sub-kategori
    all_categories = STRUCTURE["sub_categories"] + [f"market/{sub}" for sub in STRUCTURE["market"]] + [f"islamic/{sub}" for sub in STRUCTURE["islamic"]]
    
    for cat in all_categories:
        os.makedirs(cat, exist_ok=True)
        
        # Buat Index Kategori & Sitemap Kategori
        for page in ["index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"]:
            if page == "index.html":
                content = f"""
                <div class="neu-card">
                    <h2>Kategori: {cat.upper()}</h2>
                    <p>Daftar artikel pilihan dalam kategori {cat}. Temukan pembahasan mendalam di bawah ini.</p>
                    <ul>
                        {"".join([f'<li><a href="artikel{i}.html">Artikel Pembahasan Lengkap {i} - {cat.capitalize()}</a></li>' for i in range(1, 11)])}
                    </ul>
                </div>
                """
                html = get_base_html(f"Kategori {cat} - {SITE_NAME}", f"Kumpulan artikel terbaik seputar {cat}.", f"{DOMAIN}/{cat}/index.html", content)
                with open(os.path.join(cat, page), "w", encoding="utf-8") as f:
                    f.write(html)
            else:
                with open(os.path.join(cat, page), "w", encoding="utf-8") as f:
                    f.write(f"Sitemap untuk kategori {cat}")

        # Buat 30 Artikel per Kategori
        for i in range(1, 31):
            art_name = f"artikel{i}.html"
            title = f"Judul Artikel SEO Utama {i} untuk {cat.replace('/', ' - ')}"
            desc = f"Ringkasan eksklusif artikel ke-{i} membahas tuntas informasi terkait {cat} secara mendalam."
            canonical = f"{DOMAIN}/{cat}/{art_name}"
            
            content = f"""
            <article class="neu-card">
                <nav class="breadcrumb"><a href="{DOMAIN}/index.html">Home</a> &gt; <a href="{DOMAIN}/{cat}/index.html">{cat}</a> &gt; <span>{art_name}</span></nav>
                <h1>{title}</h1>
                <p><em>Dipublikasikan oleh Tim Redaksi {SITE_NAME}</em></p>
                
                <div class="toc">
                    <h3>Daftar Isi</h3>
                    <ul>
                        <li><a href="#pendahuluan">1. Pendahuluan</a></li>
                        <li><a href="#pembahasan">2. Pembahasan Utama</a></li>
                        <li><a href="#faq">3. Tanya Jawab (FAQ)</a></li>
                        <li><a href="#kesimpulan">4. Kesimpulan</a></li>
                    </ul>
                </div>

                <div class="featured-image neu-card" style="text-align: center; padding: 10px;">
                    <img src="{DOMAIN}/assets/images/featured.jpg" alt="Ilustrasi terkait {title}" style="max-width: 100%; height: auto; border-radius: 10px;">
                </div>

                <section id="pendahuluan">
                    <h2>1. Pendahuluan</h2>
                    <p>Paragraf pembuka artikel panjang yang mengulas latar belakang, urgensi, serta poin-poin krusial yang akan dibahas secara komprehensif.</p>
                </section>

                <section id="pembahasan">
                    <h2>2. Pembahasan Utama</h2>
                    <p>Uraian mendalam yang memuat analisis, data pendukung, serta referensi terpercaya guna memberikan wawasan maksimal bagi pembaca setia.</p>
                    
                    <table>
                        <tr><th>Parameter</th><th>Keterangan</th><th>Detail Nilai</th></tr>
                        <tr><td>Kategori</td><td>{cat}</td><td>Aktif / Verified</td></tr>
                        <tr><td>Status</td><td>Publikasi Standar</td><td>Terverifikasi</td></tr>
                    </table>
                </section>

                <section id="faq">
                    <h2>3. Tanya Jawab (FAQ)</h2>
                    <div class="neu-card">
                        <h3>Q: Apa manfaat utama dari topik ini?</h3>
                        <p>A: Memberikan efisiensi, akurasi data, serta pemahaman komprehensif bagi pembaca.</p>
                    </div>
                </section>

                <section id="kesimpulan">
                    <h2>4. Kesimpulan</h2>
                    <p>Kesimpulan menyeluruh dari artikel ini menegaskan pentingnya implementasi yang tepat guna mendapatkan hasil optimal.</p>
                </section>

                <div class="neu-card" style="margin-top: 20px;">
                    <h3>Bagikan Artikel Ini</h3>
                    <button class="neu-btn">Facebook</button>
                    <button class="neu-btn">Twitter</button>
                    <button class="neu-btn">WhatsApp</button>
                </div>
            </article>
            """
            
            html = get_base_html(title, desc, canonical, content)
            with open(os.path.join(cat, art_name), "w", encoding="utf-8") as f:
                f.write(html)

    print("✅ Struktur folder, file, dan ribuan artikel berhasil dibuat secara otomatis!")

if __name__ == "__main__":
    create_directory_structure()
