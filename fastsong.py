import os

# Konfigurasi Domain
DOMAIN_NAME = "https://fastsong.eu.org"
SITE_TITLE_DEFAULT = "FastSong - Portal Informasi, Tools, dan Artikel Islami"

# Struktur direktori utama beserta subdirektorinya
DIRECTORIES = {
    "root_files": [
        "index.html",
        "blog.html",
        "sitemap.html",
        "sitemap.xml",
        "sitemap.txt",
        "robots.txt",
        "ads.txt",
        "manifest.json"
    ],
    "categories": [
        "calligraphy", "code", "collor", "converter", "devoloper", 
        "domain", "domains", "eq", "finder", "hook", "img", "ip", 
        "kodepost", "link", "maps", "pdf", "qr", "quran", "removebg", 
        "safelink", "search", "seo", "source", "text", "tools", 
        "utilities", "vidio"
    ],
    "special_folders": {
        "aplikasi": 30, # Mengandung artikel 1-30 + sitemaps
        "market": [
            "finance", "macro", "micro", "economy", "explainers", 
            "manufacturing", "property", "health", "education", 
            "lifestyle", "hospitality", "tech", "media", "smes", 
            "luxury", "whos-who", "international", "local-resources"
        ],
        "islamic": [
            "biografi-ulama", "kisah-hikmah", "kisah-sejarah", 
            "kisah-birrul-walidain", "kisah-hidayah-islam", "kisah-kaum-durhaka", 
            "kisah-masa-depan", "kisah-nabi-dan-rasul", "kisah-nabi-muhammad", 
            "kisah-nyata", "kisah-orang-shalih", "kisah-pilihan", 
            "kisah-sahabat-nabi", "kisah-tabiin", "sejarah-islam", "nusantara"
        ],
        "assets": [
            "css", "js", "images"
        ]
    }
}

# Template HTML Terpusat dengan gaya Neumorphism, Adsense Ready, SEO, Schema, & Responsive
def get_article_template(title, category, slug):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - FastSong</title>
    <meta name="description" content="Baca artikel lengkap mengenai {title} di kategori {category} hanya di FastSong.eu.org. Temukan informasi terpercaya, FAQ, dan panduan lengkap.">
    <link rel="canonical" href="{DOMAIN_NAME}/{category}/{slug}">
    
    <!-- Open Graph / Social Sharing -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Informasi mendalam seputar {title}.">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{DOMAIN_NAME}/{category}/{slug}">
    <meta property="og:image" content="{DOMAIN_NAME}/assets/images/featured.jpg">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="Informasi mendalam seputar {title}.">
    <meta name="twitter:image" content="{DOMAIN_NAME}/assets/images/featured.jpg">

    <!-- CSS & Neumorphism Styling -->
    <link rel="stylesheet" href="{DOMAIN_NAME}/assets/css/style.css">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "image": ["{DOMAIN_NAME}/assets/images/featured.jpg"],
      "author": {{
        "@type": "Organization",
        "name": "FastSong"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "FastSong",
        "logo": {{
          "@type": "ImageObject",
          "url": "{DOMAIN_NAME}/assets/images/logo.png"
        }}
      }},
      "mainEntityOfPage": "{DOMAIN_NAME}/{category}/{slug}"
    }}
    </script>
