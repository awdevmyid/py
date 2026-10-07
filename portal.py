import os
import datetime

# Konfigurasi Dasar
DOMAIN = "https://waumkm.xyz"
SITE_NAME = "WAUMKM - Portal Informasi, UMKM, Teknologi & Islami"
CURRENT_YEAR = datetime.datetime.now().year

# Daftar direktori utama
DIRECTORIES = [
    # Kategori Utama / Tools
    "calligraphy", "code", "collor", "converter", "devoloper", "domain", "domains", 
    "eq", "finder", "hook", "img", "ip", "kodepost", "link", "maps", "pdf", "qr", 
    "quran", "removebg", "safelink", "search", "seo", "source", "text", "tools", 
    "utilities", "vidio",
    
    # Sub-direktori Aplikasi
    "aplikasi",
    
    # Kategori Market / Bisnis
    "market/finance", "market/macro", "market/micro", "market/economy", "market/explainers", 
    "market/manufacturing", "market/property", "market/health", "market/education", 
    "market/lifestyle", "market/hospitality", "market/tech", "market/media", "market/smes", 
    "market/luxury", "market/whos-who", "market/international", "market/local-resources",
    
    # Kategori Islamic
    "islamic/biografi-ulama", "islamic/kisah-hikmah", "islamic/kisah-sejarah", 
    "islamic/kisah-birrul-walidain", "islamic/kisah-hidayah-islam", "islamic/kisah-kaum-durhaka", 
    "islamic/kisah-masa-depan", "islamic/kisah-nabi-dan-rasul", "islamic/kisah-nabi-muhammad", 
    "islamic/kisah-nyata", "islamic/kisah-orang-shalih", "islamic/kisah-pilihan", 
    "islamic/kisah-sahabat-nabi", "islamic/kisah-tabiin", "islamic/sejarah-islam", "islamic/nusantara",
    
    # Assets
    "assets/css", "assets/js", "assets/images"
]

# Template CSS Global (Neumorphism & Responsive)
GLOBAL_CSS = """
:root {
    --bg-color: #e4ebf5;
    --text-color: #31344b;
    --primary: #6d5dfc;
    --shadow-light: #ffffff;
    --shadow-dark: #c8d0e7;
}
body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
}
.neu-box {
    background: var(--bg-color);
    box-shadow: 6px 6px 12px var(--shadow-dark), -6px -6px 12px var(--shadow-light);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
.neu-button {
    background: var(--bg-color);
    box-shadow: 4px 4px 8px var(--shadow-dark), -4px -4px 8px var(--shadow-light);
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    color: var(--primary);
    cursor: pointer;
    font-weight: bold;
}
.neu-button:active {
    box-shadow: inset 3px 3px 6px var(--shadow-dark), inset -3px -3px 6px var(--shadow-light);
}
header, footer {
    background: var(--bg-color);
    box-shadow: 0 4px 10px var(--shadow-dark);
    padding: 15px 30px;
    text-align: center;
}
.container {
    max-width: 1200px;
    margin: 20px auto;
    padding: 0 15px;
}
.flex-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
.main-content {
    flex: 3;
}
.sidebar {
    flex: 1;
}
@media (max-width: 768px) {
    .flex-grid { flex-direction: column; }
}
"""

def generate_html_template(title, desc, canonical, category, article_num=""):
    """Template HTML Terpusat untuk Artikel dan Halaman Utama"""
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{canonical}">
    
    <!-- Open Graph / Social -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
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
      "author": {{ "@type": "Organization", "name": "WAUMKM" }},
      "publisher": {{ "@type": "Organization", "name": "WAUMKM", "logo": {{ "@type": "ImageObject", "url": "{DOMAIN}/assets/images/logo.png" }} }},
      "mainEntityOfPage": "{canonical}"
    }}
    </script>
    
    <link rel="stylesheet" href="{DOMAIN}/assets/css/style.css">
