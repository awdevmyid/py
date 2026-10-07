import os
import json
from datetime import datetime

# Konfigurasi Domain & Situs
DOMAIN = "https://arabictex.github.io"
SITE_NAME = "ArabicTex & Islamic Hub"
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

# Daftar Direktori Utama & Sub-kategori sesuai struktur Anda
DIRECTORIES = {
    "root": [
        "index.html", "blog.html", "sitemap.html", "sitemap.xml", 
        "sitemap.txt", "robots.txt", "ads.txt", "manifest.json"
    ],
    "folders": [
        "calligraphy", "code", "collor", "converter", "devoloper", "domain", 
        "domains", "eq", "finder", "hook", "img", "ip", "kodepost", "link", 
        "maps", "pdf", "qr", "quran", "removebg", "safelink", "search", 
        "seo", "source", "text", "tools", "utilities", "vidio"
    ],
    "aplikasi": [
        "index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"
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

# Template CSS Global dengan Neumorphism
GLOBAL_CSS = """
:root {
    --bg-color: #e0e5ec;
    --text-color: #4a5568;
    --shadow-light: #ffffff;
    --shadow-dark: #a3b1c6;
    --primary: #3182ce;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
body { background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; padding: 20px; }
header, footer { background: var(--bg-color); padding: 20px; border-radius: 15px; box-shadow: 9px 9px 16px var(--shadow-dark), -9px -9px 16px var(--shadow-light); margin-bottom: 20px; text-align: center; }
nav a { margin: 0 10px; text-decoration: none; color: var(--primary); font-weight: bold; }
.container { display: flex; flex-wrap: wrap; gap: 20px; }
main { flex: 3; background: var(--bg-color); padding: 30px; border-radius: 15px; box-shadow: inset 5px 5px 10px var(--shadow-dark), inset -5px -5px 10px var(--shadow-light); }
aside { flex: 1; background: var(--bg-color); padding: 20px; border-radius: 15px; box-shadow: 9px 9px 16px var(--shadow-dark), -9px -9px 16px var(--shadow-light); }
.neu-card { background: var(--bg-color); padding: 20px; border-radius: 12px; box-shadow: 6px 6px 12px var(--shadow-dark), -6px -6px 12px var(--shadow-light); margin-bottom: 20px; }
h1, h2, h3 { color: #2d3748; margin-bottom: 15px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { padding: 12px; border: 1px solid #cbd5e0; text-align: left; }
.toc { background: #edf2f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
.faq-item { margin-bottom: 15px; }
@media(max-width: 768px) { .container { flex-direction: column; } }
"""

def generate_html_template(title, desc, canonical, category, h1_title):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{canonical}">
    
    <!-- Open Graph / Social Sharing -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{DOMAIN}/assets/images/featured.jpg">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{DOMAIN}/assets/images/featured.jpg">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{desc}",
      "image": "{DOMAIN}/assets/images/featured.jpg",
      "author": {{ "@type": "Organization", "name": "{SITE_NAME}" }},
      "publisher": {{ "@type": "Organization", "name": "{SITE_NAME}", "logo": {{ "@type": "ImageObject", "url": "{DOMAIN}/assets/images/logo.png" }} }},
      "datePublished": "{CURRENT_DATE}",
      "dateModified": "{CURRENT_DATE}"
    }}
    </script>

    <link rel="stylesheet" href="{DOMAIN}/assets/css/style.css">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