</head>
<body>
    <!-- Header / Navbar -->
    <header class="neu-header">
        <div class="container nav-container">
            <a href="{DOMAIN_NAME}/" class="logo">FastSong</a>
            <nav class="nav-links">
                <a href="{DOMAIN_NAME}/">Home</a>
                <a href="{DOMAIN_NAME}/blog.html">Blog</a>
                <a href="{DOMAIN_NAME}/aplikasi/">Aplikasi</a>
                <a href="{DOMAIN_NAME}/market/finance/">Market</a>
                <a href="{DOMAIN_NAME}/islamic/">Islamic</a>
            </nav>
        </div>
    </header>

    <!-- Main Content Layout -->
    <main class="container main-layout">
        <article class="content-area">
            <!-- Breadcrumb -->
            <nav class="breadcrumb">
                <a href="{DOMAIN_NAME}/">Home</a> &gt; <a href="{DOMAIN_NAME}/{category}/">{category.capitalize()}</a> &gt; <span>{title}</span>
            </nav>

            <h1 class="main-title">{title}</h1>
            
            <!-- Featured Image -->
            <div class="featured-image-wrapper">
                <img src="{DOMAIN_NAME}/assets/images/featured.jpg" alt="Ilustrasi {title}" class="neu-img">
            </div>

            <!-- Table of Contents -->
            <div class="toc-box neu-card">
                <h3>Daftar Isi</h3>
                <ul>
                    <li><a href="#pendahuluan">1. Pendahuluan</a></li>
                    <li><a href="#informasi-utama">2. Informasi Utama & Tabel Data</a></li>
                    <li><a href="#faq">3. Pertanyaan Umum (FAQ)</a></li>
                    <li><a href="#kesimpulan">4. Kesimpulan</a></li>
                </ul>
            </div>

            <!-- Adsense Top Slot -->
            <div class="adsense-slot neu-inset">
                <p>-- Iklan Google Adsense --</p>
            </div>

            <section id="pendahuluan">
                <h2>Pendahuluan</h2>
                <p>Selamat datang di pembahasan mengenai {title}. Pada artikel ini, kita akan mengupas tuntas berbagai aspek penting yang berkaitan dengan kategori {category} secara mendalam dan terstruktur.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            </section>

            <section id="informasi-utama">
                <h2>Informasi Utama & Spesifikasi</h2>
                <p>Berikut adalah tabel informasi ringkas terkait topik yang dibahas:</p>
                <table class="neu-table">
                    <tr>
                        <th>Parameter</th>
                        <th>Keterangan</th>
                    </tr>
                    <tr>
                        <td>Kategori</td>
                        <td>{category.capitalize()}</td>
                    </tr>
                    <tr>
                        <td>Pembaruan Terakhir</td>
                        <td>2026</td>
                    </tr>
                    <tr>
                        <td>Status</td>
                        <td>Aktif / Terverifikasi</td>
                    </tr>
                </table>
            </section>

            <!-- Adsense Middle Slot -->
            <div class="adsense-slot neu-inset">
                <p>-- Iklan Google Adsense --</p>
            </div>

            <section id="faq">
                <h2>Pertanyaan Umum (FAQ)</h2>
                <div class="faq-item">
                    <h3>Apa itu {title}?</h3>
                    <p>{title} adalah salah satu topik utama yang dibahas untuk memberikan solusi dan informasi akurat bagi pengguna di FastSong.</p>
                </div>
                <div class="faq-item">
                    <h3>Bagaimana cara mengakses layanan terkait?</h3>
                    <p>Anda dapat menjelajahi menu navigasi atau menggunakan fitur pencarian internal yang tersedia di situs ini.</p>
                </div>
            </section>

            <section id="kesimpulan">
                <h2>Kesimpulan</h2>
                <p>Demikian pembahasan lengkap mengenai {title}. Semoga artikel ini bermanfaat dan memberikan wawasan baru bagi Anda.</p>
            </section>

            <!-- Social Sharing -->
            <div class="social-sharing">
                <h3>Bagikan Artikel Ini:</h3>
                <button class="neu-btn">Facebook</button>
                <button class="neu-btn">Twitter / X</button>
                <button class="neu-btn">WhatsApp</button>
                <button class="neu-btn">Telegram</button>
            </div>

            <!-- Internal Links (7 Items) -->
            <div class="related-links neu-card">
                <h3>Artikel Terkait</h3>
                <ul>
                    <li><a href="#">Panduan Lengkap Teknologi Modern di FastSong</a></li>
                    <li><a href="#">Tips dan Trik Optimalisasi SEO Halaman Website</a></li>
                    <li><a href="#">Mengenal Lebih Dekat Layanan Utilitas Digital</a></li>
                    <li><a href="#">Kumpulan Tools Gratis untuk Kreator Konten</a></li>
                    <li><a href="#">Strategi Keuangan Mikro dan Makro Terkini</a></li>
                    <li><a href="#">Kisah Inspiratif dan Biografi Tokoh Berpengaruh</a></li>
                    <li><a href="#">Solusi Praktis Pemrograman dan Pengembangan Web</a></li>
                </ul>
            </div>

            <!-- External References (7 Items) -->
            <div class="external-refs neu-card">
                <h3>Referensi Luar</h3>
                <ul>
                    <li><a href="https://developer.mozilla.org" target="_blank" rel="nofollow">MDN Web Docs</a></li>
                    <li><a href="https://github.com" target="_blank" rel="nofollow">GitHub Open Source</a></li>
                    <li><a href="https://stackoverflow.com" target="_blank" rel="nofollow">Stack Overflow Developer Community</a></li>
                    <li><a href="https://w3schools.com" target="_blank" rel="nofollow">W3Schools Tutorials</a></li>
                    <li><a href="https://python.org" target="_blank" rel="nofollow">Python Official Documentation</a></li>
                    <li><a href="https://schema.org" target="_blank" rel="nofollow">Schema.org Structured Data</a></li>
                    <li><a href="https://wikipedia.org" target="_blank" rel="nofollow">Wikipedia Ensiklopedia Bebas</a></li>
                </ul>
            </div>

            <!-- Comment Section / Disqus -->
            <div class="comments-section neu-card">
                <h3>Komentar</h3>
                <div id="disqus_thread"></div>
                <p><em>(Integrasi Disqus / Komentar pembaca dimuat di sini)</em></p>
            </div>
        </article>

        <!-- Sidebar -->
        <aside class="sidebar">
            <!-- Search Widget -->
            <div class="widget neu-card">
                <h3>Pencarian</h3>
                <input type="text" placeholder="Cari artikel..." class="neu-input">
            </div>

            <!-- Popular Articles -->
            <div class="widget neu-card">
                <h3>Artikel Populer</h3>
                <ul>
                    <li><a href="#">Cara Cepat Menggunakan Tools Konverter PDF</a></li>
                    <li><a href="#">10 Tips Jitu Optimasi Kecepatan Website</a></li>
                    <li><a href="#">Mengenal Algoritma Terbaru Mesin Pencari</a></li>
                </ul>
            </div>

            <!-- Latest Articles -->
            <div class="widget neu-card">
                <h3>Artikel Terbaru</h3>
                <ul>
                    <li><a href="#">{title}</a></li>
                    <li><a href="#">Update Fitur Kalkulator Zakat & Waktu Salat</a></li>
                    <li><a href="#">Panduan Keamanan Domain & SSL</a></li>
                </ul>
            </div>

            <!-- Oldest Articles -->
            <div class="widget neu-card">
                <h3>Artikel Terlama</h3>
                <ul>
                    <li><a href="#">Arsip Pertama FastSong Tahun 2024</a></li>
                    <li><a href="#">Sejarah Awal Pembuatan Portal Tools</a></li>
                </ul>
            </div>

            <!-- Category Archive Label -->
            <div class="widget neu-card">
                <h3>Kategori & Arsip</h3>
                <ul>
                    <li><a href="{DOMAIN_NAME}/{category}/">{category.capitalize()} (Arsip)</a></li>
                    <li><a href="{DOMAIN_NAME}/blog.html">Semua Label</a></li>
                </ul>
            </div>
        </aside>
    </main>

    <!-- Footer -->
    <footer class="neu-footer">
        <div class="container">
            <p>&copy; 2026 FastSong.eu.org. Hak Cipta Dilindungi Undang-Undang.</p>
        </div>
    </footer>
