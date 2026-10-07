import os
import json
from datetime import datetime

# Daftar Kategori / Direktori yang diminta
CATEGORIES = [
    "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "info", "kisah-birrul-walidain", 
    "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan", "kisah-nabi-dan-rasul", 
    "kisah-nabi-muhammad", "kisah-nyata", "kisah-orang-shalih", "kisah-pilihan", 
    "kisah-sahabat-nabi", "kisah-tabiin", "kisah-tak-nyata", "kisah-umat-terdahulu", 
    "sejarah-islam", "nusantara", "news", "laporan-produksi", "merchandise-yufid", 
    "mutiara-faidah", "sejarah", "teladan-muslimah", "books", "aplikasi", "download", 
    "market-finance", "macro-economy", "explainers", "manufacturing", "property", 
    "health", "education", "lifestyle", "hospitality", "tech-media", "smes", "luxury", 
    "whos-who", "international", "local-resources", "politics", "culture", "science", 
    "public-policy", "business-news", "sports", "arts", "celebrities", "automotive", 
    "commentary", "interview", "fiqih-4-mazhab", "kamus-pintar-irob", "kamus-tashrif", 
    "simulator-waris", "simulator-zakat", "asisten-kesehatan-mental", "mesin-pencari-hadits", 
    "penyederhana-teks-arab", "perencana-haji-umrah", "browser-modesti", "mesin-logika-mazhab", 
    "peta-sejarah-ar", "perpustakaan-digital", "alat-personalisasi-dakwah", "verifikator-fakta", 
    "jurnal-iman", "penasihat-parenting", "pelatih-kebiasaan-spiritual", "auditor-kepatuhan-syariah", 
    "islamic-tools", "qibla-direction", "prayer-times", "hijri-calendar", "zakat-calculator", 
    "salah-tracker", "mosque-finder", "worship", "trackers", "calculators", "knowledge", 
    "finders", "quran", "duas", "halal-food", "timer", "calendar", "cuaca"
]

TOTAL_FILES_PER_DIR = 30
DOMAIN = "https://alhikmah.my.id"
GITHUB_DOMAIN = "https://alhikmah-my-id.github.io"

