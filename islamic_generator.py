import os
import json
from datetime import datetime

# Konfigurasi Domain & Situs
DOMAINS = [
    "app.alhikmah.eu.org",
    "www.alhikmah.eu.org",
    "web.alhikmah.eu.org"
]
PRIMARY_DOMAIN = "https://www.alhikmah.eu.org"
SITE_NAME = "Al-Hikmah Portal & Tools"

# Daftar direktori utama sesuai struktur yang diminta
DIRECTORIES = {
    # Root files ditangani terpisah
    "root_files": [
        "index.html", "blog.html", "sitemap.html", "sitemap.xml", 
        "sitemap.txt", "robots.txt", "ads.txt", "manifest.json"
    ],
    "sub_dirs": [
        "aplikasi", "calligraphy", "code", "collor", "converter", "devoloper", 
        "domain", "domains", "eq", "finder", "hook", "img", "ip", "kodepost", 
        "link", "maps", "pdf", "qr", "quran", "removebg", "safelink", "search", 
        "seo", "source", "text", "tools", "utilities", "vidio"
    ],
    "market": [
        "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
        "property", "health", "education", "lifestyle", "hospitality", "tech", 
        "media", "smes", "luxury", "whos-who", "international", "local-resources"
    ],
    "islamic": [
        "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "kisah-birrul-walidain", 
        "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan", "kisah-nabi-dan-rasul", 
        "kisah-nabi-muhammad", "kisah-nyata", "kisah-orang-shalih", "kisah-pilihan", 
        "kisah-sahabat-nabi", "kisah-tabiin", "sejarah-islam", "nusantara"
    ],
    "assets": [
        "assets/css", "assets/js", "assets/images"
    ]
}

# Template CSS Global (Neumorphism & Responsive)
GLOBAL_CSS = """
:root {
    --bg-color: #e4ebf5;
    --text-color: #3d4852;
    --primary: #3490dc;
    --shadow-light: #ffffff;
    --shadow-dark: #c5d9e8;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
body { background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; padding: 20px; }
.container { max-width: 1200px; margin: 0 auto; }

/* Neumorphism Elements */
.neu-box {
    background: var(--bg-color);
    box-shadow: 8px 8px 15px var(--shadow-dark), -8px -8px 15px var(--shadow-light);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
}
.neu-button {
    background: var(--bg-color);
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    box-shadow: 5px 5px 10px var(--shadow-dark), -5px -5px 10px var(--shadow-light);
    cursor: pointer;
    font-weight: bold;
    color: var(--text-color);
    transition: all 0.2s ease;
}
.neu-button:active {
    box-shadow: inset 3px 3px 6px var(--shadow-dark), inset -3px -3px 6px var(--shadow-light);
}
header, footer { text-align: center; padding: 20px; }
nav { display: flex; justify-content: center; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }
nav a { text-decoration: none; color: var(--text-color); font-weight: 600; padding: 8px 15px; border-radius: 8px; background: var(--bg-color); box-shadow: 3px 3px 6px var(--shadow-dark), -3px -3px 6px var(--shadow-light); }
.content-grid { display: grid; grid-template-columns: 3fr 1fr; gap: 20px; }
@media (max-width: 768px) { .content-grid { grid-template-columns: 1fr; } }
table { width: 100%; border-collapse: collapse; margin: 15px 0; }
th, td { padding: 10px; border-bottom: 1px solid #c5d9e8; text-align: left; }
.toc { background: rgba(255,255,255,0.5); padding: 15px; border-radius: 10px; margin-bottom: 20px; }
"""

