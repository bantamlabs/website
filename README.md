# bantamlabs.com

Static website for Bantam Labs LLC. Plain HTML and CSS: no framework, no build step, no JavaScript.

## Layout

```
index.html            Home page
404.html              Not-found page (GitHub Pages serves it automatically)
assets/css/site.css   All styles; colors are CSS variables at the top
assets/fonts/         Bebas Neue (headings only), self-hosted, SIL OFL (see OFL.txt)
assets/img/           Logo renditions (WebP), favicons, Open Graph image
brand/                Unmodified copies of logo 4a masters (944×1312 PNG)
favicon.ico           16/32/48 px icon for browsers that request /favicon.ico
robots.txt, sitemap.xml, CNAME, .nojekyll
```

## Preview locally

Pages use root-relative paths (`/assets/...`), so serve the repo root rather than opening the files directly:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. The dev server does not serve `404.html` for missing paths, so open <http://localhost:8000/404.html> to check that page.

Light and dark mode follow the OS setting. In Chrome DevTools you can switch them under **Rendering → Emulate CSS media feature prefers-color-scheme**.

## Adding a product

1. In `index.html`, find the Products section. Replace the `card-placeholder` item with one `<li class="card">` per product. A commented template is in the file.
2. For a product page, create `products/<slug>/index.html`. Copy the `<head>` from `404.html`, then set its title, description, canonical URL and Open Graph tags.
3. Add the new URL to `sitemap.xml`.

The card grid adapts on its own: one column on phones, and more as the width allows.

## Regenerating images

The images in `assets/img/` were made from `brand/` with ImageMagick and `cwebp`:

- **Logo:** trimmed to the artwork (836×1207 crop at +54+50), then exported as 360 px and 720 px wide WebP.
- **Favicons:** the hen only (crop 836×777 at +54+50), in off-white on a slate-blue (`#416180`) tile.
- **OG image:** the slate hen centered on a 1200×630 canvas filled with `#F2F2F3`.

## Publishing on GitHub Pages

1. Create a GitHub repository and push this repo's `main` branch to it.
2. Go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then branch `main`, folder `/ (root)`.
3. Under **Custom domain**, enter `bantamlabs.com` (the `CNAME` file already has it) and save.
4. After DNS resolves and GitHub issues the certificate, turn on **Enforce HTTPS**.
5. Recommended: verify the domain under your account or organization's **Settings → Pages → Verified domains**, so nobody else can claim it.

`.nojekyll` makes GitHub serve the files exactly as they are, with no Jekyll processing.

### DNS records

At your DNS provider:

| Type  | Host / Name | Value                   |
|-------|-------------|-------------------------|
| A     | `@`         | `185.199.108.153`       |
| A     | `@`         | `185.199.109.153`       |
| A     | `@`         | `185.199.110.153`       |
| A     | `@`         | `185.199.111.153`       |
| AAAA  | `@`         | `2606:50c0:8000::153`   |
| AAAA  | `@`         | `2606:50c0:8001::153`   |
| AAAA  | `@`         | `2606:50c0:8002::153`   |
| AAAA  | `@`         | `2606:50c0:8003::153`   |
| CNAME | `www`       | `<github-username-or-org>.github.io` |

Remove any other A, AAAA, or ALIAS records on `@`. With both the apex and `www` set up, GitHub redirects `www.bantamlabs.com` to `bantamlabs.com`. To check:

```sh
dig bantamlabs.com +noall +answer
dig www.bantamlabs.com +noall +answer
```

These IP addresses are listed in GitHub's documentation ("Managing a custom domain for your GitHub Pages site"). Check there before you configure DNS in case they have changed.