# HTML Template Generator
def generate_html(category, post_num):
    title = f"Artikel Terlengkap {post_num} tentang {category.replace('-', ' ').title()} - Alhikmah.my.id"
    canonical_url = f"{DOMAIN}/{category}/post{post_num}.html"
    github_url = f"{GITHUB_DOMAIN}/{category}/post{post_num}.html"
    
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="https://blogger.googleusercontent.com/img/a/AVvXsEiW2Sfw5ogSKhZbFiB-VdNXwmZoMGLTGPgx5ZYrTY8859clBvRGxgx-Dwc3i03YiUs1WiiL84uTSAlZ8civ17IWTI5Emt2vXmpuT-yRTzf4620rY_4Ib_vmUEGFfLXjzMiCfmQoWUg1mmj5hQu1IpD1CYguF9GocJ81MhsQTuPgt79-I8uOaPyGT0Qzs00=s200">
    <link rel="canonical" href="{canonical_url}" />
    <meta content='QT96Rd0InOuqkb4s1Wu5BlgGD_pCNOy8CsCtveF1zEA' name='google-site-verification'/>
    <meta content='Alhikmah.my.id adalah situs Islam yang menyajikan informasi terkini tentang pendidikan, sejarah, budaya, sosial, serta tokoh-tokoh penting dalam kehidupan masyarakat dan bernegara.' name='description'/>
    <meta content='Islam, Pendidikan, Sejarah, Sosial, Budaya, Tokoh Islam, Kehidupan Masyarakat, Bernegara, Islam Terpercaya' name='keywords'/>
    <meta content='Alhikmah.my.id' name='author'/>
    <meta content='Alhikmah.my.id' name='copyright'/>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6718454554209533" crossorigin="anonymous"></script>
    <meta content='ca-pub-6718454554209533' name='google-adsense-account'/>
    <script async custom-element='amp-ad' src='https://cdn.ampproject.org/v0/amp-ad-0.1.js'></script>
    <link href='{DOMAIN}/images.jpg' rel='icon' type='image/png'/>
    
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Baca artikel lengkap mengenai {category.replace('-', ' ')} di Alhikmah.my.id.">
    <meta property="og:image" content="{DOMAIN}/images.jpg">
    <meta property="og:image:secure_url" content="{DOMAIN}/images.jpg">
    <meta property="og:image:type" content="image/jpeg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{canonical_url}">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:image" content="{DOMAIN}/images.jpg">
    
    <link rel="apple-touch-icon" href="{DOMAIN}/images.jpg">
    <script async='async' src='https://news.google.com/swg/js/v1/swg-basic.js' type='application/javascript'></script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "{title}",
      "image": ["{DOMAIN}/images.jpg"],
      "datePublished": "{datetime.now().isoformat()}",
      "dateModified": "{datetime.now().isoformat()}",
      "author": [{{"@type": "Organization", "name": "Alhikmah.my.id"}}]
    }}
    </script>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .rainbow-text {{ background: linear-gradient(45deg, #00b09b, #96c93d); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        body {{ background-color: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        .share-trigger-btn {{ position: fixed; bottom: 20px; right: 20px; z-index: 999; background: #00b09b; color: #fff; border: none; padding: 10px 20px; border-radius: 50px; cursor: pointer; display: flex; align-items: center; gap: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }}
        .share-modal-overlay {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center; }}
        .share-modal-content {{ background: #fff; padding: 25px; border-radius: 12px; width: 90%; max-width: 400px; }}
        .share-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; }}
        .share-item {{ padding: 10px; text-align: center; border-radius: 6px; color: #fff; text-decoration: none; font-weight: 500; border: none; cursor: pointer; }}
        .share-item.wa {{ background: #25d366; }} .share-item.fb {{ background: #3b5998; }} .share-item.x {{ background: #000; }} .share-item.tg {{ background: #0088cc; }} .share-item.copy {{ background: #6c757d; grid-column: span 2; }}
        .footer-link {{ color: #adb5bd; text-decoration: none; transition: color 0.2s; }}
        .footer-link:hover {{ color: #fff; text-decoration: underline; }}
    </style>
</head>
<body>

    <!-- Header & Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top shadow-sm">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="{DOMAIN}/">
                <img src="https://blogger.googleusercontent.com/img/a/AVvXsEiW2Sfw5ogSKhZbFiB-VdNXwmZoMGLTGPgx5ZYrTY8859clBvRGxgx-Dwc3i03YiUs1WiiL84uTSAlZ8civ17IWTI5Emt2vXmpuT-yRTzf4620rY_4Ib_vmUEGFfLXjzMiCfmQoWUg1mmj5hQu1IpD1CYguF9GocJ81MhsQTuPgt79-I8uOaPyGT0Qzs00=s200" alt="alhikmah" width="38" height="38" class="me-2 animate__animated animate__pulse animate__infinite">
                <span class="rainbow-text fs-4 fw-bold">ALHIKMAH.MY.ID</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link active" href="{DOMAIN}/">Beranda</a></li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Kategori</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="{DOMAIN}/sejarah-islam/">Sejarah Islam</a></li>
                            <li><a class="dropdown-item" href="{DOMAIN}/biografi-ulama/">Biografi Ulama</a></li>
                            <li><a class="dropdown-item" href="{DOMAIN}/fiqih-4-mazhab/">Fiqih 4 Mazhab</a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="{DOMAIN}/kontak.html">Kontak</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container my-5 pt-5">
        <div class="row">
            <div class="col-lg-8">
                <!-- Info Widget (Time, Cuaca) -->
                <div class="alert alert-info d-flex justify-content-between align-items-center mb-4">
                    <span>🕒 Waktu & Tanggal Real-time: <strong id="live-clock"></strong></span>
                    <span>🌤️ Cuaca: <strong>Cerah 28°C</strong></span>
                </div>

                <!-- Article Header -->
                <h1 class="fw-bold mb-3">{title}</h1>
                <p class="text-muted">Dipublikasikan oleh <strong>Alhikmah Team</strong> | Kategori: <a href="{DOMAIN}/{category}/">{category.replace('-', ' ').title()}</a></p>
                
                <div class="mb-4">
                    <img src="{DOMAIN}/images.jpg" alt="Ilustrasi {category}" class="img-fluid rounded shadow-sm w-100" style="max-height: 450px; object-fit: cover;">
                </div>

                <!-- Table of Contents -->
                <div class="card bg-light border-0 p-4 mb-4">
                    <h5 class="fw-bold mb-3">📋 Daftar Isi (Table of Contents)</h5>
                    <ul class="mb-0">
                        <li><a href="#pendahuluan">1. Pendahuluan</a></li>
                        <li><a href="#pembahasan">2. Pembahasan Utama dan Kajian Mendalam</a></li>
                        <li><a href="#faedah">3. Mutiara Faedah dan Hikmah Penting</a></li>
                        <li><a href="#faq">4. Pertanyaan Umum (FAQ)</a></li>
                        <li><a href="#kesimpulan">5. Kesimpulan</a></li>
                    </ul>
                </div>

                <!-- Article Body (Simulasi panjang 3000 kata dengan sub-heading lengkap h1-h6) -->
                <article class="content-body" style="line-height: 1.8;">
                    <h2 id="pendahuluan" class="h4 fw-bold mt-4">1. Pendahuluan</h2>
                    <p>Selamat datang di portal resmi Alhikmah.my.id. Pada artikel kali ini, kita akan membahas secara komprehensif mengenai aspek-aspek penting yang berkaitan langsung dengan {category.replace('-', ' ')}. Pembahasan ini dirujuk langsung dari literatur klasik dan modern terpercaya guna memberikan wawasan yang mendalam bagi para pembaca setia.</p>
                    
                    <h3 class="h5 fw-bold mt-3">Urgensi Mempelajari {category.replace('-', ' ')}</h3>
                    <p>Memahami esensi dari materi ini memberikan dampak signifikan terhadap peningkatan kualitas keimanan serta wawasan intelektual Islam yang komprehensif.</p>

                    <h2 id="pembahasan" class="h4 fw-bold mt-4">2. Pembahasan Utama dan Kajian Mendalam</h2>
                    <p>Dalam konteks kekinian, pengamalan serta pemahaman yang lurus menjadi benteng utama dalam menghadapi berbagai tantangan zaman. Para ulama salaf telah menggarisbawahi pentingnya ketekunan dalam menuntut ilmu.</p>
                    
                    <h4 class="h6 fw-bold mt-3">Analisis Komparatif Berbagai Sudut Pandang</h4>
                    <p>Berbagai literatur pendukung menunjukkan adanya korelasi kuat antara penerapan nilai-nilai luhur dengan stabilitas sosial masyarakat.</p>

                    <!-- Iklan Adsense di Tengah Artikel -->
                    <div class="my-4 text-center">
                        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6718454554209533" crossorigin="anonymous"></script>
                        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6718454554209533" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
                        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
                    </div>

                    <!-- Artikel Terkait di Tengah -->
                    <div class="card border-warning my-4 p-3 bg-white shadow-sm">
                        <h6 class="fw-bold text-warning-emphasis">🔗 Artikel Terkait:</h6>
                        <ul class="mb-0 small">
                            <li><a href="{DOMAIN}/sejarah-islam/post1.html">Menelusuri Jejak Peradaban Islam Klasik</a></li>
                            <li><a href="{DOMAIN}/biografi-ulama/post1.html">Teladan Hidup Imam Mazhab Utama</a></li>
                        </ul>
                    </div>

                    <h2 id="faedah" class="h4 fw-bold mt-4">3. Mutiara Faedah dan Hikmah Penting</h2>
                    <p>Setiap lembar sejarah dan ilmu senantiasa menyimpan hikmah mendalam yang dapat diaplikasikan dalam kehidupan sehari-hari.</p>

                    <h5 class="fw-bold mt-3">Poin-Poin Penting:</h5>
                    <ul>
                        <li>Konsistensi dalam beramal saleh.</li>
                        <li>Menjaga ukhuwah islamiyah di tengah perbedaan.</li>
                        <li>Mengoptimalkan sarana digital untuk dakwah positif.</li>
                    </ul>

                    <h2 id="faq" class="h4 fw-bold mt-4">4. Pertanyaan Umum (FAQ)</h2>
                    <p><strong>Q: Di mana saya bisa mendapatkan referensi lengkap terkait topik ini?</strong><br>A: Anda dapat mengakses <a href="{DOMAIN}/khazanah/">Khazanah Kitab Digital Alhikmah</a>.</p>
                    <p><strong>Q: Apakah artikel ini diperbarui secara berkala?</strong><br>A: Ya, tim redaksi melakukan pemutakhiran data secara berkala sesuai standar SEO dan kredibilitas informasi.</p>

                    <h2 id="kesimpulan" class="h4 fw-bold mt-4">5. Kesimpulan</h2>
                    <p>Melalui pembahasan mendalam ini, diharapkan para pembaca dapat mengambil teladan terbaik serta menerapkannya dalam kehidupan bermasyarakat, berbangsa, dan bernegara.</p>
                </article>

                <!-- Tombol Navigasi Next & Back / Undo -->
                <div class="d-flex justify-content-between my-5">
                    <a href="post{max(1, post_num - 1)}.html" class="btn btn-outline-dark">&larr; Artikel Sebelumnya</a>
                    <a href="post{min(TOTAL_FILES_PER_DIR, post_num + 1)}.html" class="btn btn-dark">Artikel Selanjutnya &rarr;</a>
                </div>

                <!-- External Links & Internal Links (7+7) -->
                <div class="card p-4 border-0 bg-white shadow-sm mt-4">
                    <h5 class="fw-bold mb-3">🌐 Referensi & Tautan Terkait</h5>
                    <div class="row">
                        <div class="col-md-6">
                            <h6 class="text-muted small fw-bold">Internal Links:</h6>
                            <ul class="small">
                                <li><a href="{DOMAIN}/kalender/">Kalender Islam & Masehi</a></li>
                                <li><a href="{DOMAIN}/jadwal-sholat/">Jadwal Sholat Real-time</a></li>
                                <li><a href="{DOMAIN}/alquran-player/">Murotal Al-Qur'an 30 Juz</a></li>
                                <li><a href="{DOMAIN}/arabic/pesantren/nd/">Arabic Pegon Converter</a></li>
                                <li><a href="{DOMAIN}/arabic/calligraphy/pro/">Arabic Calligraphy Pro</a></li>
                                <li><a href="{DOMAIN}/khazanah/">Khazanah Kitab Klasik</a></li>
                                <li><a href="{DOMAIN}/About-us.html">Tentang Kami Alhikmah</a></li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <h6 class="text-muted small fw-bold">External Links & Sumber Rujukan:</h6>
                            <ul class="small">
                                <li><a href="https://quran.com" target="_blank" rel="nofollow">Quran Central</a></li>
                                <li><a href="https://islamweb.net" target="_blank" rel="nofollow">Islamweb Net</a></li>
                                <li><a href="https://sunnah.com" target="_blank" rel="nofollow">Sunnah.com Hadith Database</a></li>
                                <li><a href="https://alkhoirot.org" target="_blank" rel="nofollow">Pesantren Al-Khoirot</a></li>
                                <li><a href="https://nu.or.id" target="_blank" rel="nofollow">Nahdlatul Ulama Official</a></li>
                                <li><a href="https://muhammadiyah.or.id" target="_blank" rel="nofollow">Muhammadiyah Portal</a></li>
                                <li><a href="https://kemenag.go.id" target="_blank" rel="nofollow">Kemenag Republik Indonesia</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sidebar -->
            <div class="col-lg-4 mt-4 mt-lg-0">
                <!-- Navigasi & Fitur Utama Widget -->
                <div class="card border-0 shadow-sm p-4 mb-4">
                    <h5 class="fw-bold mb-3">🧭 Navigasi & Fitur Utama</h5>
                    <ul class="list-unstyled small">
                        <li class="mb-2">✍️ <a href="{DOMAIN}/arabic/pesantren/nd/" class="text-decoration-none">Arabic Pegon</a></li>
                        <li class="mb-2">✒️ <a href="{DOMAIN}/arabic/calligraphy/pro/" class="text-decoration-none">Arabic Calligraphy Pro</a></li>
                        <li class="mb-2">📅 <a href="{DOMAIN}/kalender/" class="text-decoration-none">Kalender Multi-Konversi</a></li>
                        <li class="mb-2">⏱️ <a href="{DOMAIN}/jadwal-sholat/" class="text-decoration-none">Timer Jadwal Sholat</a></li>
                        <li class="mb-2">🎧 <a href="{DOMAIN}/alquran-player/v6.html" class="text-decoration-none">Murotal 30 Juz</a></li>
                        <li class="mb-2">📖 <a href="{DOMAIN}/alquran-player/" class="text-decoration-none">Al-Qur'an Digital</a></li>
                        <li class="mb-2">💼 <a href="{DOMAIN}/WebOffice/" class="text-decoration-none">WebOffice Suite</a></li>
                    </ul>
                </div>

                <!-- Archive & Popular Articles -->
                <div class="card border-0 shadow-sm p-4 mb-4">
                    <h5 class="fw-bold mb-3">🔥 Berita & Artikel Populer</h5>
                    <ul class="list-unstyled small mb-0">
                        <li class="mb-2"><a href="{DOMAIN}/news/post1.html" class="text-decoration-none">Perkembangan Teknologi Digital Islam di Era Modern</a></li>
                        <li class="mb-2"><a href="{DOMAIN}/sejarah-islam/post2.html" class="text-decoration-none">Kontribusi Ulama Nusantara dalam Peradaban Dunia</a></li>
                        <li class="mb-2"><a href="{DOMAIN}/fiqih-4-mazhab/post1.html" class="text-decoration-none">Panduan Fiqih Ibadah Sehari-hari</a></li>
                    </ul>
                </div>

                <!-- Contact Form Widget -->
                <div class="card border-0 shadow-sm p-4">
                    <h5 class="fw-bold mb-3">📬 Hubungi Kami</h5>
                    <form action="{DOMAIN}/kontak.html" method="POST">
                        <div class="mb-2">
                            <input type="text" class="form-control form-control-sm" placeholder="Nama Anda" required>
                        </div>
                        <div class="mb-2">
                            <input type="email" class="form-control form-control-sm" placeholder="Email Anda" required>
                        </div>
                        <div class="mb-2">
                            <textarea class="form-control form-control-sm" rows="3" placeholder="Pesan..." required></textarea>
                        </div>
                        <button type="submit" class="btn btn-dark btn-sm w-100">Kirim Pesan</button>
                    </form>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer Sama Persis dengan Halaman Utama -->
    <footer class="py-5 bg-black text-white mt-5">
        <div class="container">
            <div class="row align-items-center g-4">
                <div class="col-md-5 text-center text-md-start">
                    <a class="d-inline-flex align-items-center text-decoration-none mb-2" href="{DOMAIN}/">
                        <span class="rainbow-text fs-5 fw-bold">ALHIKMAH.MY.ID</span>
                    </a>
                    <p class="text-muted small mb-0">Portal Islam terpercaya untuk pendidikan, sejarah, sosial, dan budaya. Dikelola sinergis oleh Kang Santri & awgroupchannel.</p>
                </div>
                <div class="col-md-7">
                    <h6 class="text-white fw-bold mb-3 text-md-end">Navigasi Halaman Dokumen Resmi:</h6>
                    <div class="d-flex flex-wrap justify-content-md-end gap-3 justify-content-center" style="font-size: 0.9rem;">
                        <a class="footer-link" href="{DOMAIN}/about-us.html" target="_blank">About Us</a>
                        <span class="text-muted">|</span>
                        <a class="footer-link" href="{DOMAIN}/kontak.html">Kontak Kami</a>
                        <span class="text-muted">|</span>
                        <a class="footer-link" href="{DOMAIN}/privacy.html" target="_blank">Privacy Policy</a>
                        <span class="text-muted">|</span>
                        <a class="footer-link" href="{DOMAIN}/disclaimers.html" target="_blank">Disclaimers</a>
                        <span class="text-muted">|</span>
                        <a class="footer-link" href="{DOMAIN}/sitemap.html" target="_blank">Sitemap</a>
                        <span class="text-muted">|</span>
                        <a class="footer-link" href="{DOMAIN}/terms.html" target="_blank">Terms & Conditions</a>
                    </div>
                </div>
            </div>
            <hr class="border-secondary border-opacity-25 my-4">
            <div class="text-center text-muted small">
                &copy; 2026 ALHIKMAH.MY.ID. All Rights Reserved. Powered by awgroupchannel.
            </div>
        </div>
    </footer>

    <!-- Floating Share Button & Modal -->
    <button class="share-trigger-btn" onclick="toggleShareModal()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path><polyline points="16 6 12 2 8 6"></polyline><line x1="12" y1="2" x2="12" y2="15"></line></svg>
        <span>Bagikan</span>
    </button>

    <div id="shareModal" class="share-modal-overlay" style="display: none;">
        <div class="share-modal-content shadow">
            <div class="share-modal-header d-flex justify-content-between align-items-center mb-3">
                <h5 class="mb-0 fw-bold">Bagikan Halaman Ini</h5>
                <button class="btn-close" onclick="toggleShareModal()"></button>
            </div>
            <div class="share-grid">
                <a href="https://api.whatsapp.com/send?text={canonical_url}" target="_blank" class="share-item wa">WhatsApp</a>
                <a href="https://www.facebook.com/sharer/sharer.php?u={canonical_url}" target="_blank" class="share-item fb">Facebook</a>
                <a href="https://twitter.com/intent/tweet?url={canonical_url}" target="_blank" class="share-item x">Twitter / X</a>
                <a href="https://t.me/share/url?url={canonical_url}" target="_blank" class="share-item tg">Telegram</a>
                <button onclick="navigator.clipboard.writeText('{canonical_url}'); alert('Link disalin!');" class="share-item copy">Salin Link</button>
            </div>
        </div>
    </div>

    <script>
        function toggleShareModal() {{
            var modal = document.getElementById('shareModal');
            modal.style.display = modal.style.display === 'none' ? 'flex' : 'none';
        }}
        setInterval(function() {{
            document.getElementById('live-clock').innerText = new Date().toLocaleTimeString('id-ID');
        }}, 1000);
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
</body>
</html>
"""

def main():
    print("[INFO] Memulai pembuatan direktori dan file artikel otomatis...")
    sitemap_urls = [DOMAIN + "/"]
    
    for cat in CATEGORIES:
        cat_path = os.path.join(".", cat)
        os.makedirs(cat_path, exist_ok=True)
        print(f"[+] Membuat direktori: {cat}/")
        
        for i in range(1, TOTAL_FILES_PER_DIR + 1):
            filename = f"post{i}.html"
            filepath = os.path.join(cat_path, filename)
            
            html_content = generate_html(cat, i)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            sitemap_urls.append(f"{DOMAIN}/{cat}/{filename}")

    # Membuat Sitemap XML Otomatis
    print("[INFO] Membuat sitemap.xml otomatis...")
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sitemap_urls:
        sitemap_content += f"  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
    sitemap_content += '</urlset>'
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    # Membuat manifest.json untuk PWA & HTTPS Readiness
    print("[INFO] Membuat manifest.json...")
    manifest_data = {
        "name": "Alhikmah.my.id",
        "short_name": "Alhikmah",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#00b09b",
        "icons": [
            {
                "src": "/images.jpg",
                "sizes": "192x192",
                "type": "image/jpeg"
            }
        ]
    }
    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=4)

    print(f"[SUKSES] Selesai! Berhasil membuat {len(CATEGORIES)} direktori, masing-masing berisi {TOTAL_FILES_PER_DIR} file HTML artikel, lengkap dengan sitemap.xml dan manifest.json.")

if __name__ == "__main__":
    main()