# Template Utama Artikel / Halaman
def get_article_template(title, category, slug, content_body):
    current_date = datetime.now().strftime("%Y-%m-%d")
    canonical_url = f"{PRIMARY_DOMAIN}/{category}/{slug}.html"
    
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{title} secara lengkap, akurat, dan terstruktur hanya di {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    
    <!-- Open Graph / Social Sharing -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Baca artikel lengkap seputar {title} di {SITE_NAME}.">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{PRIMARY_DOMAIN}/assets/images/featured.jpg">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="Baca artikel lengkap seputar {title}.">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "image": "{PRIMARY_DOMAIN}/assets/images/featured.jpg",
      "author": {{ "@type": "Organization", "name": "{SITE_NAME}" }},
      "publisher": {{
        "@type": "Organization",
        "name": "{SITE_NAME}",
        "logo": {{ "@type": "ImageObject", "url": "{PRIMARY_DOMAIN}/assets/images/logo.png" }}
      }},
      "datePublished": "{current_date}",
      "dateModified": "{current_date}"
    }}
    </script>

    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <div class="container">
        <!-- Header & Navbar -->
        <header class="neu-box">
            <h1>{SITE_NAME}</h1>
            <p>Portal Informasi, Artikel Terstruktur, dan Islamic Tools Terlengkap</p>
        </header>
        
        <nav>
            <a href="../index.html">Home</a>
            <a href="../blog.html">Blog</a>
            <a href="../quran/index.html">Quran</a>
            <a href="../tools/index.html">Tools</a>
            <a href="../sitemap.html">Sitemap</a>
        </nav>

        <!-- Breadcrumb -->
        <div class="neu-box" style="padding: 10px 20px; font-size: 14px;">
            <a href="../index.html">Home</a> &gt; <a href="index.html">{category.capitalize()}</a> &gt; <span>{title}</span>
        </div>

        <div class="content-grid">
            <!-- Main Content Area -->
            <main>
                <article class="neu-box">
                    <h1>{title}</h1>
                    <p style="font-size: 12px; color: #666; margin-bottom: 15px;">Dipublikasikan pada: {current_date} | Kategori: {category}</p>
                    
                    <!-- Featured Image -->
                    <div style="margin-bottom: 20px;">
                        <img src="../assets/images/featured.jpg" alt="Ilustrasi {title}" style="width: 100%; height: auto; border-radius: 10px;">
                    </div>

                    <!-- Table of Contents -->
                    <div class="toc">
                        <h3>Daftar Isi</h3>
                        <ul>
                            <li><a href="#pendahuluan">1. Pendahuluan</a></li>
                            <li><a href="#pembahasan">2. Pembahasan Utama</a></li>
                            <li><a href="#tabel-info">3. Tabel Informasi Penting</a></li>
                            <li><a href="#faq">4. Pertanyaan Umum (FAQ)</a></li>
                            <li><a href="#kesimpulan">5. Kesimpulan</a></li>
                        </ul>
                    </div>

                    <!-- Article Body -->
                    <h2 id="pendahuluan">1. Pendahuluan</h2>
                    <p>{content_body}</p>
                    
                    <!-- Adsense Unit (In-Article) -->
                    <div class="neu-box" style="text-align: center; background: #eef3fc; margin: 20px 0;">
                        <small>[ Iklan Google Adsense ]</small>
                    </div>

                    <h2 id="pembahasan">2. Pembahasan Utama</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elemen penting dalam topik ini mencakup analisis mendalam serta referensi valid yang dapat diandalkan oleh pembaca.</p>

                    <h2 id="tabel-info">3. Tabel Informasi Penting</h2>
                    <table>
                        <tr><th>Parameter</th><th>Keterangan</th></tr>
                        <tr><td>Topik Utama</td><td>{title}</td></tr>
                        <tr><td>Kategori</td><td>{category.upper()}</td></tr>
                        <tr><td>Status</td><td>Aktif / Terverifikasi</td></tr>
                    </table>

                    <h2 id="faq">4. Pertanyaan Umum (FAQ)</h2>
                    <div class="neu-box" style="background: rgba(255,255,255,0.3); margin: 10px 0;">
                        <strong>Q: Apa manfaat utama dari {title}?</strong><br>
                        A: Memberikan pemahaman komprehensif serta solusi praktis yang relevan dengan kebutuhan saat ini.
                    </div>

                    <h2 id="kesimpulan">5. Kesimpulan</h2>
                    <p id="kesimpulan">Kesimpulan dari pembahasan mengenai {title} ini adalah pentingnya penerapan pengetahuan secara konsisten untuk hasil yang optimal.</p>

                    <!-- Internal Links (7 Links) -->
                    <div class="neu-box" style="margin-top: 30px;">
                        <h3>Artikel Terkait (Internal Links)</h3>
                        <ul>
                            <li><a href="artikel1.html">Panduan Lengkap Terkait Topik 1</a></li>
                            <li><a href="artikel2.html">Strategi Jitu dan Tips Praktis</a></li>
                            <li><a href="artikel3.html">Analisis Mendalam dan Studi Kasus</a></li>
                            <li><a href="artikel4.html">Rekomendasi Terbaik Tahun Ini</a></li>
                            <li><a href="artikel5.html">Mengenal Lebih Dekat Aspek Utama</a></li>
                            <li><a href="artikel6.html">Kesalahan Umum yang Harus Dihindari</a></li>
                            <li><a href="artikel7.html">Langkah Awal Memulai dengan Mudah</a></li>
                        </ul>
                    </div>

                    <!-- External References (7 References) -->
                    <div class="neu-box" style="margin-top: 20px;">
                        <h3>Referensi Eksternal</h3>
                        <ul>
                            <li><a href="https://example.com/ref1" target="_blank" rel="nofollow">Referensi Akademik Internasional 1</a></li>
                            <li><a href="https://example.com/ref2" target="_blank" rel="nofollow">Jurnal Penelitian Terkait 2</a></li>
                            <li><a href="https://example.com/ref3" target="_blank" rel="nofollow">Dokumentasi Resmi & Standar 3</a></li>
                            <li><a href="https://example.com/ref4" target="_blank" rel="nofollow">Laporan Riset Industri 4</a></li>
                            <li><a href="https://example.com/ref5" target="_blank" rel="nofollow">Statistik & Data Global 5</a></li>
                            <li><a href="https://example.com/ref6" target="_blank" rel="nofollow">Panduan Ahli Profesional 6</a></li>
                            <li><a href="https://example.com/ref7" target="_blank" rel="nofollow">Arsip Publik Terpercaya 7</a></li>
                        </ul>
                    </div>

                    <!-- Social Sharing -->
                    <div style="display: flex; gap: 10px; margin-top: 20px;">
                        <button class="neu-button" onclick="alert('Dibagikan ke Facebook!')">Bagikan ke FB</button>
                        <button class="neu-button" onclick="alert('Dibagikan ke Twitter/X!')">Bagikan ke Twitter</button>
                        <button class="neu-button" onclick="alert('Tautan disalin!')">Salin Link</button>
                    </div>

                    <!-- Comment Section / Disqus Placeholder -->
                    <div class="neu-box" style="margin-top: 30px;">
                        <h3>Komentar / Diskusi</h3>
                        <p style="color: #777; font-size: 14px; margin-bottom: 10px;">Gunakan kolom di bawah untuk berdiskusi (Integrasi Disqus/Komentar Lokal).</p>
                        <textarea class="neu-box" style="width: 100%; height: 80px; border: none; resize: none;" placeholder="Tulis komentar Anda..."></textarea>
                        <button class="neu-button" style="margin-top: 10px;">Kirim Komentar</button>
                    </div>
                </article>
            </main>

            <!-- Sidebar -->
            <aside>
                <div class="neu-box">
                    <h3>Artikel Populer</h3>
                    <ul style="list-style: none; margin-top: 10px;">
                        <li style="margin-bottom: 8px;"><a href="artikel1.html">Topik Populer Pilihan Pembaca</a></li>
                        <li style="margin-bottom: 8px;"><a href="artikel5.html">Panduan Cepat Menguasai Dasar</a></li>
                        <li style="margin-bottom: 8px;"><a href="artikel12.html">Tips Efektif & Efisien</a></li>
                    </ul>
                </div>
                
                <div class="neu-box">
                    <h3>Artikel Terbaru</h3>
                    <ul style="list-style: none; margin-top: 10px;">
                        <li style="margin-bottom: 8px;"><a href="artikel30.html">Rilis Update Terbaru {category}</a></li>
                        <li style="margin-bottom: 8px;"><a href="artikel29.html">Inovasi Teknologi Terkini</a></li>
                    </ul>
                </div>

                <div class="neu-box" style="text-align: center;">
                    <small>[ Widget Adsense Sidebar ]</small>
                </div>
            </aside>
        </div>

        <!-- Footer -->
        <footer class="neu-box" style="margin-top: 30px;">
            <p>&copy; 2026 {SITE_NAME}. Hak Cipta Dilindungi Undang-Undang.</p>
        </footer>
    </div>
