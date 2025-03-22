import os
import markdown
from fpdf import FPDF

# this will save the generated topic into html pdf txt and md in the blog dir 
def save_blog(topic, content):
    safe_topic = topic.lower().replace(" ", "_")
    folder_path = f"blogs/{safe_topic}"
    os.makedirs(folder_path, exist_ok=True)

    with open(f"{folder_path}/{safe_topic}.md", "w", encoding="utf-8") as md_file:
        md_file.write(content)

    with open(f"{folder_path}/{safe_topic}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(content)

    html_content = f"""
    <html>
    <head>
        <title>{topic} - SEO Optimized</title>
        <meta name="description" content="An in-depth blog on {topic}, optimized for search engines.">
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }}
            h1, h2, h3 {{ color: #333; }}
            p {{ font-size: 18px; }}
        </style>
    </head>
    <body>
        {markdown.markdown(content)}
    </body>
    </html>
    """
    with open(f"{folder_path}/{safe_topic}.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line.encode('latin-1', 'replace').decode('latin-1'))

    pdf.output(f"{folder_path}/{safe_topic}.pdf")

    print(f"✅ Blog saved in '{folder_path}' as Markdown, TXT, HTML, and PDF.")
    