</head>
<body>
    <header>
        <h1>{SITE_NAME}</h1>
        <nav>
            <a href="{DOMAIN}/index.html">Home</a>
            <a href="{DOMAIN}/blog.html">Blog</a>
            <a href="{DOMAIN}/islamic/biografi-ulama/index.html">Islamic</a>
            <a href="{DOMAIN}/market/economy/index.html">Market</a>
            <a href="{DOMAIN}/sitemap.html">Sitemap</a>
        </nav>
    </header>

    <div class="container">
        <main>
            <!-- Breadcrumb -->
            <nav aria-label="breadcrumb" style="margin-bottom: 15px; font-size: 0.9rem;">
                <a href="{DOMAIN}/index.html">Home</a> &gt; <a href="#">{category.capitalize()}</a> &gt; <span>{h1_title}</span>
            </nav>

            <h1>{h1_title}</h1>
            
            <img src="{DOMAIN}/assets/images/featured.jpg" alt="{h1_title} - Featured Image" style="width:100%; height:auto; border-radius:10px; margin-bottom:20px;">

            <!-- Table of Contents -->
            <div class="toc">
                <h3>Daftar Isi</h3>
                <ul>
                    <li><a href="#pengantar">1. Pengantar</a></li>
                    <li><a href="#informasi">2. Tabel Informasi Penting</a></li>
                    <li><a href="#pembahasan">3. Pembahasan Mendalam</a></li>
                    <li><a href="#faq">4. Tanya Jawab (FAQ)</a></li>
                    <li><a href="#kesimpulan">5. Kesimpulan</a></li>
                </ul>
            </div>

            <h2 id="pengantar">1. Pengantar</h2>
            <p>{desc} Artikel ini membahas secara komprehensif mengenai berbagai aspek penting yang berkaitan langsung dengan kebutuhan Anda hari ini.</p>

            <!-- Adsense In-Article -->
            <div class="neu-card" style="text-align:center;">
                <ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-XXXXXXXXXXXXXXXX" data-ad-slot="1234567890"></ins>
                <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
            </div>

            <h2 id="informasi">2. Tabel Informasi Penting</h2>
            <table>
                <tr><th>Parameter</th><th>Keterangan</th></tr>
                <tr><td>Kategori</td><td>{category.capitalize()}</td></tr>
                <tr><td>Tanggal Rilis</td><td>{CURRENT_DATE}</td></tr>
                <tr><td>Status</td><td>Aktif / Terverifikasi</td></tr>
            </table>

            <h2 id="pembahasan">3. Pembahasan Mendalam</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            
            <h3>Sub-Bab Pendukung</h3>
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

            <!-- Internal Links -->
            <div class="neu-card">
                <h3>Artikel Terkait (Internal Links)</h3>
                <ul>
                    <li><a href="artikel1.html">Panduan Lengkap Artikel 1</a></li>
                    <li><a href="artikel2.html">Analisis Mendalam Artikel 2</a></li>
                    <li><a href="artikel3.html">Strategi Jitu Artikel 3</a></li>
                    <li><a href="artikel4.html">Tips Praktis Artikel 4</a></li>
                    <li><a href="artikel5.html">Studi Kasus Artikel 5</a></li>
                    <li><a href="artikel6.html">Update Terbaru Artikel 6</a></li>
                    <li><a href="artikel7.html">Rekomendasi Terbaik Artikel 7</a></li>
                </ul>
            </div>

            <h2 id="faq">4. Tanya Jawab (FAQ)</h2>
            <div class="faq-item">
                <strong>Q: Apa manfaat utama dari topik ini?</strong><br>
                <p>A: Manfaat utamanya adalah memberikan kejelasan, efisiensi, dan referensi yang valid.</p>
            </div>
            <div class="faq-item">
                <strong>Q: Bagaimana cara memulainya?</strong><br>
                <p>A: Anda dapat mengikuti panduan langkah-demi-langkah yang telah disediakan di atas.</p>
            </div>

            <h2 id="kesimpulan">5. Kesimpulan</h2>
            <p id="kesimpulan">Dengan memahami seluruh poin di atas, diharapkan Anda dapat mengimplementasikannya dengan baik dan memperoleh hasil yang optimal.</p>

            <!-- External References -->
            <div class="neu-card" style="font-size: 0.9rem;">
                <h4>Referensi Eksternal & Sumber:</h4>
                <ol>
                    <li><a href="https://example.com/ref1" target="_blank" rel="nofollow">Referensi Resmi Industri 1</a></li>
                    <li><a href="https://example.com/ref2" target="_blank" rel="nofollow">Jurnal Akademik Terkait 2</a></li>
                    <li><a href="https://example.com/ref3" target="_blank" rel="nofollow">Laporan Riset Global 3</a></li>
                    <li><a href="https://example.com/ref4" target="_blank" rel="nofollow">Dokumentasi Standar 4</a></li>
                    <li><a href="https://example.com/ref5" target="_blank" rel="nofollow">Statistik & Data Pasar 5</a></li>
                    <li><a href="https://example.com/ref6" target="_blank" rel="nofollow">Analisis Ahli Independen 6</a></li>
                    <li><a href="https://example.com/ref7" target="_blank" rel="nofollow">Arsip Publik Terpercaya 7</a></li>
                </ol>
            </div>

            <!-- Social Sharing -->
            <div class="neu-card" style="text-align:center;">
                <h4>Bagikan Artikel Ini:</h4>
                <a href="#" class="neu-card" style="padding:5px 10px; display:inline-block; margin:5px;">Facebook</a>
                <a href="#" class="neu-card" style="padding:5px 10px; display:inline-block; margin:5px;">Twitter / X</a>
                <a href="#" class="neu-card" style="padding:5px 10px; display:inline-block; margin:5px;">WhatsApp</a>
                <a href="#" class="neu-card" style="padding:5px 10px; display:inline-block; margin:5px;">Telegram</a>
            </div>

            <!-- Comment Section / Disqus -->
            <div class="neu-card">
                <h3>Diskusi & Komentar</h3>
                <div id="disqus_thread"></div>
                <script>
                    var disqus_shortname = 'arabictex';
                    (function() {{
                        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                    }})();
                </script>
            </div>
        </main>

        <aside>
            <div class="neu-card">
                <h3>Artikel Populer</h3>
                <ul>
                    <li><a href="#">Topik Populer Pilihan 1</a></li>
                    <li><a href="#">Topik Populer Pilihan 2</a></li>
                    <li><a href="#">Topik Populer Pilihan 3</a></li>
                </ul>
            </div>
            <div class="neu-card">
                <h3>Artikel Terbaru</h3>
                <ul>
                    <li><a href="#">Rilis Berita Terbaru 1</a></li>
                    <li><a href="#">Rilis Berita Terbaru 2</a></li>
                </ul>
            </div>
            <div class="neu-card">
                <h3>Label / Kategori</h3>
                <p><a href="#">{category.capitalize()}</a>, <a href="#">Panduan</a>, <a href="#">Tools</a></p>
            </div>
        </aside>
    </div>

    <footer>
        <p>&copy; 2026 {SITE_NAME}. Hak Cipta Dilindungi.</p>
    </footer>
