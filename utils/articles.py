from pathlib import Path
import utils.settings as config

ARTICLE_PATH = Path(config.ARTICLE_DIR)

# Initialize an empty dictionary
markdown_files = {}

# Loop through all markdown files in the folder
for file in ARTICLE_PATH.glob('*.md'):
    # Read the content and store it in the dictionary
    with file.open('r', encoding='utf-8') as f:
        markdown_files[file.name] = f.read()

def set_articles(title, post_date, author, post_md, post_image_url=''):

    return {
        "post_title": title,
        "post_date": post_date,
        "author": author,
        "post_image_url": post_image_url,
        "post_md": post_md
    }

ARTICLES = [
    set_articles('Data Analysis in Crypto using OHLCV data', '2024-08-01', 'InoTives', 'data_analysis_in_crypto_using_ohlcv.md', 'https://img.playbook.com/ftkOGVTEXTDCOJQYJr-sdniP50wnhDi1c-6y59ybwJI/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzdiNTE5Nzkw/LThlMTktNDFkYi1i/NjVkLWRmYTc0MTBi/NmZmNg' ),
    set_articles('Using Machine Learning in Crypto OHLCV Data', '2024-09-01', 'InoTives', 'using-machine-learning-in-crypto-ohlcv-data.md','https://img.playbook.com/WQO74KfJnl4Izy50eN5idqpEE7Lft1kLmteH89zyVnw/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzdlODY0M2Vh/LTQ1ZTctNGU1MS1i/Y2Y3LTBlY2EzZGNh/YzEwZA' ),
    set_articles('Python Fundemental for Data Analysis', '2024-06-15', 'InoTives', 'python-fundemental-for-data-analysis.md','https://img.playbook.com/CkV_U5khbzznyb50-ijsGkBQcU42oqfO34mceRjwWL8/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzAwNjlmNjgw/LWUwNTktNDNiMS04/NTBlLTdjNjY2Yzcw/Y2ZmYg' )
]