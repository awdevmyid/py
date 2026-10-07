import os
import json
from datetime import datetime

# Konfigurasi Domain & Situs
DOMAIN = "https://mikrodinet.eu.org"
SITE_NAME = "MikroDiNet"
CURRENT_YEAR = datetime.now().year

# Struktur Direktori Utama & Subkategori
DIRECTORIES = {
    "root": [
        "index.html", "blog.html", "sitemap.html", "sitemap.xml", "sitemap.txt",
        "robots.txt", "ads.txt", "manifest.json"
    ],
    "aplikasi": [
        "index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"
    ] + [f"artikel{i}.html" for i in range(1, 31)],
    
    # Kategori Utilitas & Tools Umum
    "sub_kategori": [
        "calligraphy", "code", "collor", "converter", "devoloper", "domain", 
        "domains", "eq", "finder", "hook", "img", "ip", "kodepost", "link", 
        "maps", "pdf", "qr", "quran", "removebg", "safelink", "search", "seo", 
        "source", "text", "tools", "utilities", "vidio"
    ],
    
    # Kategori Market / Ekonomi
    "market": [
        "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
        "property", "health", "education", "lifestyle", "hospitality", "tech", 
        "media", "smes", "luxury", "whos-who", "international", "local-resources"
    ],
    
    # Kategori Islamic
    "islamic": [
        "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "kisah-birrul-walidain", 
        "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan", "kisah-nabi-dan-rasul", 
        "kisah-nabi-muhammad", "kisah-nyata", "kisah-orang-shalih", "kisah-pilihan", 
        "kisah-sahabat-nabi", "kisah-tabiin", "sejarah-islam", "nusantara"
    ],
    
    # Aset Pendukung
    "assets": [
        "assets/css/style.css",
        "assets/js/main.js",
        "assets/js/islamic-tools.js",
        "assets/images/"
    ]
}

# Template CSS Global (Neumorphism & Responsive Design)
CSS_CONTENT = """
:root {
    --bg-color: #e0e5ec;
    --text-color: #4a5568;
    --primary: #3182ce;
    --shadow-light: #ffffff;
    --shadow-dark: #a3b1c6;
}

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
body { background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; padding: 20px; }

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
    color: var(--text-color);
    font-weight: bold;
    transition: all 0.2s ease;
}

.neu-button:active {
    box-shadow: inset 3px 3px 6px var(--shadow-dark), inset -3px -3px 6px var(--shadow-light);
}

header, footer { text-align: center; padding: 20px; }
nav ul { display: flex; justify-content: center; list-style: none; gap: 15px; flex-wrap: wrap; margin-bottom: 20px; }
nav a { text-decoration: none; color: var(--text-color); font-weight: 600; }

.container { max-width: 1200px; margin: 0 auto; }
.main-content { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }

@media (max-width: 768px) {
    .main-content { grid-template-columns: 1fr; }
}

table { width: 100%; border-collapse: collapse; margin: 15px 0; }
th, td { padding: 10px; border: 1px solid var(--shadow-dark); text-align: left; }
img { max-width: 100%; height: auto; border-radius: 8px; }
"""

# Template JavaScript Utama & Fitur Interaktif Islamic Tools
JS_CONTENT = """
document.addEventListener("DOMContentLoaded", function() {
    console.log("MikroDiNet Script Initialized.");
});
"""

ISLAMIC_TOOLS_JS = """
// Logika Terpisah untuk Islamic Tools (Prayer Times, Qibla, Kalender Hijriah, Zakat)
function getPrayerTimes() {
    // Simulasi pengambilan data waktu salat via API eksternal
    const container = document.getElementById("prayer-times-result");
    if(container) {
        container.innerHTML = "<p>Subuh: 04:30 | Dzuhur: 12:00 | Ashar: 15:15 | Maghrib: 18:00 | Isya: 19:10</p>";
    }
}

function calculateZakat(nisab, wealth) {
    if(wealth >= nisab) {
        return wealth * 0.025;
    }
    return 0;
}
"""

def generate_html_template(title, description, canonical, content_body, breadcrumbs, faqs=[]):
    """Menghasilkan template HTML terpusat lengkap dengan SEO, Schema.org, dan Neumorphism."""
    
    # Schema.org JSON-LD Breadcrumb & Article
    schema_faq = ""
    if faqs:
        faq_items = [{
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        } for q, a in faqs]
        schema_faq = json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_items
        }, indent=4)

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
    
    <link rel="stylesheet" href="{DOMAIN}/assets/css/style.css">
    
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
    {f'<script type="application/ld+json">{schema_faq}</script>' if schema_faq else ''}