</body>
</html>
"""

def create_structure():
    print("Membangun struktur direktori dan file...")
    
    # Buat file CSS Utama
    os.makedirs("assets/css", exist_ok=True)
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(GLOBAL_CSS)

    # Buat file JS untuk Islamic Tools
    os.makedirs("assets/js", exist_ok=True)
    with open("assets/js/islamic-tools.js", "w", encoding="utf-8") as f:
        f.write("""
// Logika Terpisah untuk Islamic Tools (Waktu Shalat, Kiblat, Cuaca, dll.)
console.log("Islamic Tools JS Loaded Successfully.");
function getPrayerTimes() { /* Implementasi API Waktu Shalat */ }
function getQiblaDirection() { /* Implementasi Arah Kiblat */ }
""")

    # 1. Root Files
    for file in DIRECTORIES["root"]:
        path = file
        with open(path, "w", encoding="utf-8") as f:
            if file == "robots.txt":
                f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml")
            elif file == "sitemap.txt":
                f.write(f"{DOMAIN}/\n{DOMAIN}/blog.html")
            elif file == "manifest.json":
                f.write(json.dumps({"name": SITE_NAME, "short_name": "ArabicTex", "start_url": "/", "display": "standalone"}))
            else:
                f.write(generate_html_template("Home - " + SITE_NAME, "Pusat informasi dan tools Islami serta teknologi.", f"{DOMAIN}/{file}", "home", "Selamat Datang di " + SITE_NAME))

    # 2. Folders biasa (Single index.html)
    for folder in DIRECTORIES["folders"]:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(generate_html_template(folder.capitalize() + " - " + SITE_NAME, f"Halaman utama kategori {folder}", f"{DOMAIN}/{folder}/index.html", folder, f"Kategori: {folder.capitalize()}"))

    # 3. Kategori Aplikasi (30 Artikel)
    os.makedirs("aplikasi", exist_ok=True)
    with open("aplikasi/index.html", "w", encoding="utf-8") as f:
        f.write(generate_html_template("Aplikasi & Tools - " + SITE_NAME, "Kumpulan aplikasi web dan tools lengkap.", f"{DOMAIN}/aplikasi/index.html", "aplikasi", "Aplikasi & Tools Terlengkap"))
    
    for i in range(1, 31):
        filename = f"artikel{i}.html"
        title = f"Panduan Aplikasi & Tools Bagian {i} - {SITE_NAME}"
        desc = f"Pembahasan lengkap artikel aplikasi nomor {i} untuk mendukung produktivitas Anda."
        with open(os.path.join("aplikasi", filename), "w", encoding="utf-8") as f:
            f.write(generate_html_template(title, desc, f"{DOMAIN}/aplikasi/{filename}", "aplikasi", f"Artikel Aplikasi #{i}"))

    # 4. Kategori Market (Subkategori + Artikel)
    for sub in DIRECTORIES["market"]:
        dir_path = os.path.join("market", sub)
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(generate_html_template(sub.replace("-", " ").capitalize() + " Market - " + SITE_NAME, f"Analisis market sektor {sub}.", f"{DOMAIN}/market/{sub}/index.html", "market", f"Market: {sub.replace('-', ' ').capitalize()}"))
        
        # Buat 5 contoh artikel per submarket agar lengkap
        for i in range(1, 6):
            art_name = f"artikel{i}.html"
            with open(os.path.join(dir_path, art_name), "w", encoding="utf-8") as f:
                f.write(generate_html_template(f"Analisis {sub} #{i} - Market", f"Pembahasan mendalam market {sub} artikel ke-{i}.", f"{DOMAIN}/market/{sub}/{art_name}", "market", f"Analisis {sub.capitalize()} #{i}"))

    # 5. Kategori Islamic (Subkategori + Artikel + Integrasi Tools)
    for sub in DIRECTORIES["islamic"]:
        dir_path = os.path.join("islamic", sub)
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(generate_html_template(sub.replace("-", " ").capitalize() + " - " + SITE_NAME, f"Kumpulan literatur dan kisah Islami: {sub}.", f"{DOMAIN}/islamic/{sub}/index.html", "islamic", f"Kategori Islami: {sub.replace('-', ' ').capitalize()}"))
        
        for i in range(1, 6):
            art_name = f"artikel{i}.html"
            with open(os.path.join(dir_path, art_name), "w", encoding="utf-8") as f:
                f.write(generate_html_template(f"Kisah & Sejarah {sub} #{i}", f"Kisah teladan dan sejarah Islam pada kategori {sub}.", f"{DOMAIN}/islamic/{sub}/{art_name}", "islamic", f"Kisah {sub.capitalize()} #{i}"))

    print("Semua struktur folder dan file berhasil digenerate secara otomatis!")

if __name__ == "__main__":
    create_structure()