</head>
<body>

    <!-- Header / Navbar -->
    <header class="neu-box">
        <h1><a href="{DOMAIN}/" style="text-decoration:none; color:inherit;">WAUMKM.XYZ</a></h1>
        <nav>
            <a href="{DOMAIN}/" class="neu-button">Home</a>
            <a href="{DOMAIN}/blog.html" class="neu-button">Blog</a>
            <a href="{DOMAIN}/market/economy/" class="neu-button">Market</a>
            <a href="{DOMAIN}/islamic/nusantara/" class="neu-button">Islamic</a>
            <a href="{DOMAIN}/tools/" class="neu-button">Tools</a>
        </nav>
    </header>

    <div class="container">
        <!-- Breadcrumb -->
        <div class="neu-box" style="padding: 10px 20px; font-size: 14px;">
            <a href="{DOMAIN}/">Home</a> &raquo; <a href="#">{category}</a> &raquo; <span>{title}</span>
        </div>

        <div class="flex-grid">
            <!-- Main Content Area -->
            <main class="main-content">
                <article class="neu-box">
                    <h1>{title} {article_num}</h1>
                    <p><em>Dipublikasikan pada {CURRENT_YEAR} oleh Tim Redaksi WAUMKM</em></p>
                    
                    <!-- Featured Image -->
                    <img src="{DOMAIN}/assets/images/featured.jpg" alt="{title}" style="width:100%; height:auto; border-radius:8px; margin-bottom:15px;">
                    
                    <!-- Table of Contents -->
                    <div class="neu-box" style="background: rgba(0,0,0,0.02);">
                        <h3>Daftar Isi</h3>
                        <ul>
                            <li><a href="#pengantar">1. Pengantar</a></li>
                            <li><a href="#pembahasan">2. Pembahasan Utama</a></li>
                            <li><a href="#tabel-info">3. Ringkasan Informasi</a></li>
                            <li><a href="#faq">4. Pertanyaan Umum (FAQ)</a></li>
                            <li><a href="#kesimpulan">5. Kesimpulan</a></li>
                        </ul>
                    </div>

                    <h2 id="pengantar">1. Pengantar</h2>
                    <p>{desc} Artikel ini membahas secara mendalam mengenai berbagai aspek penting yang berkaitan dengan kebutuhan Anda secara komprehensif.</p>
                    
                    <!-- Adsense Slot 1 -->
                    <div class="neu-box" style="text-align:center; background:#dfebf6;">
                        <small>[ Iklan Google Adsense ]</small>
                    </div>

                    <h2 id="pembahasan">2. Pembahasan Utama</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elemen-elemen penting dalam topik ini dijabarkan dengan pendekatan praktis agar mudah dipahami.</p>
                    <h3>Sub-Pembahasan Spesifik</h3>
                    <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

                    <!-- Tabel Informasi -->
                    <h3 id="tabel-info">3. Ringkasan Informasi</h3>
                    <table style="width:100%; border-collapse: collapse; margin: 15px 0;">
                        <tr style="border-bottom: 2px solid #ccc;">
                            <th style="text-align:left; padding:8px;">Parameter</th>
                            <th style="text-align:left; padding:8px;">Keterangan</th>
                        </tr>
                        <tr>
                            <td style="padding:8px; border-bottom: 1px solid #ddd;">Kategori</td>
                            <td style="padding:8px; border-bottom: 1px solid #ddd;">{category}</td>
                        </tr>
                        <tr>
                            <td style="padding:8px; border-bottom: 1px solid #ddd;">Pembaruan</td>
                            <td style="padding:8px; border-bottom: 1px solid #ddd;">{CURRENT_YEAR}</td>
                        </tr>
                    </table>

                    <!-- FAQ Section -->
                    <h2 id="faq">4. Pertanyaan Umum (FAQ)</h2>
                    <div class="neu-box">
                        <strong>Q: Apakah informasi ini gratis?</strong>
                        <p>A: Ya, seluruh informasi dan tools di waumkm.xyz dapat diakses secara gratis.</p>
                    </div>

                    <h2 id="kesimpulan">5. Kesimpulan</h2>
                    <p id="kesimpulan">Dengan memahami panduan ini, diharapkan pembaca dapat mengoptimalkan strategi dan kebutuhan digital mereka secara maksimal.</p>

                    <!-- Social Sharing -->
                    <div style="margin: 20px 0;">
                        <strong>Bagikan Artikel:</strong>
                        <button class="neu-button">Facebook</button>
                        <button class="neu-button">Twitter</button>
                        <button class="neu-button">WhatsApp</button>
                    </div>

                    <!-- Internal Links & External References -->
                    <hr>
                    <h4>Internal Links:</h4>
                    <ul>
                        <li><a href="{DOMAIN}/aplikasi/">Aplikasi & Tools Utama</a></li>
                        <li><a href="{DOMAIN}/market/economy/">Analisis Ekonomi & Pasar</a></li>
                        <li><a href="{DOMAIN}/islamic/nusantara/">Sejarah & Nusantara</a></li>
                        <li><a href="{DOMAIN}/tools/">Koleksi Tools Praktis</a></li>
                        <li><a href="{DOMAIN}/blog.html">Blog & Artikel Terbaru</a></li>
                        <li><a href="{DOMAIN}/sitemap.html">Peta Situs Lengkap</a></li>
                        <li><a href="{DOMAIN}/pdf/">PDF Converter Tool</a></li>
                    </ul>

                    <h4>Referensi Eksternal:</h4>
                    <ul>
                        <li><a href="https://www.google.com" target="_blank" rel="nofollow">Google Resources</a></li>
                        <li><a href="https://developer.mozilla.org" target="_blank" rel="nofollow">MDN Web Docs</a></li>
                        <li><a href="https://github.com" target="_blank" rel="nofollow">GitHub Open Source</a></li>
                        <li><a href="https://stackoverflow.com" target="_blank" rel="nofollow">Stack Overflow Community</a></li>
                        <li><a href="https://wikipedia.org" target="_blank" rel="nofollow">Wikipedia ensiklopedia</a></li>
                        <li><a href="https://w3schools.com" target="_blank" rel="nofollow">W3Schools Tutorials</a></li>
                        <li><a href="https://archive.org" target="_blank" rel="nofollow">Internet Archive</a></li>
                    </ul>
                </article>

                <!-- Komentar Disqus -->
                <div class="neu-box">
                    <h3>Komentar</h3>
                    <div id="disqus_thread">[ Kolom Komentar Disqus / Diskusi Pembaca ]</div>
                </div>
            </main>

            <!-- Sidebar -->
            <aside class="sidebar">
                <div class="neu-box">
                    <h3>Artikel Populer</h3>
                    <ul>
                        <li><a href="#">Panduan Lengkap UMKM Digital {CURRENT_YEAR}</a></li>
                        <li><a href="#">Optimasi SEO On-Page Praktis</a></li>
                        <li><a href="#">Mengenal Tools Produktivitas Terbaik</a></li>
                    </ul>
                </div>
                <div class="neu-box">
                    <h3>Artikel Terbaru</h3>
                    <ul>
                        <li><a href="#">Update Tren Teknologi & Pasar</a></li>
                        <li><a href="#">Kisah Inspiratif Tokoh Islam Nusantara</a></li>
                        <li><a href="#">Review Aplikasi Web Terkini</a></li>
                    </ul>
                </div>
                <div class="neu-box">
                    <h3>Hubungi Kami</h3>
                    <p>Kirimkan saran atau pertanyaan melalui <a href="{DOMAIN}/contact.html">Form Kontak</a>.</p>
                </div>
            </aside>
        </div>
    </div>

    <!-- Footer -->
    <footer class="neu-box">
        <p>&copy; {CURRENT_YEAR} <a href="{DOMAIN}" style="text-decoration:none;">WAUMKM.XYZ</a>. Hak Cipta Dilindungi Undang-Undang.</p>
    </footer>

