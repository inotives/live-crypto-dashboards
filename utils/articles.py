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

ARTICLES = [
{
    "post_title": "Data Analysis in Crypto using OHLCV data",
    "post_date": '2024-08-01',
    "author": 'InoTives',
    "post_image_url": "",
    "post_md": markdown_files['data_analysis_in_crypto_using_ohlcv.md']
},
{
    "post_title": "Playing with M/L in python",
    "post_date": '2024-09-01',
    "author": 'InoTives',
    "post_image_url": "",
    "post_md": markdown_files['playing_with_ml_in_python.md']
},
{
    "post_title": "Linear regression with OHLCV data for forecasting bitcoin price.",
    "post_date": '2024-07-15',
    "author": 'InoTives',
    "post_image_url": "",
    "post_md": markdown_files['linear_regression_with_ohlcv_forecasting_btc_price.md']
}
]