</body>
</html>
"""

def create_structure():
    print("[INFO] Memulai pembuatan struktur direktori dan file otomatis...")
    
    # 1. Buat direktori CSS assets
    os.makedirs("assets/css", exist_ok=True)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(GLOBAL_CSS)

    # 2. Buat file root
    for file_name in DIRECTORIES["root_files"]:
        if file_name == "robots.txt":
            content = f"User-agent: *\nAllow: /\nSitemap: {PRIMARY_DOMAIN}/sitemap.xml"
        elif file_name == "ads.txt":
            content = "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
        elif file_name == "manifest.json":
            content = json.dumps({"name": SITE_NAME, "short_name": "AlHikmah", "start_url": "/", "display": "standalone"}, indent=2)
        elif file_name == "sitemap.xml":
            content = f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'><url><loc>{PRIMARY_DOMAIN}/</loc></url></urlset>"
        else:
            content = f"<!DOCTYPE html><html><head><title>{file_name} - {SITE_NAME}</title><link rel='stylesheet' href='assets/css/style.css'></head><body><div class='container neu-box'><h1>Halaman {file_name}</h1><p>Selamat datang di {SITE_NAME}.</p><p><a href='index.html'>Kembali ke Beranda</a></p></div></body></html>"
        
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)

    # Kumpulan semua kategori sub-direktori
    all_categories = DIRECTORIES["sub_dirs"] + DIRECTORIES["market"] + DIRECTORIES["islamic"]

    for cat in all_categories:
        cat_path = cat
        os.makedirs(cat_path, exist_ok=True)
        
        # Buat sitemap & index di dalam kategori
        with open(os.path.join(cat_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(get_article_template(f"Kategori Utama {cat.capitalize()}", cat, "index", f"Berikut adalah kumpulan artikel lengkap dan terstruktur dalam kategori {cat}."))
        
        with open(os.path.join(cat_path, "sitemap.html"), "w", encoding="utf-8") as f:
            f.write(f"<!DOCTYPE html><html><head><title>Sitemap {cat}</title></head><body><h1>Sitemap {cat}</h1></body></html>")
        with open(os.path.join(cat_path, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write("<urlset></urlset>")
        with open(os.path.join(cat_path, "sitemap.txt"), "w", encoding="utf-8") as f:
            f.write(f"{PRIMARY_DOMAIN}/{cat}/\n")

        # Buat artikel1.html sampai artikel30.html untuk setiap kategori
        for i in range(1, 31):
            slug = f"artikel{i}"
            title = f"Panduan Lengkap {slug.capitalize()} Mengenai {cat.replace('-', ' ').title()} Bagian {i}"
            body_text = f"Artikel mendalam mengenai {slug} dalam kategori {cat} yang menyajikan informasi terkini, analisis komprehensif, serta panduan praktis untuk pembaca."
            
            file_content = get_article_template(title, cat, slug, body_text)
            with open(os.path.join(cat_path, f"{slug}.html"), "w", encoding="utf-8") as af:
                af.write(file_content)

    print("[SUKSES] Seluruh struktur direktori, file pendukung, dan puluhan artikel berhasil dibuat!")

if __name__ == "__main__":
    create_structure()