</head>
<body>
    <div class="container">
        <header class="neu-box">
            <h1>{SITE_NAME}</h1>
            <nav>
                <ul>
                    <li><a href="{DOMAIN}/index.html">Home</a></li>
                    <li><a href="{DOMAIN}/blog.html">Blog</a></li>
                    <li><a href="{DOMAIN}/aplikasi/index.html">Aplikasi</a></li>
                    <li><a href="{DOMAIN}/market/finance/index.html">Market</a></li>
                    <li><a href="{DOMAIN}/islamic/sejarah-islam/index.html">Islamic</a></li>
                </ul>
            </nav>
        </header>

        <div class="main-content">
            <main>
                <article class="neu-box">
                    <nav aria-label="breadcrumb">
                        <small>{breadcrumbs}</small>
                    </nav>
                    
                    <h1>{title}</h1>
                    <img src="{DOMAIN}/assets/images/featured.jpg" alt="{title}" loading="lazy">
                    
                    <div class="neu-box" style="margin: 20px 0;">
                        <h3>Daftar Isi</h3>
                        <ul>
                            <li><a href="#pengantar">1. Pengantar</a></li>
                            <li><a href="#informasi">2. Tabel Informasi Utama</a></li>
                            <li><a href="#pembahasan">3. Pembahasan Mendalam</a></li>
                            <li><a href="#faq">4. Pertanyaan Umum (FAQ)</a></li>
                        </ul>
                    </div>

                    <section id="pengantar">
                        <p>{content_body}</p>
                    </section>

                    <section id="informasi">
                        <h3>Tabel Informasi Penting</h3>
                        <table>
                            <tr><th>Atribut</th><th>Keterangan</th></tr>
                            <tr><td>Kategori</td><td>Teknologi & Informasi</td></tr>
                            <tr><td>Pembaruan</td><td>{CURRENT_YEAR}</td></tr>
                        </table>
                    </section>

                    <section id="pembahasan">
                        <h2>Analisis & Penjelasan Lengkap</h2>
                        <p>Artikel ini menyajikan pembahasan menyeluruh yang dirancang untuk memberikan wawasan bernilai tinggi bagi pembaca setia {SITE_NAME}.</p>
                    </section>

                    {f'''
                    <section id="faq">
                        <h2>FAQ (Pertanyaan yang Sering Diajukan)</h2>
                        {"".join([f"<h4>{q}</h4><p>{a}</p>" for q, a in faqs])}
                    </section>
                    ''' if faqs else ''}

                    <div class="neu-box" style="margin-top: 20px;">
                        <h3>Kesimpulan</h3>
                        <p>Demikian ulasan lengkap mengenai topik ini. Semoga bermanfaat dan menjadi referensi terpercaya Anda.</p>
                    </div>

                    <!-- Social Sharing & Adsense Placeholder -->
                    <div class="neu-box" style="text-align: center; margin-top: 20px;">
                        <p><strong>Bagikan Artikel Ini:</strong></p>
                        <button class="neu-button">Facebook</button>
                        <button class="neu-button">Twitter / X</button>
                        <button class="neu-button">WhatsApp</button>
                    </div>
                </article>

                <!-- Kolom Komentar Disqus / Diskusi -->
                <div class="neu-box">
                    <h3>Kolom Komentar</h3>
                    <p>Tulis tanggapan atau pertanyaan Anda di bawah ini:</p>
                    <textarea class="neu-box" style="width: 100%; height: 80px; border: none;" placeholder="Tulis komentar..."></textarea>
                    <button class="neu-button">Kirim Komentar</button>
                </div>
            </main>

            <aside>
                <div class="neu-box">
                    <h3>Artikel Populer</h3>
                    <ul>
                        <li><a href="#">Panduan Lengkap Teknologi {CURRENT_YEAR}</a></li>
                        <li><a href="#">Tips & Trik Optimasi SEO Website</a></li>
                    </ul>
                </div>
                <div class="neu-box">
                    <h3>Artikel Terbaru</h3>
                    <ul>
                        <li><a href="#">Inovasi Layanan Digital Terbaru</a></li>
                        <li><a href="#">Strategi Keuangan Modern</a></li>
                    </ul>
                </div>
                <div class="neu-box">
                    <h3>Label / Kategori</h3>
                    <p><a href="#">Teknologi</a> | <a href="#">Islamic</a> | <a href="#">Market</a></p>
                </div>
            </aside>
        </div>

        <footer class="neu-box">
            <p>&copy; {CURRENT_YEAR} {SITE_NAME}. All rights reserved. | <a href="{DOMAIN}/sitemap.html">Sitemap</a></p>
        </footer>
    </div>
    <script src="{DOMAIN}/assets/js/main.js"></script>
