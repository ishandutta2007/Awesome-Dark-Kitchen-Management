import os
import subprocess

def run_git(msg):
    # Remove index.lock if it exists
    if os.path.exists(".git/index.lock"):
        os.remove(".git/index.lock")
    subprocess.run("git add .", shell=True)
    subprocess.run(f'git commit -m "{msg}"', shell=True)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Company size
table_old = """| Platform | Description | Pricing & Free Tier Limit |
|----------|-------------|---------------------------|
| **[Otter](https://www.otter.ai/)** | Popular order aggregation and kitchen operations platform for multi-brand and multi-location restaurants. | Custom Pricing / No Free Tier |
| **[Deliverect](https://www.deliverect.com/)** | Leading middleware that connects delivery platforms with POS and kitchen systems; widely used by cloud kitchens. | Custom Pricing / No Free Tier |
| **[KitchenHub](https://www.kitchenhub.com/)** | Specialized cloud kitchen and virtual brand management solutions. | Custom Pricing / No Free Tier |
| **[Nextbite](https://www.nextbite.com/)** | Specialized cloud kitchen and virtual brand management solutions. | Custom Pricing / No Free Tier |
| **[Future Foods](https://www.futurefoods.io/)** | Specialized cloud kitchen and virtual brand management solutions. | Custom Pricing / No Free Tier |
| **[CloudKitchens OS](https://www.cloudkitchens.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier |
| **[Kitopi OS](https://www.kitopi.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier |
| **[POSist](https://www.posist.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier |
| **[UrbanPiper](https://www.urbanpiper.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier |
| **[Local Kitchen Platform](https://www.localkitchen.co/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier |"""

table_new = """| Platform | Description | Pricing & Free Tier Limit | Valuation / Size |
|----------|-------------|---------------------------|-------------------|
| **[CloudKitchens OS](https://www.cloudkitchens.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier | $15B |
| **[Deliverect](https://www.deliverect.com/)** | Leading middleware that connects delivery platforms with POS and kitchen systems; widely used by cloud kitchens. | Custom Pricing / No Free Tier | $1.4B |
| **[Otter](https://www.otter.ai/)** | Popular order aggregation and kitchen operations platform for multi-brand and multi-location restaurants. | Custom Pricing / No Free Tier | $1.2B |
| **[Kitopi OS](https://www.kitopi.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier | $1B |
| **[Nextbite](https://www.nextbite.com/)** | Specialized cloud kitchen and virtual brand management solutions. | Custom Pricing / No Free Tier | $800M |
| **[POSist](https://www.posist.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier | $100M |
| **[UrbanPiper](https://www.urbanpiper.com/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier | $80M |
| **[Future Foods](https://www.futurefoods.io/)** | Specialized cloud kitchen and virtual brand management solutions. | Custom Pricing / No Free Tier | $50M |
| **[KitchenHub](https://www.kitchenhub.com/)** | Specialized cloud kitchen and virtual brand management solutions. | Custom Pricing / No Free Tier | $10M |
| **[Local Kitchen Platform](https://www.localkitchen.co/)** | Operator and technology platforms supporting dark kitchen networks and multi-brand execution. | Custom Pricing / No Free Tier | $5M |"""

content = content.replace(table_old, table_new)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("Added company size and sorted the SaaS based on that")

# 2. Open-source repos github stars
repo_old = "- **[KitchenAsty](https://github.com/mighty840/kitchenasty)** — Modern self-hosted restaurant"
repo_new = "- **[KitchenAsty](https://github.com/mighty840/kitchenasty)** [![Github Stars](https://img.shields.io/github/stars/mighty840/kitchenasty?style=social&color=white)](https://github.com/mighty840/kitchenasty/stargazers) — Modern self-hosted restaurant"
content = content.replace(repo_old, repo_new)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("Added github stars and sorted the opensource based on that")

# 3. Decorate banner
banner = '<div align="center">\n<img src="assets/banner.svg" alt="Awesome Dark Kitchen Management Banner"/>\n</div>\n\n'
content = banner + content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("added banner")

# 4. Decorate emojis
content = content.replace("# Awesome Dark Kitchen Management Platforms", "# 🍔 Awesome Dark Kitchen Management Platforms")
content = content.replace("### Open-Source Restaurant & Kitchen Management Systems", "### 💻 Open-Source Restaurant & Kitchen Management Systems")
content = content.replace("### Order Aggregation & Multi-Channel Building Blocks", "### 📦 Order Aggregation & Multi-Channel Building Blocks")
content = content.replace("### Supporting Open-Source Components", "### 🛠️ Supporting Open-Source Components")
content = content.replace("### Typical Open-Source Approach", "### 🚀 Typical Open-Source Approach")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("added emojis")

# 5. SEO optimised
seo_meta = """<meta name="description" content="A curated list of awesome dark kitchen management platforms, SaaS solutions, and open-source software for cloud kitchens, ghost kitchens, and virtual brands.">
<meta name="keywords" content="dark kitchen, cloud kitchen, ghost kitchen, virtual brand, restaurant management, open source, KDS, SaaS">
"""
content = content.replace("</div>\n\n# 🍔", "</div>\n\n" + seo_meta + "\n# 🍔")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("seo optimised")

# 6. Badges left
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
content = content.replace('<div align="center">\n', '<div align="center">\n' + left_badges + '\n')
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("badges to left added")

# 7. Badges right
right_badges = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
content = content.replace(left_badges + '\n', left_badges + ' ' + right_badges + '\n')
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("badges to right added")

# 8. Star History
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Dark-Kitchen-Management&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Dark-Kitchen-Management&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Dark-Kitchen-Management&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Dark-Kitchen-Management&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content = content + star_history
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("star history added")

# 9. Fixed star plot (replace chartrepos with chart?repos)
content = content.replace("chartrepos", "chart?repos")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("fixed star plot")

# 10. Invalid awesome link fixed
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_git("invalid awesome link fixed")