</body>
</html>
"""

def create_structure():
    print("Memulai pembuatan struktur direktori dan file waumkm.xyz...")
    
    # Buat direktori utama
    os.makedirs("assets/css", exist_ok=True)
    os.makedirs("assets/js", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)
    
    for d in DIRECTORIES:
        os.makedirs(d, exist_ok=True)

    # 1. Buat File CSS Global
    with open("assets/css/style.css", "w", encoding="utf-8") as f:
        f.write(GLOBAL_CSS)

    # 2. Buat File Root Utama
    root_files = ["index.html", "blog.html", "sitemap.html", "sitemap.xml", "sitemap.txt", "robots.txt", "ads.txt", "manifest.json"]
    for rf in root_files:
        path = rf
        if rf.endswith(".html"):
            content = generate_html_template(f"Halaman {rf.replace('.html','').capitalize()} - WAUMKM", f"Informasi resmi halaman {rf} di WAUMKM.", f"{DOMAIN}/{rf}", "Utama")
        elif rf == "robots.txt":
            content = f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml"
        elif rf == "ads.txt":
            content = "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
        elif rf == "manifest.json":
            content = '{\n  "name": "WAUMKM",\n  "short_name": "WAUMKM",\n  "start_url": "/",\n  "display": "standalone"\n}'
        else:
            content = f"{DOMAIN}/{rf}"
            
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    # 3. Buat File dalam Direktori & Sub-direktori (termasuk 30 Artikel per kategori/sub-kategori)
    all_categories = DIRECTORIES.copy()
    all_categories.append("") # untuk root level jika diperlukan, tapi sudah dihandle terpisah

    for cat in DIRECTORIES:
        # File pendukung kategori
        cat_files = ["index.html", "sitemap.html", "sitemap.xml", "sitemap.txt"]
        for cf in cat_files:
            file_path = os.path.join(cat, cf)
            if cf == "index.html":
                title_cat = f"Kategori {cat.upper()} - WAUMKM"
                content = generate_html_template(title_cat, f"Kumpulan artikel dan informasi terbaik seputar {cat}.", f"{DOMAIN}/{cat}/", cat)
            else:
                content = f"Sitemap untuk {cat}"
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        # Buat artikel 1 sampai 30 di setiap kategori
        for i in range(1, 31):
            art_name = f"artikel{i}.html"
            art_path = os.path.join(cat, art_name)
            art_title = f"Artikel {i} Panduan Lengkap {cat.replace('/', ' ').title()}"
            art_desc = f"Pembahasan mendalam artikel {i} terkait {cat} terlengkap dan terupdate tahun {CURRENT_YEAR}."
            art_canonical = f"{DOMAIN}/{cat}/{art_name}"
            
            content = generate_html_template(art_title, art_desc, art_canonical, cat, f"#{i}")
            with open(art_path, "w", encoding="utf-8") as f:
                f.write(content)

    # 4. Pemisahan Logika JavaScript Khusus Islamic Tools & API Eksternal
    islamic_tools_js = """
// Logika JavaScript Terpisah untuk Islamic Tools, Cuaca, dan Lokasi
document.addEventListener("DOMContentLoaded", function() {
    console.log("Islamic Tools & API Integration Initialized.");
    
    // Contoh fungsi placeholder untuk Prayer Times / Qibla API
    window.fetchPrayerTimes = function(city) {
        // Fetch ke API waktu salat eksternal tanpa mengganggu statis HTML
        fetch(`https://api.aladhan.com/v1/timingsByCity?city=${city}&country=Indonesia&method=2`)
            .then(response => response.json())
            .then(data => {
                console.log("Prayer Times Data:", data);
            })
            .catch(error => console.error("Error fetching prayer times:", error));
    };
});
"""
    with open("assets/js/islamic-tools.js", "w", encoding="utf-8") as f:
        f.write(islamic_tools_js)

    print("Selesai! Seluruh struktur direktori dan ribuan file artikel berhasil dibuat otomatis.")

if __name__ == "__main__":
    create_structure()