</body>
</html>
"""

def create_structure():
    print("Memulai pembuatan struktur direktori dan file...")
    
    # 1. Buat Direktori Aset & File Pendukung
    os.makedirs("assets/css", exist_ok=True)
    os.makedirs("assets/js", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)
    
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(CSS_CONTENT)
    with open("assets/js/main.js", "w", encoding="utf-8") as f:
        f.write(JS_CONTENT)
    with open("assets/js/islamic-tools.js", "w", encoding="utf-8") as f:
        f.write(ISLAMIC_TOOLS_JS)

    # 2. Buat File Root
    for filename in DIRECTORIES["root"]:
        filepath = filename
        if filename.endswith(".html"):
            content = generate_html_template(
                f"Beranda Utama - {SITE_NAME}",
                "Portal informasi, tools, aplikasi, market, dan wawasan Islami terpercaya.",
                f"{DOMAIN}/{filename}",
                "Selamat datang di pusat informasi digital dan utilitas terpadu.",
                "Home",
                [("Apa itu MikroDiNet?", "Platform direktori informasi dan tools terlengkap.")]
            )
        elif filename.endswith(".xml"):
            content = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{DOMAIN}/{filename}</loc></url></urlset>'
        elif filename == "robots.txt":
            content = f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml"
        elif filename == "ads.txt":
            content = "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
        elif filename == "manifest.json":
            content = json.dumps({"name": SITE_NAME, "short_name": SITE_NAME, "start_url": "/index.html", "display": "standalone"}, indent=4)
        else:
            content = f"Sitemap TXT untuk {DOMAIN}"
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # 3. Buat Kategori Sub-Tools, Market, dan Islamic beserta subfoldernya
    all_subcats = DIRECTORIES["sub_kategori"] + DIRECTORIES["market"] + DIRECTORIES["islamic"]
    
    for subcat in all_subcats:
        # Tentukan induk kategori berdasarkan list
        parent = "market" if subcat in DIRECTORIES["market"] else ("islamic" if subcat in DIRECTORIES["islamic"] else "")
        folder_path = os.path.join(parent, subcat) if parent else subcat
        os.makedirs(folder_path, exist_ok=True)
        
        # Buat index.html di setiap subkategori
        index_path = os.path.join(folder_path, "index.html")
        html_data = generate_html_template(
            f"Kategori {subcat.replace('-', ' ').title()} - {SITE_NAME}",
            f"Kumpulan artikel, informasi, dan layanan terbaik seputar {subcat}.",
            f"{DOMAIN}/{folder_path}/index.html",
            f"Halaman khusus untuk kategori {subcat}. Temukan berbagai pembahasan komprehensif di sini.",
            f"Home &gt; {parent.title() if parent else ''} &gt; {subcat.title()}"
        )
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html_data)

    # 4. Buat Folder Aplikasi & 30 Artikel di dalamnya
    os.makedirs("aplikasi", exist_ok=True)
    for i in range(1, 31):
        file_name = f"artikel{i}.html" if i > 1 else "index.html" if i == 1 else f"artikel{i}.html"
        # Untuk artikel aplikasi
        file_path = os.path.join("aplikasi", f"artikel{i}.html" if i > 1 else "index.html")
        html_data = generate_html_template(
            f"Aplikasi Artikel {i} - {SITE_NAME}",
            f"Pembahasan mendalam mengenai aplikasi dan teknologi artikel {i}.",
            f"{DOMAIN}/aplikasi/artikel{i}.html",
            f"Ini adalah konten artikel nomor {i} dalam direktori aplikasi.",
            "Home &gt; Aplikasi &gt; Artikel " + str(i),
            [("Bagaimana cara menggunakan aplikasi ini?", "Ikuti panduan langkah demi langkah yang tersedia di artikel.")]
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_data)

    print("Struktur folder dan file berhasil dibuat sepenuhnya!")

if __name__ == "__main__":
    create_structure()
