import os
certs_dir = '/home/mihkuno/projects/portfolio/public/certs'
exclude = ['cisco.png', 'langchain.jpg', 'langgraph.jpg']
files = [f for f in os.listdir(certs_dir) if f not in exclude and f.endswith(('.png', '.jpg', '.jpeg'))]
files.sort()
html_snippets = []
for f in files:
    html_snippets.append(f'    <img src="public/certs/{f}" style="width:100%; height:180px; object-fit:cover; border:1px solid var(--border); border-radius:8px; cursor:pointer; transition: transform 0.2s;" onmouseover="this.style.transform=\'scale(1.02)\'" onmouseout="this.style.transform=\'scale(1)\'" onclick="window.open(this.src, \'_blank\')" loading="lazy" alt="{f}">')

with open('/tmp/html_out.txt', 'w') as f:
    f.write('\n'.join(html_snippets))
