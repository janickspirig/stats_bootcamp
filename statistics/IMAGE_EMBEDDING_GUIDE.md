# Image Embedding Guide for Statistics Bootcamp

> How to make images appear smoothly inline in Notion pages when publishing the bootcamp.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Option 1: GitHub Raw URLs (Current)](#option-1-github-raw-urls-current)
3. [Option 2: GitHub Pages Hosting](#option-2-github-pages-hosting)
4. [Option 3: Image CDN Services](#option-3-image-cdn-services)
5. [Option 4: Notion Native Upload via API](#option-4-notion-native-upload-via-api)
6. [Option 5: Self-Hosted / S3 Bucket](#option-5-self-hosted--s3-bucket)
7. [Comparison Matrix](#comparison-matrix)
8. [Recommended Approach](#recommended-approach)
9. [How It Works with publish_to_notion.py](#how-it-works-with-publish_to_notionpy)
10. [Troubleshooting](#troubleshooting)

---

## 1. Overview

### The Challenge

When publishing markdown files to Notion, images must be accessible via **public HTTP URLs**. Notion's API creates image blocks using the `external` type, which fetches images from the provided URL at render time.

```json
{
  "type": "image",
  "image": {
    "type": "external",
    "external": {
      "url": "https://example.com/image.png"
    }
  }
}
```

**Key requirements:**
- Images must be publicly accessible (no authentication)
- URLs should be stable and not expire
- Fast loading improves user experience
- Notion caches external images but re-fetches periodically

### Current State

- **45 images** generated in `statistics/final_bootcamp/images/`
- **40 markdown files** reference these images
- Images are now using GitHub raw URLs after running `update_image_urls.py`

---

## Option 1: GitHub Raw URLs (Current)

**Status: ✅ Already Implemented**

Images are served directly from GitHub's raw content endpoint.

### URL Format

```
https://raw.githubusercontent.com/{owner}/{repo}/{branch}/path/to/image.png
```

**Example:**
```
https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/normal_curve.png
```

### How to Set Up

```bash
# Already done - but for reference:
python3 statistics/tools/update_image_urls.py \
    --username janickspirig \
    --repo stats_bootcamp \
    --branch main
```

### Pros

| Advantage | Description |
|-----------|-------------|
| **Free** | No additional costs |
| **Simple** | No extra infrastructure needed |
| **Integrated** | Images versioned alongside content |
| **Automatic** | URLs update when images are regenerated and pushed |
| **Reliable** | GitHub has excellent uptime |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| **No CDN** | Served from GitHub's servers, not edge-cached globally |
| **Rate Limiting** | GitHub may rate-limit if accessed very frequently |
| **Performance** | Slower than dedicated image hosts (~200-300ms TTFB) |
| **Public Repo Required** | Private repos require authentication tokens |

### Best For

- Small to medium projects (< 10,000 image views/month)
- Development and testing
- Projects already using GitHub

---

## Option 2: GitHub Pages Hosting

Serve images from a GitHub Pages site for better caching and custom domain support.

### URL Format

```
https://{username}.github.io/{repo}/images/image.png
```

Or with custom domain:
```
https://bootcamp.example.com/images/image.png
```

### How to Set Up

1. **Enable GitHub Pages** in repo settings:
   - Go to Settings → Pages
   - Source: Deploy from branch `main`
   - Folder: `/statistics/final_bootcamp` (or root)

2. **Update image URLs** to use GitHub Pages URL:
   ```bash
   # Create a modified version of update_image_urls.py
   # or manually update the base URL pattern
   ```

3. **Wait for deployment** (usually 1-5 minutes)

### Pros

| Advantage | Description |
|-----------|-------------|
| **Free** | No additional costs |
| **Better Caching** | GitHub Pages has CDN-like caching |
| **Custom Domains** | Can use your own domain |
| **HTTPS** | Automatic SSL certificates |
| **Slightly Faster** | Better optimized for static assets |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| **Setup Required** | Need to enable and configure GitHub Pages |
| **Build Time** | Changes take 1-5 min to deploy |
| **Bandwidth Limit** | 100 GB/month soft limit |
| **Public Only** | Repository must be public (or use GitHub Pro) |

### Best For

- Projects already using GitHub Pages for documentation
- When you need a custom domain
- Slightly better performance than raw URLs

---

## Option 3: Image CDN Services

Use a dedicated image hosting/CDN service for optimal performance.

### Popular Options

| Service | Free Tier | Paid Plans | Key Features |
|---------|-----------|------------|--------------|
| **Cloudinary** | 25 GB bandwidth/month | From $99/mo | Transformations, optimization |
| **imgix** | None | From $100/mo | Real-time processing |
| **ImageKit** | 20 GB bandwidth/month | From $49/mo | Smart optimization |
| **Uploadcare** | 3,000 uploads/month | From $25/mo | Easy integration |
| **Cloudflare Images** | N/A | $5/100K images | Edge delivery |

### Example: Cloudinary Setup

1. **Sign up** at [cloudinary.com](https://cloudinary.com)

2. **Upload images** via API or dashboard:
   ```python
   import cloudinary.uploader
   
   cloudinary.config(
       cloud_name="your_cloud",
       api_key="your_key",
       api_secret="your_secret"
   )
   
   for image_file in Path("images").glob("*.png"):
       result = cloudinary.uploader.upload(image_file)
       print(f"{image_file.name}: {result['secure_url']}")
   ```

3. **Update markdown files** with Cloudinary URLs:
   ```markdown
   ![Normal Distribution](https://res.cloudinary.com/your_cloud/image/upload/v1234/normal_curve.png)
   ```

### Pros

| Advantage | Description |
|-----------|-------------|
| **Fast** | Global CDN with 30-50ms TTFB |
| **Optimized** | Automatic format conversion (WebP, AVIF) |
| **Transformations** | Resize, crop, watermark on-the-fly |
| **Analytics** | Usage tracking and insights |
| **Reliable** | Enterprise-grade uptime SLAs |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| **Cost** | Free tiers are limited; scales up quickly |
| **Vendor Lock-in** | URLs are service-specific |
| **Setup Complexity** | Requires account setup, API integration |
| **URL Management** | Need to track/store CDN URLs separately |

### Best For

- High-traffic production sites
- Projects needing image transformations
- Professional/commercial deployments

---

## Option 4: Notion Native Upload via API

Upload images directly to Notion's servers using the API.

### How It Works

Notion's API supports file uploads to their AWS S3 infrastructure:

1. **Request upload URL** from Notion API
2. **Upload file** to the presigned S3 URL
3. **Reference file** in the image block

### API Flow (Conceptual)

```python
# Note: Notion's file upload API has limitations
# This is a simplified example

# Step 1: Create image block with file upload
response = notion.blocks.children.append(
    block_id=page_id,
    children=[{
        "object": "block",
        "type": "image",
        "image": {
            "type": "file",
            "file": {
                "url": "...",  # Obtained from upload
                "expiry_time": "..."
            }
        }
    }]
)
```

### Current Limitations

As of 2024, Notion's public API has **limited file upload support**:

- File uploads require OAuth authentication (not API tokens)
- Uploaded file URLs expire after ~1 hour
- No public API for permanent file hosting
- Must use `external` type for persistent images

### Pros

| Advantage | Description |
|-----------|-------------|
| **Native** | Images stored directly in Notion |
| **No External Deps** | No third-party services needed |
| **Integrated** | Managed alongside content |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| **Limited API** | File upload API is restricted |
| **Expiring URLs** | Uploaded files have temporary URLs |
| **OAuth Required** | Can't use simple API tokens |
| **No Bulk Upload** | Tedious for many images |

### Best For

- Manual, one-off image additions
- When you need images inside Notion's ecosystem
- **NOT recommended** for automated publishing

---

## Option 5: Self-Hosted / S3 Bucket

Host images on your own infrastructure or cloud storage.

### Options

| Platform | Setup Complexity | Cost | Performance |
|----------|-----------------|------|-------------|
| **AWS S3 + CloudFront** | Medium | Pay per use | Excellent |
| **Google Cloud Storage** | Medium | Pay per use | Excellent |
| **DigitalOcean Spaces** | Low | $5/mo base | Good |
| **Backblaze B2 + Cloudflare** | Medium | Very low | Good |
| **Self-hosted (VPS)** | High | VPS cost | Variable |

### Example: AWS S3 + CloudFront

1. **Create S3 bucket** with public read access
2. **Upload images** to bucket
3. **Create CloudFront distribution** pointing to bucket
4. **Update URLs** to use CloudFront domain

```
https://d1234567890.cloudfront.net/images/normal_curve.png
```

### Pros

| Advantage | Description |
|-----------|-------------|
| **Full Control** | Own your infrastructure |
| **Scalable** | Handle any traffic level |
| **Custom Domain** | Use your own branding |
| **Cost Effective** | Can be cheaper at scale |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| **Setup Effort** | Requires infrastructure knowledge |
| **Maintenance** | You manage uptime, security |
| **Costs** | Need to monitor and control |
| **Complexity** | More moving parts |

### Best For

- Enterprise deployments
- When you need full control
- High-traffic production sites
- Existing cloud infrastructure

---

## Comparison Matrix

| Criteria | GitHub Raw | GitHub Pages | CDN (Cloudinary) | Notion Native | Self-Hosted |
|----------|------------|--------------|------------------|---------------|-------------|
| **Cost** | Free | Free | Freemium | Free | Variable |
| **Setup** | ✅ Easy | ⚠️ Medium | ⚠️ Medium | ❌ Difficult | ❌ Complex |
| **Performance** | ⚠️ OK | ⚠️ OK | ✅ Fast | ✅ Fast | ✅ Fast |
| **Reliability** | ✅ High | ✅ High | ✅ High | ⚠️ Limited | ⚠️ Depends |
| **Maintenance** | ✅ None | ✅ Minimal | ⚠️ Some | ✅ None | ❌ High |
| **URL Stability** | ✅ Stable | ✅ Stable | ✅ Stable | ❌ Expires | ✅ Stable |
| **Works with Notion** | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ Limited | ✅ Yes |

---

## Recommended Approach

### For This Bootcamp: **GitHub Raw URLs** (Already Done)

**Why:**
1. ✅ Already set up and working
2. ✅ Free, no additional services
3. ✅ Images version-controlled with content
4. ✅ `publish_to_notion.py` already handles external URLs
5. ✅ Sufficient for educational content (~hundreds of views)

### Upgrade Path (If Needed)

If you experience performance issues or need higher traffic capacity:

1. **Quick upgrade:** Enable GitHub Pages (free, better caching)
2. **Best performance:** Migrate to Cloudinary or ImageKit (free tier sufficient for most cases)

---

## How It Works with publish_to_notion.py

The existing `publish_to_notion.py` script already handles external image URLs correctly.

### Image Handling in the Script

From `publish_to_notion.py` lines 124-141:

```python
# Image
elif stripped.startswith('!['):
    match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
    if match:
        alt_text, url = match.groups()
        if url.startswith('http'):
            # Creates proper Notion image block
            blocks.append({
                "object": "block",
                "type": "image",
                "image": {"type": "external", "external": {"url": url}}
            })
        else:
            # Fallback for local paths (should not happen if URLs updated)
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": f"[Image: {alt_text}]"}}]}
            })
```

### Publishing Workflow

```bash
# 1. Generate images
python3 statistics/tools/generate_images.py

# 2. Commit and push to GitHub
git add statistics/final_bootcamp/images/
git commit -m "Update images"
git push

# 3. Convert to GitHub URLs (already done, but can re-run)
python3 statistics/tools/update_image_urls.py \
    --username janickspirig \
    --repo stats_bootcamp \
    --branch main

# 4. Commit URL changes
git add statistics/final_bootcamp/
git commit -m "Update image URLs"
git push

# 5. Publish to Notion
export NOTION_TOKEN="secret_xxx"
export NOTION_ROOT_PAGE_ID="your_page_id"
python3 statistics/tools/publish_to_notion.py

# 6. (Optional) Revert to relative paths for local dev
python3 statistics/tools/update_image_urls.py --revert
```

---

## Troubleshooting

### Images Not Appearing in Notion

| Symptom | Cause | Solution |
|---------|-------|----------|
| Placeholder text instead of image | URL starts with `../` (relative) | Run `update_image_urls.py` to convert to GitHub URLs |
| Image shows broken icon | URL is incorrect or file doesn't exist | Verify URL is accessible in browser |
| Image loads slowly | GitHub raw URLs have higher latency | Consider GitHub Pages or CDN |
| Rate limit errors | Too many requests to GitHub | Wait and retry, or use CDN |

### Verify Image URL Works

```bash
# Test that an image URL returns HTTP 200
curl -sI "https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/normal_curve.png" | head -n 1
# Expected: HTTP/2 200
```

### Check Current URL Status

```bash
python3 statistics/tools/update_image_urls.py --status
```

---

## Summary

| If you need... | Use... |
|----------------|--------|
| Quick, free, simple | **GitHub Raw URLs** ✅ (current setup) |
| Better caching, custom domain | **GitHub Pages** |
| Best performance, transformations | **Cloudinary / ImageKit** |
| Full control, enterprise scale | **AWS S3 + CloudFront** |

**For this bootcamp:** The current GitHub Raw URLs setup is sufficient and already working. No changes needed unless performance becomes an issue.

---

*Last updated: December 2024*