</body>
</html>
"""

def create_structure():
    print("Memulai pembuatan struktur folder dan file untuk FastSong...")

    # 1. Membuat file root utama
    for file_name in DIRECTORIES["root_files"]:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"<!-- {file_name} for FastSong -->\n")
    
    # 2. Membuat kategori standar (tanpa 30 artikel, cukup sitemap & index kategori)
    for cat in DIRECTORIES["categories"]:
        os.makedirs(cat, exist_ok=True)
        # Buat index kategori dan sitemap lokal
        for sub_file in ["index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"]:
            with open(os.path.join(cat, sub_file), "w", encoding="utf-8") as f:
                f.write(f"<!-- {cat}/{sub_file} -->\n")

    # 3. Membuat folder khusus: 'aplikasi' (berisi 30 artikel + sitemaps)
    app_dir = "aplikasi"
    os.makedirs(app_dir, exist_ok=True)
    for i in range(1, 31):
        filename = f"artikel{i}.html"
        file_path = os.path.join(app_dir, filename)
        content = get_article_template(f"Aplikasi Artikel {i}", "aplikasi", filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    for sub_file in ["index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"]:
        with open(os.path.join(app_dir, sub_file), "w", encoding="utf-8") as f:
            f.write(f"<!-- {app_dir}/{sub_file} -->\n")

    # 4. Membuat folder 'market' dan subkategorinya
    for sub_cat in DIRECTORIES["special_folders"]["market"]:
        dir_path = os.path.join("market", sub_cat)
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(f"<!-- Market: {sub_cat} -->\n")

    # 5. Membuat folder 'islamic' dan subkategorinya
    for sub_cat in DIRECTORIES["special_folders"]["islamic"]:
        dir_path = os.path.join("islamic", sub_cat)
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(f"<!-- Islamic: {sub_cat} -->\n")

    # 6. Membuat folder 'assets' (css, js, images)
    for asset_sub in DIRECTORIES["special_folders"]["assets"]:
        os.makedirs(os.path.join("assets", asset_sub), exist_ok=True)

    print("Struktur direktori dan file berhasil dibuat dengan sukses!")

if __name__ == "__main__":
    create_structure()
